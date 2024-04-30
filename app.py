import streamlit as st
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cluster import KMeans


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
        st.text('업로드 하신 csv파일의 데이터는 다음과 같습니다.')
        st.dataframe(user_df)

        #1-2. isna() 메소드 이용
        df_isna = user_df.isna().sum()
        st.text('업로드 하신 데이터의 결측값(NaN) 존재 여부입니다.')
        st.dataframe(df_isna)
        st.info('결측값이 존재하면 해당 데이터는 삭제합니다.')
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
                st.info(f'원활한 클러스터링을 위해, {object_col_list} 컬럼은 인코딩 작업이 자동 수행됩니다.')
                #4-2. 필요한 Encoder 종류 파악
                label_encoder = LabelEncoder()
                one_hot_encoder = OneHotEncoder()
                for z in range(len(object_col_list)):
                    nunique = object_col_list[z].nunique()
                    if nunique >= 3 :
                        ct = ColumnTransformer([('encoder', OneHotEncoder(), object_col_list[z])], remainder='passthrough')
                        object_col_list[z] = ct.fit_transform(object_col_list[z])
                        user_df[sel_list][f'{z}'] = one_hot_encoder.transform(user_df[sel_list][f'{z}'])
                    else:
                        user_df[sel_list][f'{z}'] = label_encoder.transform(user_df[sel_list][f'{z}'])
            else:
                pass




            #5. WCSS 계산


            #6. Elbow method 이용하여 차트로 표현


            #7. 유저 임의의 k 개수 결정


            #8. KMeans 수행해서 그룹정보 가져오기


            #9. 본 데이터프레임에 그룹정보 컬럼 추가


            #10. 결과를 파일로 저장
        else:
            st.info('2개 이상의 컬럼을 선택하여야 클러스터링이 가능합니다')

    else :
        pass


if __name__ == '__main__':
    main()




