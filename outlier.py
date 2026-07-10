import pandas as pd
import numpy as np

# 1. 데이터 로드
train_x_path = r"C:\Users\이가현\Downloads\online\online\online1\dataset\train\env\train_X.csv"
train_x = pd.read_csv(train_x_path)

print("="*60)
print("[분석 1] 각 변수별 기본 통계치 확인 (이상치 감지용)")
print("="*60)
# describe()는 최솟값(min), 최댓값(max)을 보여주어 말도 안 되는 수치가 있는지 파악하게 해줍니다.
print(train_x.describe().T[['min', 'max', 'mean']])

print("\n" + "="*60)
print("[분석 2] 변수들의 고윳값(Unique Value) 개수 파악")
print("="*60)
# 고윳값이 1개라는 것은 데이터가 처음부터 끝까지 변하지 않았다는 뜻이므로 제거 후보가 됩니다.
for col in train_x.columns:
    if col != 'time':
        print(f"{col}: 고윳값 개수 = {train_x[col].nunique()}개")

print("\n" + "="*60)
print("[분석 3] 시간 피처 엔지니어링 예시 테스트")
print("="*60)
# time 열에서 날짜(DAT)와 시간 분리 시뮬레이션
# 예: "DAT109 00:02" -> 날짜=109, 시=0, 분=2
sample_time = train_x['time'].str.split(' ')
train_x['day'] = sample_time.str[0].str.replace('DAT', '').astype(int)
train_x['hour'] = sample_time.str[1].str.split(':').str[0].astype(int)
train_x['minute'] = sample_time.str[1].str.split(':').str[1].astype(int)

print(train_x[['time', 'day', 'hour', 'minute']].head(3))
print("\n👉 시간 축 숫자로 분리 성공!")