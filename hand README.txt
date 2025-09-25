Project Title:
Hand Gesture Virtual Mouse Control using Webcam
________________________________________
What this project does:
1.	 Uses your webcam to detect hand gestures in real-time
2.	 Uses Media Pipe to detect hands and fingers
3.	 Controls your mouse cursor with your index finger
4.	 Supports left click, right click, scroll up, scroll down
5.	 Detects how many fingers are up to perform actions
6.	 Closes when you press Q
________________________________________
Technologies Used:
•	OpenCV – To capture webcam video
•	Media Pipe – For real-time hand tracking
•	Py Auto GUI – To control mouse and perform clicks/scroll
________________________________________
 Gesture Control List:
Fingers Shown	 Action
5 fingers	Scroll down
4 fingers	Scroll up
3 fingers	Right click
2 fingers	Left click
1 finger (index)	Move curser
________________________________________
 Required Python Libraries:
Install the required packages using pip:
pip install open cv-python media pipe py auto gui
How to Run the Project:
1.	Save the script as hand_mouse.py
2.	Open Terminal or Command Prompt in the folder
3.	Run the script:
python hand_mouse.py
4.	A webcam window will open.
5.	Show your hand to control the mouse!

How it Works (in simple words):
•	Your webcam sees your hand
•	Media Pipe finds your fingertips
•	Based on how many fingers are up:
o	It clicks, moves mouse, or scrolls
•	It only follows one hand and locks onto it
•	Very small movements control the mouse
________________________________________
 How to Stop the App:
•	Press Q on your keyboard
•	Or close the webcam window
________________________________________
Educational Use:
This project is useful for:
•	Touchless interfaces
•	AI & ML learning
•	Beginners learning computer vision
•	BTech mini/final year project
