# Codrone Simulator

## Introduction
This project is about the software providing virtual simulation for CoDrone. Using python API to control the drone.

## Features
- Multiple 3D scenes with CoDrone model and animation
- Simple to use Python API for drone controlling inside python drone simulator
- MiniMap, command and coordinate system help for understanding of the python codes
- Multiple obstacles for drone flight training

## 📖 Setup Instructions
- [Windows setup](./Win_Setup.md)
- [Mac Setup](./Mac_Setup.md)

---
# install Drone Simulator

## ⚠️ **CRITICAL INSTALLATION NOTICE** ⚠️
==================================
> This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.

## Windows
1. Install the Drone Simulator through Windows Store:

    Codrone Simulator: [Windows Store](https://www.microsoft.com/store/apps/9P1Z3XZVZJZP)

![image](https://github.com/user-attachments/assets/337b67f1-9613-4aff-93aa-7f8812f28ae7)

2. Run Codrone Simulator

![image](https://github.com/user-attachments/assets/340df00d-1d46-417f-afb3-20e45320802e)

3. Allow Firewall Access

![image](https://github.com/user-attachments/assets/12fbed66-ff86-4b30-aa56-14cc0cf57293)

After Sucessfully Running the Simulator please follow the Guide below to setup the Jupyter Lab and start coding with the Simulator.

- [Windows setup](./Win_Setup.md)

## MacOS
Install the Drone Simulator through Mac App Store: Coming Soon

Codrone Simulator: [Mac App Store "Add Link"]() Coming Soon

Please follow the steps below for MacOS:
### Running Simulator

1. Extract the Simulator
  - Locate the downloaded DroneSimMac.zip file
  - Double click to extract the contents

  <img width="117" alt="Screenshot 2024-12-20 at 11 56 41 AM" src="https://github.com/user-attachments/assets/7e81133a-0a41-49c9-8456-dbb04d9c6bde" />

2. Install to Applications
  - Drag the extracted DroneSimMac app to your Applications folder

  <img width="553" alt="Screenshot 2024-12-20 at 11 58 25 AM" src="https://github.com/user-attachments/assets/4b3a9bce-8947-4176-b1e0-8aebe535d91a" />

3. Configure App Permissions
  - Right-click (or Control+click) on DroneSimMac in Applications
  - Select "Show Package Contents"

  <img width="392" alt="Screenshot 2024-12-20 at 11 59 25 AM" src="https://github.com/user-attachments/assets/858a36e3-4355-4126-8c96-029b7c215d1c" />

  - Navigate to Contents/MacOS folder

  <img width="275" alt="Screenshot 2024-12-20 at 12 00 48 PM" src="https://github.com/user-attachments/assets/f18ea8a6-a870-4b34-9928-bf28bede89b1" />

  - Right-click (or Control+click) in the MacOS folder and select "New Terminal at Folder"

  <img width="363" alt="Screenshot 2024-12-20 at 12 01 45 PM" src="https://github.com/user-attachments/assets/eab5cfd7-765c-4ced-bf3f-80666bbf9f38" />

  - In Terminal, run:
    ```bash
    bash
    ```
    Then run:
    ```bash
    chmod +x Drone
    ```

   <img width="387" alt="Screenshot 2024-12-20 at 1 35 56 PM" src="https://github.com/user-attachments/assets/a9e9380a-ef9f-4762-85cf-28a82ca2fb02" />
   <img width="489" alt="Screenshot 2024-12-20 at 1 32 47 PM" src="https://github.com/user-attachments/assets/30a7eb89-4864-48cb-b165-96cb03968def" />

4. Launch the Simulator
  - In the same Terminal window, run:
    ```bash
    ./Drone
    ```

   <img width="504" alt="Screenshot 2024-12-20 at 1 33 18 PM" src="https://github.com/user-attachments/assets/03d9e698-e98d-49c4-9db1-eec481139670" />

   If you see a "cannot open" error:

   <img width="317" alt="Screenshot 2024-12-20 at 1 42 09 PM" src="https://github.com/user-attachments/assets/b9982b8d-5080-42fa-b47a-9f74367e8e5b" />

   Follow these steps:
  1. Close the Terminal window
  2. Open a new Terminal window from Applications

     <img width="452" alt="Screenshot 2024-12-20 at 3 11 36 PM" src="https://github.com/user-attachments/assets/d15a9601-dd33-4d0d-ab07-3ee1f9d8c8aa" />

  3. Run this command:
     ```bash
     xattr -r -d com.apple.quarantine /Applications/DroneSimMac.app
     ```

   <img width="666" alt="Screenshot 2024-12-20 at 3 13 21 PM" src="https://github.com/user-attachments/assets/cfa63515-a220-4679-849a-90d3552c6f25" />

   The simulator window should now open when you double click the DroneSimMac app in Applications

   <img width="945" alt="Screenshot 2024-12-20 at 12 10 25 PM" src="https://github.com/user-attachments/assets/463fee58-eaa8-4f9a-845c-2bc9557307d1" />

5. Select Freeplay Mode
  - Click the "Freeplay" button to begin

  ![image](https://github.com/user-attachments/assets/bd0d8d5d-c9a6-4a6d-bc5e-2bcafe4b1b20)

After Sucessfully Running the Simulator please follow the Guide below to setup the Jupyter Lab and start coding with the Simulator.

- [Mac Setup](./Mac_Setup.md)

---

## Python Drone Simulator

### Obstacle Editor
- Link to Obstacle Editor README: [Obstacle Editor README](https://github.com/10botics/codrone-simulator/blob/main/ObstacleEditorREADME.md)

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
