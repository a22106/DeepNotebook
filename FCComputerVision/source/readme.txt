강의자료안내: source 폴더는 각 챕터별  실습프로젝트에 대한 (1) 실습코드, (2) 데이터자료를 포함하고 있습니다.

(0) 실습환경의 주요 프로세서와 주요설치 패키지는 아래와 같습니다.
- CPU: AMD Ryzen 5 3600 6-Core Processor
- Memory: 16.0 GB
- GPU: NVIDIA GeForce RTX 2060 RTX
- Python: 3.8.13
- Anaconda: conda 4.10.3
- Nvidia driver: 511.09
- CUDA: 11.1

(1) 실습코드 관련
 - 모든 실습은 jupyter notebook 환경에서 진행합니다.
 - Chapter0* 각 폴더에는 SOLUTION.ipynb 이름의 실습코드(솔루션)가 있습니다.
 - Chapter03, Chapter05, Chapter06, Chapter07 에서는 utils.py가 제공되고, 해당 스크립트는 각 챕터의 실습진행에 사용되는 함수호출에 필요합니다.
 - requirements.txt 에 실습진행을 위한 python 패키지버전이 있으니 command 창에 "pip install -r requirements.txt" 입력하여 설치하실 수 있습니다.

(2) 데이터 관련
 - DATASET은 압축된 상태이며, 원하시는 경로에 압축을 풀고 챕터별 실습데이터에 접근하실 수 있습니다.
   ㄴ DATASET/Classification 데이터 사용 실습챕터 : Chapter02
   ㄴ DATASET/Segmentation 데이터 사용 실습챕터 : Chapter03, Chapter04
   ㄴ DATASET/Detection, sample_video.mp4 데이터 사용 실습챕터 : Chapter05, Chapter06, Chapter07
   ㄴ DATASET/Face-Recognition 데이터 사용 실습챕터 : Chapter09, Chapter10

 - 실습의 학습과정에서 저장하는 학습모델은 trained_model 폴더에 저장되어 있어서, 로드하여 테스트해볼 수 있습니다.


문의사항 및 피드백이 있으시면 언제든지 주세요.
감사합니다.

문의: pjh5672.dev@gmail.com