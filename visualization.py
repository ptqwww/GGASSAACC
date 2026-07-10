import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 로드 및 시간 피처 엔지니어링
train_x_path = r"C:\Users\이가현\Downloads\online\online\online1\dataset\train\env\train_X.csv"
df = pd.read_csv(train_x_path)

# 시간 분리 (시각화용)
sample_time = df['time'].str.split(' ')
df['day'] = sample_time.str[0].str.replace('DAT', '').astype(int)
df['hour'] = sample_time.str[1].str.split(':').str[0].astype(int)

# 2. 그래프 스타일 설정
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'Malgun Gothic' # Windows 한글 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False    # 마이너스 부호 깨짐 방지

# ============================================================
# [시각화 1] 수치형 데이터 시각화 : 내부 온도 분포 (Histogram & Boxplot)
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('내부 온도(temperature) 분포 및 이상치 확인', fontsize=16)

sns.histplot(data=df, x='temperature', kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('온도 히스토그램 (Distribution)')

sns.boxplot(data=df, x='temperature', ax=axes[1], color='lightpink')
axes[1].set_title('온도 상자 그림 (Box Plot)')

plt.tight_layout()
plt.show()

# ============================================================
# [시각화 2] 범주형(이진형) 데이터 시각화 : FCU 팬 가동 빈도 (Count Plot)
# ============================================================
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='fcu_fan', palette='Set2')
plt.title('FCU 팬(fcu_fan) 가동 빈도 확인')
plt.xlabel('가동 상태 (0: 꺼짐, 201: 켜짐)')
plt.ylabel('데이터 개수(분)')
plt.show()

# ============================================================
# [시각화 3] 데이터 관계 시각화 1 : 시간(Hour)에 따른 내부 온도 변화 (Line Plot)
# ============================================================
plt.figure(figsize=(10, 5))
# 주간/야간 패턴이 뚜렷하게 보이는지 확인합니다.
sns.lineplot(data=df, x='hour', y='temperature', ci=None, marker='o', color='red')
plt.title('하루 시간대별 평균 내부 온도 변화 추이')
plt.xlabel('시간 (Hour)')
plt.ylabel('평균 온도 (℃)')
plt.xticks(range(0, 24))
plt.show()

# ============================================================
# [시각화 4] 데이터 관계 시각화 2 : 주요 환경 변수 간 상관관계 (Heatmap)
# ============================================================
plt.figure(figsize=(10, 8))
# 모든 변수를 다 넣으면 너무 복잡하므로 주요 변수 몇 개만 골라서 봅니다.
selected_cols = ['temperature_outside', 'humidity_outside', 'solar_radiation', 'temperature', 'humidity', 'co2', 'hour']
corr_matrix = df[selected_cols].corr()

# 상관관계 히트맵 그리기
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f", linewidths=.5)
plt.title('주요 환경 변수 간 상관관계 히트맵 (Correlation Heatmap)')
plt.tight_layout()
plt.show()