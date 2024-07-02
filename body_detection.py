import cv2 as cv
import mediapipe as mp
import pyttsx3
import pygame
import time

# Initialize Mediapipe modules
mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils

# Initialize pose and face mesh models
pose = mpPose.Pose()
capture = cv.VideoCapture(0)

# Initialize speech engine
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

# Main loop for detecting pose and calculating height
while True:
    isTrue, img = capture.read()
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = pose.process(img_rgb)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            if id == 28:  # Adjust as needed for correct landmark point
                cx1, cy1 = int(lm.x * img.shape[1]), int(lm.y * img.shape[0])
                cv.circle(img, (cx1, cy1), 15, (0, 0, 0), cv.FILLED)
                # Assuming fixed distance for example, adjust as per your setup
                distance_cm = 100  # Example distance in cm
                speak(f"You are approximately {distance_cm} centimeters tall")
                speak("Measurement completed. You can relax now.")
                speak("Press 'q' to exit.")
                break

    img = cv.resize(img, (700, 500))
    cv.imshow("Task", img)
    
    # Exit condition
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
