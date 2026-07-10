# 🌱 스마트팜 다분광 및 환경 데이터 기반 근권부 상태 예측 EDA

## 📖 프로젝트 개요
[cite_start]본 프로젝트는 1분 단위로 기록된 온실 환경(env) 데이터와 다분광 영상(ms) 데이터를 분석하여, **5분 뒤의 근권부(배지) 상태(함수율, EC, 온도)**를 예측하는 다중 출력(Multi-output) 모델 구축을 위한 탐색적 데이터 분석(EDA) 코드 및 문서입니다. [cite: 92, 95] [cite_start]온실 내외부 센서 데이터와 제어 구동기 작동 내역, 그리고 식물의 수분 스트레스를 파악할 수 있는 다분광 이미지를 융합하여 분석합니다. [cite: 93]

### 👥 Team
* **HBNU MAKER SUPPORTERS**

---

## 📊 데이터셋 구조 (Dataset Structure)

### 1. 환경 데이터 (Tabular - `env`)
* [cite_start]**형태:** 1분 단위 시계열 수치형 데이터 [cite: 92]
* **크기:**
  * [cite_start]`train_X.csv`: 37,440행 $\times$ 20열 (총 26일 치 데이터) [cite: 59, 94]
  * [cite_start]`test_X.csv`: 17,280행 $\times$ 20열 (총 12일 치 데이터) [cite: 59, 94]
* **변수 구성:**
  * [cite_start]**원인 변수 (입력):** 외부 온도, 일사량 등 내부 환경 변화를 유발하는 요인 [cite: 2, 44]
  * [cite_start]**조절 변수 (제어):** 천창 개폐, 차광 커튼, 팬코일유닛(FCU) 등 시스템이 작동시키는 장치 [cite: 9, 45]
  * [cite_start]**결과 변수 (출력):** 내부 온도, 습도, CO2 농도 등 제어 결과로 나타나는 식물 생육 환경 [cite: 45]

### 2. 다분광 영상 데이터 (Image - `ms`)
* [cite_start]**형태:** BSQ 방식의 바이너리 하이퍼스펙트럴 큐브 데이터 (`.raw`, `.hdr`) [cite: 93]
* [cite_start]**해상도:** $1280 \times 1024 \times 10$ Bands (가로 $\times$ 세로 $\times$ 파장 대역 수) [cite: 93]
* [cite_start]**활용:** 캘리브레이션 보정 패널(White Reference Panel)을 기준으로 잎사귀의 반사율을 측정하여 생육 상태 및 수분 스트레스 분석 [cite: 85, 87, 89]

---

## 🛠️ 주요 EDA 및 피처 엔지니어링 전략

### 1. 데이터 정합성 및 결측치/이상치 처리 (`env_check.py`, `outlier.py`)
* [cite_start]`train_X` 데이터 내 결측치(NaN) 0개 확인 완료. [cite: 59]
* [cite_start]모든 수치형 센서 데이터가 물리적 정상 범위(예: 외부 온도 -5.7 ~ 12.3도) 내에 존재함을 확인. [cite: 103]
* [cite_start]**상수 피처 제거:** 전체 기간 동안 작동하지 않은(고윳값 1개) `tube_rail_valve` 변수는 노이즈 방지를 위해 제거. [cite: 98, 99]

### 2. 시계열 피처 분해 및 시각화 (`visualization.py`)
* [cite_start]문자열 변수인 `time`을 `day`, `hour`, `minute` 수치형 변수로 완벽하게 분해하여 시계열 연속성 확보. [cite: 95, 96]
* **분석 결과:**
  * **내부 온도:** 히스토그램 및 Boxplot을 통한 분포 확인.
  * **가동 빈도:** 범주형(이진형) 제어 변수인 `fcu_fan` 등의 Count Plot 시각화.
  * [cite_start]**상관관계:** 일사량 증가에 따른 내부 온도 상승 및 조절 변수 작동 패턴 등을 Heatmap으로 분석. [cite: 13, 14]

### 3. 다파장 영상 데이터 파싱 (`mv_image.py`)
* Numpy를 활용해 1차원 Unsigned 16-bit 바이너리 배열을 3차원 큐브 `(1024, 1280, 10)` 형태로 Reshape.
* Band 0 (713nm) 등 특정 파장 대역의 2차원 평면 이미지를 Matplotlib으로 시각화 및 검증.

---

## 🚀 넥스트 스텝 (To-Do)
- [ ] [cite_start]시계열 예측 성능 극대화를 위한 이동 평균(Rolling Mean) 및 직전 값(Lag) 파생 변수 생성 [cite: 96]
- [ ] 다분광 이미지에서 잎사귀 반사율 수치 및 식생지수 추출 후 `env` 데이터와 병합
- [ ] 5분 뒤 시점의 정답 매핑(Shift) 및 다중 출력(Multi-Output) 베이스라인 모델 구축
