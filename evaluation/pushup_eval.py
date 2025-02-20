from data_extraction.extract_angles import calculate_angle
from data_extraction.extract_pose_data import get_landmark_coordinates

# 자세 평가 함수
def evaluate_pushup_pose(elbow_angle, body_angle):
    feedback = []
    
    # 팔꿈치 각도 체크 (정상 범위 예시)
    if elbow_angle < 70 or elbow_angle > 160:
        feedback.append("팔꿈치를 더 굽히세요.")

    if body_angle < 150:
         feedback.append("잘못된 자세 - 허리가 너무 처졌습니다.")
    elif body_angle > 180:
        feedback.append("잘못된 자세 - 엉덩이가 너무 올라갔습니다.")
    
    return feedback

def feedback_pushup_pose(result):
    if result.pose_landmarks:
    # 어깨, 팔꿈치, 손목, 엉덩이, 무릎 좌표 추출
        shoulder = get_landmark_coordinates(result.pose_landmarks, 11)
        elbow = get_landmark_coordinates(result.pose_landmarks, 13)
        wrist = get_landmark_coordinates(result.pose_landmarks, 15)
        hip = get_landmark_coordinates(result.pose_landmarks, 23)
        knee = get_landmark_coordinates(result.pose_landmarks, 25)

        elbow_angle = calculate_angle(shoulder, elbow, wrist)
        body_angle = calculate_angle(shoulder, hip, knee)

        print(f"Elbow Angle: {elbow_angle:.2f} degrees")
        print(f"Body Angle: {body_angle:.2f} degrees")

        feedback = evaluate_pushup_pose(elbow_angle, body_angle)

        if len(feedback) == 0:
            feedback.append("올바른 자세입니다.")
            
    return feedback