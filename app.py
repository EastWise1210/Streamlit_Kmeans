import streamlit as st
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cluster import KMeans

import time
from progress import run_progress


def main():
    st.title('K-Means 군집화 앱')
    st.subheader('K-Means Clustering Application')
    st.text('.csv파일을 업로드하면 비슷한 유형의 데이터끼리 묶어주는(군집화, 그룹화) 앱입니다.')

    #0. csv 파일 업로드
    user_file = st.file_uploader('.csv파일을 업로드하세요', type=['csv'])


    #1. 결측값(NaN) 존재여부 파악
    if user_file is not None:
        #1-1. user_file을 데이터프레임화
        user_df = pd.read_csv(user_file, encoding='utf-8')

        if user_df.shape[0] < 10:
            st.warning('입력하신 자료의 데이터 개수가 10개 미만입니다. 다른 파일을 업로드해주십시오.')
            return
        

        else:
            st.text('업로드 하신 csv파일의 데이터는 다음과 같습니다.')
            st.dataframe(user_df)

            #1-2. isna() 메소드 이용
            df_isna = user_df.isna().sum()
            st.text('업로드 하신 데이터의 결측값(NaN) 존재 여부입니다.')
            st.dataframe(df_isna)
            st.warning('결측값이 존재하면 해당 데이터는 삭제합니다.')
            #1-3. 결측값 데이터 삭제
            user_df.dropna(inplace=True)
            #1-4. 인덱스 리셋&삭제
            user_df.reset_index(inplace=True)        
            user_df.drop('index', axis=1, inplace=True)

            #3. 컬럼 선택 가능 구현
            st.subheader('클러스터링에 사용할 컬럼 선택')
            st.text('X로 사용할 컬럼을 선택하세요')
            sel_list = st.multiselect(label='컬럼을 선택하세요', options=user_df.columns)
            X = user_df[sel_list]
            if sel_list != []:
                st.dataframe(X)
            else:
                pass 
            

            if len(sel_list) >= 2:
                #4-1. Encoding 필요 여부 파악
                check_type = user_df[sel_list].dtypes   #1차원 시리즈 데이터 - 인덱스:컬럼명 / 데이터:컬럼의 타입
                object_col_list = []   #인코딩 필요한 컬럼명 리스트
                for i in range(check_type.shape[0]):
                    if check_type[check_type.index[i]] == 'object':
                        object_col_list.append(check_type.index[i])
                    else:
                        pass

                if object_col_list != []:   #인코딩 필요한 컬럼 존재시 안내메세지
                    st.warning(f'원활한 클러스터링을 위해, {object_col_list} 컬럼은 인코딩 작업이 자동 수행됩니다.')

                    #4-2. 필요한 Encoder 종류 파악
                    label_encoder = LabelEncoder()
                    for z in object_col_list:   #타입이 object인 컬럼 중에서 nunique 개수에 따라 Label / OneHot 구분
                        nunique = X[f'{z}'].nunique()
                        if nunique >= 3 :
                            ct = ColumnTransformer([('encoder', OneHotEncoder(), X[f'{z}'])], remainder='passthrough')
                            X = ct.fit_transform(X)
                        else:
                            label_encoder.fit(X[f'{z}'])
                            X[f'{z}'] = label_encoder.transform(X[f'{z}'])
                else:
                    pass


                #5. WCSS 계산
                run_progress()
                wcss = []
                for i in range(1, 11):
                    kmeans = KMeans(n_clusters=i, random_state=10)
                    kmeans.fit(X)
                    wcss.append(kmeans.inertia_)
                #inertia_가 wcss값임  ->  wcss 값을 비교함으로 최적값 찾기


                #6. Elbow method 이용하여 차트로 표현
                st.line_chart(wcss)
                st.info('위 그래프는 최적의 k값을 찾기 위해 WCSS를 구한 결과입니다. 그래프를 참고하여 다음 입력란에 사용자 임의의 K값을 입력해주십시오.')
                user_sel_kval = st.number_input(label='값을 선택해주십시오.', min_value=0, max_value=10, value=0)


                #7. 유저 임의의 k 개수 결정
                if user_sel_kval != 0:
                    kmeans = KMeans(n_clusters=user_sel_kval, random_state=1)

                    #8. KMeans 수행해서 그룹정보 가져오기
                    y_pred = kmeans.fit_predict(X)
                    
                    #9. 본 데이터프레임에 그룹정보 컬럼 추가
                    X['Group'] = y_pred
                    st.info(f'아래는 사용자께서 선택하신 k = {user_sel_kval}값의 개수로 클러스터링한 전체 결과입니다.')
                    st.dataframe(X)
                    sel_num = st.number_input(f'선택하신 k = {user_sel_kval} 범위 안에서 구성된 그룹 번호를 선택하시면 해당 그룹의 데이터를 하단에 보여드립니다.', min_value=0, max_value=user_sel_kval-1, value=0)
                    st.dataframe(X[X['Group'] == sel_num])


                    #10. 결과를 파일로 저장
                    import joblib
                    X.to_csv('Result_Dataframe.csv')
                    joblib.dump(kmeans, 'user_KMeans.pkl')
                    st.info('아래 버튼을 누르시면 작업 결과물을 파일로 다운로드하실 수 있습니다.')
                    df_down_button = st.download_button(label='데이터프레임 다운로드', data='./Result_Dataframe.csv', file_name='Result Dataframe.csv')
                    ml_down_button = st.download_button(label='머신러닝 모델 다운로드', data='./user_KMeans.pkl', file_name='user_KMeans.pkl')


                else:
                    st.info('k 개수를 선택하시면 클러스터링 작업을 수행하여 결과를 출력합니다.')



            else:
                st.info('2개 이상의 컬럼을 선택하여야 클러스터링이 가능합니다')

    else :
        pass


if __name__ == '__main__':
    main()