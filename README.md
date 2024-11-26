# Codrone Simulator Unity Releases

## How to Open Drone Simulator
1. Unzip Zip file to desired location
2. Open folder
3. Run Unity.exe file
4. Allow Network Access Request

## After Successfully Opening Drone Simulator
Opened Drone Simulator should look like this:
![OpenUnityexe](https://github.com/user-attachments/assets/cd73b3ec-db4b-48d5-9738-2789b0dba9aa)

Download the python sample file in the link below to confirm the setup has been completed
[Download Latest Release](https://github.com/10botics/codrone-simulator-sdk-python)
---
## Introduction
This project is about the software providing virtual simulation on CoDrone. There are two types of simulation. The first one is directly controlling the drone with a controller. The second one is using python api to control the drone.

## Features
- Multiple 3D scenes with CoDrone model and animation
- Simple to use Python API for drone controlling inside python drone simulator
- MiniMap, command and coordinate system help for understanding of the python codes
- Multiple obstacles for drone flight training
- Obstacle editor for customizing the obstacles in the scene
---
## Python Drone Simulator
### Original Drone API Supported
Link to Original API: https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation
- pair()
- land() (Note: When the drone is grabbing an object, the land function will be ignored)
- takeoff()
- avoid_wall()
- detect_wall()
- hover()
- move()
- reset_move()
- set_pitch()
- set_roll()
- set_throttle()
- set_yaw()
- turn_left()
- turn_right()
- go()
- move_forward()
- move_backward()
- move_left()
- move_right()
- drone_LED_off()
- set_drone_LED()
- drone_buzzer()
- start_drone_buzzer()
- end_drone_buzzer()
- get_bottom_range()
- get_front_range()

## Custom Drone Simulator API
Link to Github Custom API Package: https://github.com/10botics/codrone-simulator-sdk-python

### Extra Drone API
- grab()
  - The drone will grab up an arbitrary grabbable object within the grab range of the drone. The current range of the drone is an 1.1m height capsule with 0.3m radius, with the upper spherical center of the capsule as the center of the drone. Note that only one arbitrary object will be grabbed if there are multiple grabbable object within range. Also, if the drone already grabbed an grabbable object, this command will be ignored.

- release()
    - The drone will release the grabbed object if the drone has grabbed one. The released object will be placed on the drone position with height equal zero(y = 0). If there is no grabbed object, this command will be ignored. Note that this command need to be run before running the land command as the drone with grabbed object will not be able to land.

- reset_position_and_rotation()
  - The drone will be teleported to the initial position and rotation. The initial position and rotation is the position and rotation of the drone when the drone simulator is opened. Note: This Command will not reset the Timer or the score. Only Reset the Drone Position)

- send_message(message):
  - The Drone will send out a message to the console. The message is the inputed string message. The message will be shown in the console of the drone simulator. Note that the message will be shown in the console of the drone simulator, not the python console.

### Extra API
- teleport_to(x, y, z)
  - The x, y and z formed the coordinate of the position that the drone will going to teleport. It is an y-up left-handed coordinate system. The drone will directly teleport to the inputed position drone after the execution of this line. Note that there are boundary set for the teleport range.

- teleport_by(x, y, z)
  - The x, y and z formed the offset translate vector that the drone will going to teleport toward. It is an y-up left-handed coordinate system. The drone will directly teleport toward with the inputed offset after the execution of the line. Note that there are boundary set for the teleport range.

- teleport_yaw_to(yaw)
  - The yaw is the rotation angle that the drone will rotate to. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degree. The forward direction(positive z-axis) yaw angle is 0. The drone will directly rotate toward with the input rotation after the execution of the line.

- teleport_yaw_by(yaw)
  - The yaw is the rotation angle offset that the drone will rotate toward. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degree. The drone will directly rotate toward the input offset angle with the input rotation after the execution of the line.

- set_restart_pos(x, z)
  - The x and z formed the coordinate of the position that the drone will be teleported to after next restart function is executed. Note that there are boundary set for the restart range.

- set_restart_yaw(yaw)
  - The yaw is the rotation angle that the drone will rotate to after next restart function is executed. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degree. The foward direction(positive z-axis) yaw angle is 0.
---
## Obstacle Editor
### Functions
- Translate Obstacle
- Rotate Obstacle
- Adjust the Height of Obstacle
- Delete Obstacle
- Snap Mode

### Inputs
- Rotate Camera (left mouse button + left alt)
- Pan Camera (middle mouse button + left alt)
- Zoom Camera (mouse scroll) or (right mouse button + left alt)
- Toggle Camera to Focus on Drone (F)
- Enter/Exit Editor Mode (Tab)
- Enter/Exit Delete Mode inside Editor Mode (X)
- Toggle Snap Mode inside Editor Mode (Shift + Tab)
- Toggle Grid for visualizing the position (G)
- Toggle the visibility of the drone properties panel and the Info panel (T)

### Running Guide Line
- Install "codrone-simulator" package through Windows CMD or MAC Terminal
- Turn on the Python drone simulator
- Run the code with the python environment in your computer (VS Code or PyCharm)
- Note: If you have a code written for the Real CoDrone API, change the import command:
    From codrone_edu.drone import Drone => From codrone_simulator import Drone
    From codrone_edu.protocol import Note => From codrone_simulator import Note
    (These maybe varies depending on the path from the python code directory to the codrone_simulator.py file's directory)

### Troubleshooting
- If the python code run but the drone is not moving, what should I do?
    1. Restart the drone simulator.
    2. Makes ure the python code run properly without any error.
    3. Make sure the drone current command inside the info panel is not null
- If the python code keep running and not going to end, what should I do?
    1. Check if there any code that is about sensors, those code maybe the reason of the problem.
    2. Restart the drone simulator.
    3. Make sure the Python API and the Drone Simulator is up to date.
- If the Python API cannot be detected, what should I do?
    1. Mak esure there is no typo in the import command
    2. Make sure the import path is correct (If you are directly downloading the source file)
    3. Make sure the pip install environment and the python environment installed are same as the running environment.
