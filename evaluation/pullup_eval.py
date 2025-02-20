# 자세 평가 함수
from data_extraction.extract_angles import calculate_angle
from data_extraction.extract_pose_data import get_landmark_coordinates


def evaluate_pullup_pose(body_angle, hand, mouth):
    feedback = []

    if body_angle > 50 and body_angle < 130:
      feedback.append("몸이 기울져있습니다.")

    if hand < mouth:
      feedback.append("턱이 바보다 낮습니다.")

    return feedback

def feedback_pullup_pose(result):
    if result.pose_landmarks:
        # 어깨, 팔꿈치, 손목, 엉덩이, 무릎 좌표 추출
        shoulder = get_landmark_coordinates(result.pose_landmarks, 11)
        hip = get_landmark_coordinates(result.pose_landmarks, 23)
        knee = get_landmark_coordinates(result.pose_landmarks, 25)
        hand = get_landmark_coordinates(result.pose_landmarks, 15)
        mouth = get_landmark_coordinates(result.pose_landmarks, 10)

        hand_y = hand[1]
        mouth_y = mouth[1]

        body_angle = calculate_angle(shoulder, hip, knee)

        print(f"Hand: {hand} Mouth_y: {mouth}")
        print(f"Body Angle: {body_angle:.2f} degrees")

        feedback = evaluate_pullup_pose(body_angle, hand, mouth)

        if len(feedback) == 0:
            feedback.append("올바른 자세입니다.")
            
    return feedback
