

![header](https://capsule-render.vercel.app/api?type=Venom&color=gradient&height=200&section=header&text=머신러닝%20웹%20대시보드&fontSize=60&fontAlignY=60&animation=fadeIn)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h5>머신 러닝(Machine Learning) 기법 중 군집화[Clustering]에 해당하는 K-Means 모델을 적용한 웹 대시보드 프로젝트입니다.</h5>
    <h5>사용자가 업로드한 csv 파일 데이터에 대해 임의의 k값에 따라 그룹화를 진행하여 결과를 표시하는 서비스를 제공합니다.</h5>
<br>
    <h6>■링크 : 링크 삽입 자리</h6>
<br>
<!--목차 1. 머신러닝 간략 소개-->
    <h3>1. 개괄</h3>
  <ol start="1" type="a">
    <li>머신러닝은 인간의 고등 지적능력인 '학습 - 추론'을 모방한 알고리즘임</li>
    <li>지도 학습[Supervised Learning]과 비지도 학습[Unsupervised Learning]으로 구분할 수 있으며, 비지도 학습은 알고리즘 모델에게 데이터에 대한 별도의 학습 과정이 필요치 않음.</li>
    <li>본 대시보드에서 사용한 군집화 모델은 비지도 학습에 해당되며, 데이터들의 특징들을 계산하여 유사한 것들끼리 그룹으로 구분</li>
    <li>실제 이용사례로는, B2C 기업이 고객 데이터를 유형별로 분류하여 타겟 고객층에 대한 마케팅 전략 세분화 및 정밀 기획 등이 있음</li>
  </ol>
<br>    
<!--목차 2. 개발목적 표기-->
    <h3>2. 개발 목적</h3>
  <ul>
    <li>사용자 임의의 CSV파일 속 데이터에 대해 인공지능 모델을 통해 군집화한 결과를 제공하여, 마케팅을 비롯한 경영 기획 등 실생활 속 다양한 의사결정에 도움이 되는 서비스 구현을 목적으로 함</li>
  </ul>
<br>
<!--3. 개발방법 서술-->
    <h3>3. 개발 방법</h3>
  <ol start="1" type="a">
    <li>로컬에 Anaconda Prompt로 가상환경 생성하고 Python(ver 3.10) 및 주요 라이브러리(numpy, pandas, matplotlib, seaborn, scikit-learn, joblib, ipython, pillow, jupyter) 설치하여 개발환경 구축 </li>
    <li>Github에 원격 Repository를 생성하고 Github Desktop을 이용해서 로컬에 clone한 뒤 Visual Studio Code로 연동하여 작업환경 구성</li>
    <li>먼저, 코드 결과를 즉시 확인하기 편리한 jupyter notebook에서 작업</li>
    <ol start="1" type="1">
      <li>모델 생성(학습 및 성능평가)에 사용할 csv파일 준비 및  pandas의 read_csv() 메소드 이용하여 DataFrame으로 저장</li>
      <li>라벨링 상태 확인 후 isna().sum()으로  결측값(NaN 등) 존재여부 조회 및 해당 데이터 drop</li>
      <li>전체 컬럼 중 학습에 사용할 (타겟)컬럼 분리(ex> id 등 예측 목적에 상관 없는 컬럼들을 제외)</li>
      <li>분리한 컬럼들 중 dtype이 object인 경우 Encoding 작업 수행하되, 해당 cartegorical column의 nunique 값에 따라 구분</li>
        <ul>
          <li>-nunique >= 3 경우 sklearn의 ColumnTransformer와 OneHotEncoder 이용</li>
          <li>nunique <= 2 경우 sklearn의 LabelEncoder 이용</li>
        </ul>
      <li>clustering의 경우 feature scaling, train_test_split이 필요 없으므로 생략</li>
      <li>kmeans 모델 생성 후 최적의 k값을 찾기 위해 wcss를 계산하고 matplotlib으로 시각화하여 elbow method로 확인</li>
      <li>최적의 k 값을 대입시켜 다시 kmeans 모델 생성</li>
      <li>위에서 encoding까지 끝난 데이터프레임을 다시 생성한 kmeans 모델에 대입하고 이 predict 결과를 'Group'컬럼으로 만들어 데이터프레임에 추가한 뒤 점검</li>
      <li>생성한 모델을 .pkl 파일로 저장</li>
    </ol>
    <li>clone한 repository 폴더에 app.py 파일을 만들고 Visual Studio Code로 위 과정의 소스코드를 빌드하며 streamlit run app.py로 작동여부 확인하며 디버깅</li>
    <li>빌드 및 디버깅 완료 후 commit하고 Github 원격 repository에 push까지 마무리</li>
    <li>서버로 사용할 AWS EC2 인스턴스를 생성하고 OS는 Amazon Linux로 설정</li>
    <li>원격 접속을 위해 PuTTY에 실행시 해당 인스턴스의 퍼블릭 IP address와 키 페어 .ppk파일 경로 정보 저장</li>
    <li>PuTTY로 해당 인스턴스에 원격 접속하여 Anaconda 설치 후 개발 환경과 동일한 조건의 가상환경(Python 3.10, 주요 library 설치) 생성</li>
    <li>서버에 Git 소프트웨어 설치 후 위와 동일한 Github Repository를 clone한 뒤 해당 파일을 pull하여 저장</li>
    <li>$ nohup streamlit run app.py --server.port [포트넘버] 명령어로 백그라운드 실행</li>
    <li>해당 인스턴스가 속한 보안 그룹의 인바운드 규칙을 편집하여 접근 가능하도록 방화벽 설정(해당 포트 오픈)</li>
    <li>AWS EC2 인스턴스에 할당된 퍼블릭 IP address를 웹 브라우저에 입력하여 서비스 배포 여부 최종 확인</li>
  </ol>
<br>
<!--목차 4. 개발환경 요약-->
    <h3>4. 개발 환경</h3>
  <ol start="1" type="a">
    <li>[가상환경] : Anaconda를 사용하여 가상환경(Python 3.10, 주요 라이브러리 설치) 생성</li>
    <li>[코드 에디터] : Visual Studio Code, Jupyter Notebook</li>
    <li>[프레임워크] : Streamlit</li>
    <li>[주요 라이브러리] : numpy, pandas, matplotlib, seaborn, scikit-learn, joblib, ipython, pillow, jupyter</li>
    <li>[버전 관리] : Github Desktop를 이용하여 원격 레포지토리에서 로컬로 clone한 뒤 작업시 commit & push</li>
    <li>[서버 관리] : AWS EC2 클라우드 컴퓨팅 서비스 이용하여 인스턴스 생성 후 PuTTY로 원격접속하여 개발 환경과 동일한 가상 환경으로 관리</li>
    <li>[서비스 방법] : Github 원격 레포지토리에서 작업 파일을 EC2 서버에 pull하여 업로드하고 백그라운드 실행 설정 및 개별 포트 지정하여 하나의 서버에서 여러 대시보드 가동하도록 설정</li>
  </ol>
<br>
<!--목차 5. 개발이슈 표기-->
    <h3>5. 개발 이슈</h3>
  <ol start="1" type="a">
    <li>사용자가 업로드한 csv 파일의 데이터 개수(데이터프레임의 행의 개수)가, wcss 계산에 사용될 k값보다 적을 경우 오류 발생</li>
      <ul>
        <li>sol : 유저가 업로드한 DataFrame의 Shape를 검사하고 조건문을 설정하여, 데이터의 수가 k값보다 적을 경우 return 처리하고 경고 메세지 표시</li>
      </ul>
    <li>사용자가 업로드한 자료에 결측값(NaN 등)이 존재할 경우 데이터 분석시 오류 발생</li>
      <ul>
        <li>sol : isna() 메소드를 이용하여 결측값 존재 여부를 파악한 뒤 해당하는 데이터는 자동으로 삭제하도록 처리</li>
      </ul>
    <li>사용자가 업로드한 자료에 문자열로 이루어진 카테고리컬 데이터 컬럼이 있을 경우 데이터 분석에 오류 발생</li>
      <ul>
        <li>sol : scikit-learn의 Encoder, ColumnTransformer를 활용하여 숫자 데이터로 변환하도록 처리</li>
      </ul>
  </ol>
<br>
<!--목차 6. 개발 및 서비스 한계-->
    <h3>6. 개발 및 서비스 한계</h3>
  <ol start="1" type="a">
    <li>CSV 파일의 데이터 중 범주형(categorical) 컬럼의 고윳값(unique) 개수가 많은 경우, Encoding 작업시 컬럼의 개수가 과도하게 많아져 FreeTier 등급의 성능으로는 처리가 불가능함. 때문에 본 서비스에서는 카테고리컬 컬럼의 nunique 값이 약 4~5 이상인 경우 리소스 제한 문제로 인하여 서비스 제공이 원활하지 않음.<br>
    (sol) : 데이터 개수(행의 개수)에 대한 해당 컬럼의 nunique 값의 비율이 60% 이상이면 클러스터링 작업이 무의미해지므로, 이와 같은 케이스는 제외하도록 조건문으로 처리</li>
  </ol>
  <br>
  <br>
</body>
</html>



![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=footer&text=Thanks%20for%20Reading&fontSize=50)

<!--파이썬 아이콘-->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

<!--주피터노트북 아이콘-->
![JupyterNotebook](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

<!--아마존 AWS 아이콘-->
![](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

<!--비주얼 스튜디오 코드 아이콘-->
![VSC](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

