def get_landmark_coordinates(landmarks, index):
    # 특정 관절의 3D 좌표 추출
    landmark = landmarks.landmark[index]
    
    return (landmark.x, landmark.y, landmark.z)