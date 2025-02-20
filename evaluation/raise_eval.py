from data_extraction.extract_angles import calculate_angle
from data_extraction.extract_pose_data import get_landmark_coordinates

# 자세 평가 함수
def evaluate_raise_up_pose(right_arm_angle, left_arm_angle):
    feedback = []
    if right_arm_angle < 80 and left_arm_angle < 80:
        feedback.append("양쪽 팔이 너무 낮습니다.")
    elif right_arm_angle > 120 and left_arm_angle > 120:
        feedback.append("양쪽 팔이 너무 높습니다.")

    elif right_arm_angle < 80 and left_arm_angle > 120:
        feedback.append("오른쪽 팔이 너무 낮고 왼쪽 팔이 너무 높습니다.")
    elif right_arm_angle > 120 and left_arm_angle < 80:
        feedback.append("오른쪽 팔이 너무 높고 왼쪽 팔이 너무 낮습니다.")

    elif right_arm_angle > 120:
        feedback.append("오른쪽 팔이 너무 높습니다.")
    elif right_arm_angle < 80:
        feedback.append("오른쪽 팔이 너무 낮습니다.")

    elif left_arm_angle < 80:
        feedback.append("왼쪽 팔이 너무 낮습니다.")
    elif left_arm_angle > 120:
        feedback.append("왼쪽 팔이 너무 높습니다.")
    
    return feedback

def feedback_raise_pose(result):
    if result.pose_landmarks:
    # 어깨, 손목, 엉덩이 좌표 추출
        left_shoulder = get_landmark_coordinates(result.pose_landmarks, 11)
        left_wrist = get_landmark_coordinates(result.pose_landmarks, 15)
        left_hip = get_landmark_coordinates(result.pose_landmarks, 23)

        right_shoulder = get_landmark_coordinates(result.pose_landmarks, 12)
        right_wrist = get_landmark_coordinates(result.pose_landmarks, 16)
        right_hip = get_landmark_coordinates(result.pose_landmarks, 24)

        left_arm_angle = calculate_angle(left_wrist, left_shoulder, left_hip)
        right_arm_angle = calculate_angle(right_wrist, right_shoulder, right_hip)

        print(f"Left arm Angle: {left_arm_angle:.2f} degrees")
        print(f"Right arm Angle: {right_arm_angle:.2f} degrees")

        feedback = evaluate_raise_up_pose(right_arm_angle, left_arm_angle)

        if len(feedback) == 0:
            feedback.append("올바른 자세입니다.")
            
    return feedback