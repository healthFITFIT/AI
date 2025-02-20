import numpy as np

def calculate_angle(a, b, c):
    # a, b, c는 각 관절의 3D 좌표 (x, y, z)
    ba = np.array(a) - np.array(b)
    bc = np.array(c) - np.array(b)
    
    # 벡터 간 각도 계산
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))  # -1 ~ 1 범위로 조정
    
    return np.degrees(angle) 