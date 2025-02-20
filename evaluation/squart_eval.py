from data_extraction.extract_angles import calculate_angle
from data_extraction.extract_pose_data import get_landmark_coordinates

def evaluate_squart_pose(hip_angle, knee_x, foot_x):
    feedback = []

    if abs(knee_x - foot_x) > 5:
        feedback.append("무릎이 발끝을 넘었습니다.")
    if hip_angle < 70:
        feedback.append("허리가 너무 구부러졌습니다.")
    
    return feedback


def feedback_squart_pose(result):
    if result.pose_landmarks:
        # 어깨, 엉덩이, 무릎, 발 좌표 추출
        shoulder = get_landmark_coordinates(result.pose_landmarks, 11)
        hip = get_landmark_coordinates(result.pose_landmarks, 23)
        knee = get_landmark_coordinates(result.pose_landmarks, 25)
        foot = get_landmark_coordinates(result.pose_landmarks, 31)

        hip_angle = calculate_angle(shoulder, hip, knee)

        print(f"Knee_x: {knee[0]} Foot_x: {foot[0]}")
        print(f"Hip Angle: {hip_angle:.2f} degrees")

        feedback = evaluate_squart_pose(hip_angle, knee[0], foot[0])

        if len(feedback) == 0:
            feedback.append("올바른 자세입니다.")

        return feedback