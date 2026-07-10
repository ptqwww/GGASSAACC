import numpy as np
import matplotlib.pyplot as plt

# 1. 파일 경로 설정 (가현 님 PC의 실제 .raw 데이터 경로)
raw_path = r"C:\Users\이가현\Downloads\online\online\online1\dataset\train\ms\DAT131\1_DAT131_132028\cube.raw"
# 경로만 바꾸면 다른 .raw 파일도 동일한 방식으로 로드 및 시각화 가능

try:
    print("=== [데이터 둘러보기] 다분광 영상 메타데이터 로드 ===")
    
    # cube.hdr에 적혀있는 실제 규격 데이터 반영
    samples = 1280      # 가로 (Width)
    lines = 1024        # 세로 (Height)
    bands = 10          # 밴드 개수 (채널 수)
    data_type = np.uint16  # 데이터 타입 12 = Unsigned 16-bit int
    
    # 2. .raw 바이너리 파일 읽기
    print("바이너리 파일을 직접 로드 중...")
    data_flattened = np.fromfile(raw_path, dtype=data_type)
    print(f"로드된 전체 1차원 데이터 크기: {data_flattened.shape}")
    
    # 3. [데이터 양 파악] BSQ 방식에 맞춰 3차원으로 형상 변환 (Reshape)
    # interleave = bsq는 (Bands, Lines, Samples) 순서로 데이터가 일렬로 서있음을 의미합니다.
    data_cube_bsq = data_flattened.reshape((bands, lines, samples))
    
    # 이미지 시각화와 이미지 처리를 위해 표준 형태인 (Lines, Samples, Bands) 구조로 축을 변경해줍니다.
    data_cube = data_cube_bsq.transpose(1, 2, 0)
    
    print("\n" + "="*50)
    print("=== [결과] 다분광 데이터 구조 파악 완료 ===")
    print("="*50)
    print(f"최종 HyperSpectral Cube Shape: {data_cube.shape} -> (세로, 가로, 밴드수)")
    print(f"세로 해상도(Lines) : {data_cube.shape[0]} 픽셀")
    print(f"가로 해상도(Samples) : {data_cube.shape[1]} 픽셀")
    print(f"파장 대역 수(Bands) : {data_cube.shape[2]} 개 대역 (713nm ~ 920nm)")
    
    # 4. [피처 이해 & 시각화] 0번째 밴드 (713nm) 시각화 수행
    print("\n첫 번째 밴드(713nm) 이미지를 화면에 띄웁니다...")
    
    plt.figure(figsize=(12, 9))
    # 0번 밴드의 2차원 평면 이미지를 시각화합니다.
    plt.imshow(data_cube[:, :, 0], cmap='jet')
    
    # 부가 정보 레이블 추가
    plt.title("Visualization: Band 0 (713nm)", fontsize=14)
    plt.colorbar(label='Pixel Intensity (Reflection)')
    plt.xlabel('Samples (Width)')
    plt.ylabel('Lines (Height)')
    
    # 그래프 창 띄우기
    plt.show()
    print("\n성공적으로 데이터 시각화를 마쳤습니다!")

except FileNotFoundError:
    print(f"에러: '{raw_path}' 파일을 찾을 수 없습니다. 경로를 다시 확인해주세요.")
except Exception as e:
    print(f"오류 발생: {e}")