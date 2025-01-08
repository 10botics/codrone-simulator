# Codrone Simulator

![image](https://github.com/user-attachments/assets/3a7d0107-2747-41c6-9f2b-0d075df50f97)

<p align="center">
  <a href="https://apps.microsoft.com/detail/9P03665Z63QG?hl=en-us&gl=HK&ocid=pdpshare">
    <img src="https://github.com/user-attachments/assets/41758171-68b8-49c5-81cb-68fe62ba5bd0" alt="Get it from Microsoft Store" width="200"/>
  </a>
  <a href="https://apps.apple.com/">
    <img src="https://github.com/user-attachments/assets/2a9a2327-014c-4e10-ba5f-9eee8c258ce2" alt="Download on the Mac App Store" width="285"/>
  </a>
</p>



## Introduction
This project is about the software providing virtual simulation for CoDrone. Using python API to control the drone.

## Features
- Multiple 3D scenes with CoDrone model and animation
- Simple to use Python API for drone controlling inside python drone simulator
- MiniMap, command and coordinate system help for understanding of the python codes
- Multiple obstacles for drone flight training

## Prerequisites
### Python
- Python 3.11 required to run the Drone Commands
  - [Python Windows Install Guide](./docs/Python_Win_Install.md)
  - [Python MacOS Install Guide](./docs/Python_Mac_Install.md)

### SDK
- This SDK Contains the Drone Simulator API to control the Drone
  ```bash
  pip install codrone_simulator
  ```

## Install Drone Simulator


  - [Drone Simulator Windows Install Guide](./docs/DroneSim_Win_Install.md)

  - [Drone Simulator MacOS Install Guide](./docs/DroneSim_Mac_Install.md)


## JupyterLab
JupyterLab is an interactive development environment that allows you to create and run Python code in notebook format. For the Codrone Simulator.

  - [JupyterLab Windows Install Guide](./docs/Jupyterlab_Win_Install.md)

  - [JupyterLab MacOS Install Guide](./docs/Jupyterlab_Mac_Install.md)


## Hello World
Create your first drone program with the Hello World example.

Follow Instrcutions to control the Drone
  - [Hello World Jupyterlab Guide](./docs/HelloWorld_Jupy.md)

## Python Drone Simulator

### Obstacle Editor
- Link to Obstacle Editor README: [Obstacle Editor README](./docs/ObstacleEditorREADME.md)

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

### Custom Drone Simulator API
Link to Github Custom API Package: https://github.com/10botics/codrone-simulator-sdk-python

### Extra Drone API
- grab()
  - The drone will grab up an arbitrary grabbable object within the grab range of the drone. The current range of the drone is a 1.1m height capsule with 0.3m radius, with the upper spherical center of the capsule as the center of the drone. Note: that only one arbitrary object will be grabbed if there are multiple grabbable objects within range. Also, if the drone already grabbed a grabbable object, this command will be ignored.

- release()
  - The drone will release the grabbed object if the drone has grabbed one. The released object will be placed on the drone position with height equal zero(y = 0). If there is no grabbed object, this command will be ignored. Note: that this command needs to be run before running the land command as the drone with grabbed object will not be able to land.

- reset_position_and_rotation()
  - The drone will be teleported to the initial position and rotation. The initial position and rotation is the position and rotation of the drone when the drone simulator is opened. Note: This Command will not reset the Timer or the score. Only Reset the Drone Position)

- send_message(message):
  - The Drone will send out a message to the console. The message is the inputted string message. The message will only be shown in the console of the drone simulator, not the python console.

### Extra API
- teleport_to(x, y, z)
  - The x, y and z form the coordinate of the position that the drone will teleport to. It is a y-up left-handed coordinate system. The drone will directly teleport to the inputted position drone after the execution of this line. Note: that there are boundaries set for the teleport range.

- teleport_by(x, y, z)
  - The x, y, and z form the offset translation vector that the drone will move towards. It uses a y-up left-handed coordinate system. The drone will directly teleport by the specified offset after executing this command. Note that there are boundaries set for the teleport range.

- teleport_yaw_to(yaw)
  - The yaw is the rotation angle that the drone will rotate to. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The forward direction(positive z-axis) yaw angle is 0. The drone will directly rotate toward with the input rotation after the execution of the line.

- teleport_yaw_by(yaw)
  - The yaw is the rotation angle offset that the drone will rotate toward. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The drone will directly rotate toward the input offset angle with the input rotation after the execution of the line.

- set_restart_pos(x, z)
  - The x and z form the coordinate of the position that the drone will be teleported to after next restart function is executed. Note that there are boundaries set for the restart range.

- set_restart_yaw(yaw)
  - The yaw is the rotation angle that the drone will rotate to after next restart function is executed. Positive yaw value is clockwise rotation while negative yaw value is anti-clockwise rotation. The unit of the yaw value is in degrees. The forward direction(positive z-axis) yaw angle is 0.
---

## Inputs
- Rotate Camera (left mouse button + left alt)
- Pan Camera (middle mouse button + left alt)
- Zoom Camera (mouse scroll) or (right mouse button + left alt)
- Toggle Camera to Focus on Drone (F)
- Toggle Grid for visualizing the position (G)

### Running Guide Line
- Install "codrone-simulator" package through Windows CMD or MAC Terminal
- Turn on the Python drone simulator
- Enter a Competition Scene or Free Play Scene
- Open JupyterLab and create a new Python notebook
- Run your code cells in the Jupyter notebook
- Note: If you have code written for the Real CoDrone API, change the import command:
    From codrone_edu.drone import Drone => From codrone_simulator import Drone
    From codrone_edu.protocol import Note => From codrone_simulator import Note

### Troubleshooting
- If the python code is running but the drone is not moving, what should I do?
    1. Restart the drone simulator.
    2. Make sure the python code runs properly without any error.
    3. Make sure the drone current command inside the info panel is not null
- If the python code keeps running and not going to end, what should I do?
    1. Check if there are any code related to sensors, those code may be the reason for the problem.
    2. Restart the drone simulator.
    3. Make sure the Python API and the Drone Simulator are up to date.
- If the Python API cannot be detected, what should I do?
    1. Make sure there is no typo in the import command
    2. Make sure the import path is correct (If you are directly downloading the source file)
    3. Make sure the pip install environment and the python environment installed are the same as the running environment.
- If JupyterLab cannot connect to the simulator:
    1. Make sure the simulator is running before executing code cells
    2. Restart the Jupyter kernel
    3. Verify that codrone-simulator package is installed in the same Python environment as JupyterLab
