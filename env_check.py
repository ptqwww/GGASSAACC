import pandas as pd

# 1. 파일 경로 설정
train_x_path = r"C:\Users\이가현\Downloads\online\online\online1\dataset\train\env\train_X.csv"
test_x_path = r"C:\Users\이가현\Downloads\online\online\online1\dataset\test\env\test_X.csv"

# 2. CSV 데이터 로드
print("환경 데이터를 읽어오는 중입니다...")
train_x = pd.read_csv(train_x_path)
test_x = pd.read_csv(test_x_path)
print("로드 완료!\n")

# ----------------------------------------------------
# [2단계] 데이터 양(레코드 수, 피처 수) 파악
# ----------------------------------------------------
print("="*60)
print("[2단계] 데이터 개수 및 변수 개수 (Shape) 확인")
print("="*60)
print(f"훈련 데이터 (train_X) 크기: {train_x.shape} -> 행(시간): {train_x.shape[0]}개, 열(변수): {train_x.shape[1]}개")
print(f"테스트 데이터 (test_X) 크기: {test_x.shape} -> 행(시간): {test_x.shape[0]}개, 열(변수): {test_x.shape[1]}개")
print("\n")

# ----------------------------------------------------
# [3단계] 피처 이해 (데이터 타입 및 결측치 총량 파악)
# ----------------------------------------------------
print("="*60)
print("[3단계] train_X 결측치(비어있는 값) 개수 검사")
print("="*60)
null_counts = train_x.isnull().sum()
# 결측치가 있는 변수만 골라서 출력합니다.
missing_features = null_counts[null_counts > 0]
if len(missing_features) == 0:
    print("🎉 축하합니다! train_X에는 결측치(NaN)가 단 하나도 없습니다.")
else:
    print("⚠️ 아래 변수들에서 결측치가 발견되었습니다. 전처리가 필요합니다:")
    print(missing_features)

print("\n" + "="*60)
print("데이터 상위 3개 행 미리보기 (어떻게 생겼나 맛보기)")
print("="*60)
# 첫 3줄을 출력하여 실제 컬럼명과 시간 데이터 형태를 눈으로 확인합니다.
print(train_x.head(3))