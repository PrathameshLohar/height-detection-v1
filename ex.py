import cv2 as cv
import pyttsx3
import subprocess

# Initialize face detector
face_detector = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize speech engine
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()

# Function to calculate focal length
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length

# Function to calculate distance
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length) / face_width_in_frame
    return distance

# Constants for calibration
Known_distance = 100.0  # Example: distance from camera to object in cm
Known_width = 14.3  # Example: width of face in the real world in cm

# Reading reference image for calibration
ref_image = cv.imread("ref_img.jpg")

# Function to detect face width in pixels
def face_data(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    face_width = 0
    for (x, y, h, w) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_width = w
    return face_width

# Finding face width in reference image
ref_image_face_width = face_data(ref_image)

# Calculating focal length based on known distance and width
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, ref_image_face_width)

# Initialize camera
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_width_in_frame = face_data(frame)

    # if face_width_in_frame != 0:
    #     Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)
    #     cv.line(frame, (30, 30), (230, 30), (0, 0, 255), 32)
    #     cv.line(frame, (30, 30), (230, 30), (0, 0, 0), 28)
    #     Distance = round(Distance, 2)
        
    #     if Distance in range(230, 260):
    #         speak("Please stand still for measurement.")
    #         # Launching body_detection.py using subprocess
    #         subprocess.Popen(['python', 'body_detection.py'])
    #         break
    #     elif Distance < 230:
    #         speak("Please step back.")
    #     else:
    #         speak("Please come a little closer.")

    #     cv.putText(frame, f"Distance: {Distance} cm", (30, 35), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if face_width_in_frame != 0:
        Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)
        cv.line(frame, (30, 30), (230, 30), (0, 0, 255), 32)
        cv.line(frame, (30, 30), (230, 30), (0, 0, 0), 28)
        Distance = round(Distance, 2)
        
        # Change the range check to 100 cm to 150 cm
        if Distance in range(140, 151):
            speak("Please stand still for measurement.")
            # Launching body_detection.py using subprocess
            subprocess.Popen(['python', 'body_detection.py'])
            break
        elif Distance < 140:
            speak("Please step back.")
        else:
            speak("Please come a little closer.")

        cv.putText(frame, f"Distance: {Distance} cm", (30, 35), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)



    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
