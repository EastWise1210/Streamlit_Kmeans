<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>


<body>
    <h2>웹 대시보드</h2>
    <h5>머신 러닝(Machine Learning) 기법 중 군집화[Clustering]에 해당하는 K-Means 모델을 적용한 웹 대시보드 미니 프로젝트입니다.</h5>
    <h5>사용자가 업로드한 csv 파일 데이터에 대해 임의의 k값에 따라 그룹화를 진행하여 결과를 표시하는 서비스를 제공합니다.</h5>
<br>
    <h6>링크 : 링크 삽입 자리</h6>
<br>
<!--목차 1. 머신러닝 간략 소개-->
    <h3>1. 개괄</h3>
  <ol start="1" type="a">
    <li>머신러닝(Machine Learning)은 인간의 고등 지적능력인 '학습 - 추론'을 모방한 알고리즘입니다.</li>
    <li>지도 학습[Supervised Learning]과 비지도 학습[Unsupervised Learning]으로 구분할 수 있으며, 비지도 학습은 알고리즘 모델에게 데이터에 대한 별도의 학습 과정이 필요 없습니다.</li>
    <li>본 대시보드에서 사용한 군집화 모델은 비지도 학습에 해당되며, 데이터들의 특징들을 계산하여 유사한 것들끼리 그룹으로 구분합니다.</li>
    <li>실제 이용사례로는, B2C 기업이 고객 데이터를 유형별로 분류하여 타겟 고객층에 대한 마케팅 전략 세분화 및 정밀 기획 등이 있습니다.</li>
  </ol>
<br>    
<!--목차 2. 개발환경 표기-->
    <h3>2. 개발 환경</h3>
  <ol start="1" type="a">
    <li>[가상환경] : Anaconde를 사용하여 Python 3.10 버전의 가상환경 구축</li>
    <li>[코드 에디터] : Visual Studio Code, Jupyter Notebook 활용</li>
    <li>[프레임워크] : Streamlit 사용</li>
    <li>[주요 라이브러리] : Numpy, Pandas, Scikit-Learn, joblib 이용</li>
    <li>[버전 관리] : Git Desktop 소프트웨어를 이용하여 Github 원격 레포지토리에서 로컬로 clone한 후 매 작업시 commit & push하여 관리</li>
    <li>[서버 관리] : AWS(Amazon Web Service) EC2 클라우드 컴퓨팅 서비스 FreeTier 등급을 이용하여 인스턴스 리소스를 할당받고 PuTTY로 원격 접속하여 OS(Amazon Linux) 설치 및 개발 환경과 동일한 가상 환경(Python=3.10, 주요 라이브러리 install) 구축, 관리</li>
    <li>[서비스 방법] : 본 작업 파일을 상기에 서술한 EC2 리소스에 업로드하여 서버에서 원격접속 터미널 종료 후에도 동작 가능토록 백그라운드 실행 설정 및 포트 지정하여 하나의 서버에서 여러 대시보드 가동하도록 설정</li>
  </ol>
<br>
<!--목차 3. 개발 목적 표기-->
    <h3>3. 개발 목적</h3>
  <ol start="1" type="a">
    <li>머신 러닝(Machine-Learning) 기법 중 군집화[Clustering]에 해당하는 K-Means 모델을 적용하여, 사용자가 입력한 CSV(Comma Seperated Value)파일 자료의 데이터들을 그룹화하는 기능을 구현해서, 해당 자료[data]에 대한 의사결정에 도움이 되는 정보[information] 제공을 목적으로 하였습니다.</li>
  </ol>
<br>
<!--목차 4. 개발 이슈-->
    <h3>4. 개발 이슈</h3>
  <ol start="1" type="a">
    <li>사용자가 업로드한 csv 파일의 데이터 개수(데이터프레임의 행의 개수)가, wcss 계산에 사용될 k값보다 적을 경우 오류 발생<br>
        (sol) : 유저가 업로드한 DataFrame의 Shape를 검사하고 조건문을 설정하여, 데이터의 수가 k값보다 적을 경우 return 처리하고 경고 메세지 표시 </li>
    <li>사용자가 업로드한 자료에 결측값(NaN 등)이 존재할 경우 데이터 분석시 오류 발생<br>
        (sol) : isna() 메소드를 이용하여 결측값 존재 여부를 파악한 뒤 해당하는 데이터는 자동으로 삭제하도록 처리</li>
    <li>사용자가 업로드한 자료에 문자열로 이루어진 카테고리컬 데이터 컬럼이 있을 경우 데이터 분석에 오류 발생<br>
        (sol) : scikit-learn의 Encoder, ColumnTransformer를 활용하여 숫자 데이터로 변환하도록 처리</li>
  </ol>
<br>
<!--목차 5. 개발 및 서비스 한계-->
    <h3>5. 개발 및 서비스 한계</h3>
  <ol start="1" type="a">
    <li>본 서비스에 업로드한 CSV 파일의 데이터프레임에서 카테고리컬 컬럼의 unique(고윳값)의 개수가 많은 경우, Encoding 후 해당 컬럼의 개수가 과도하게 많아져 EC2 FreeTier 등급의 리소스로는 하드웨어적으로 처리가 불가능함. 때문에 본 서비스에서는 카테고리컬 컬럼의 nunique 값이 4~5 이상인 경우 리소스 제한 문제로 인하여 서비스 제공이 원활하지 않음.</li>
  </ol>
</body>
</html>