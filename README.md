# Streamlit_Kmeans



[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=eEastWise1210](https://github.com/anuraghazra/github-readme-stats)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>웹 대시보드</h2>
    <h6>머신 러닝(Machine Learning) 기법 중 군집화[Clustering]에 해당하는 K-Means 모델을 적용한 웹 대시보드 미니 프로젝트입니다.</h6>
    <br><br>
    <h3>1. 개발환경</h3>
    <p>(1)Anaconde를 사용하여 Python 3.10 버전의 가상환경 구축</p>
    <p>(2)코드 에디터 : Visual Studio Code, Jupyter Notebook 활용</p>
    <p>(3)프레임워크 : Streamlit 사용</p>
    <p>(4)주요 라이브러리 : Numpy, Pandas, Scikit-Learn, joblib 이용</p>
    <p>(5)버전 관리 : Git Desktop 소프트웨어를 이용하여 Github 원격 레포지토리에서 로컬로 clone한 후 매 작업시 commit & push하여 관리</p>
    <p>(6)서버 관리 : AWS(Amazon Web Service) EC2 클라우드 컴퓨팅 서비스 FreeTier 등급을 이용한 인스턴스 리소스를 할당받고 PuTTY로 원격 접속하여 개발 환경과 동일한 가상 환경(Python=3.10, 주요 라이브러리 install) 구축 및 관리</p>
<p>(7)서비스 방법 : 본 작업 파일을 (6)에서 서술한 EC2 리소스에 업로드하여 서버에서 원격접속 터미널 종료 후에도 동작 가능토록 백그라운드 실행 설정 </p>
</body>
</html>




<1> 개발환경



<2> 개발 목적
머신 러닝(Machine-Learning) 기법 중 군집화[Clustering]에 해당하는 K-Means 모델을 적용하여, 사용자가 입력한 CSV(Comma Seperated Value)파일 자료의 데이터들을 그룹화하는 기능을 구현해서, 해당 자료[data]에 대한 의사결정에 도움이 되는 정보[information] 제공을 목적으로 하였습니다.


<3> 개발 이슈
(1)사용자가 업로드한 csv 파일의 데이터 개수(데이터프레임의 행의 개수)가, wcss 계산에 사용될 k값보다 적을 경우 오류 발생
->유저가 업로드한 DataFrame의 Shape를 검사하고 조건문을 설정하여, 데이터의 수가 k값보다 적을 경우 return 처리하고 경고 메세지 표시 

(2)사용자가 업로드한 자료에 결측값(NaN 등)이 존재할 경우 데이터 분석시 오류 발생
->isna() 메소드를 이용하여 결측값 존재 여부를 파악한 뒤 해당하는 데이터는 자동으로 삭제하도록 처리

(3)사용자가 업로드한 자료에 문자열로 이루어진 카테고리컬 데이터 컬럼이 있을 경우 데이터 분석에 오류 발생
->scikit-learn의 Encoder, ColumnTransformer를 활용하여 숫자 데이터로 변환하도록 처리


<4> 개발 및 서비스 한계
본 서비스에 업로드한 CSV 파일의 데이터프레임에서 카테고리컬 컬럼의 unique(고윳값)의 개수가 많은 경우, Encoding 후 해당 컬럼의 개수가 과도하게 많아져 EC2 FreeTier 등급의 리소스로는 하드웨어적으로 처리가 불가능함. 때문에 본 서비스에서는 카테고리컬 컬럼의 nunique 값이 4~5 이상인 경우 리소스 제한 문제로 인하여 서비스 제공이 원활하지 않음.