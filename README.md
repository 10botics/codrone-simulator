# Codrone Simulator

## Introduction
This project is about the software providing virtual simulation for CoDrone. Using python API to control the drone.

## Features
- Multiple 3D scenes with CoDrone model and animation
- Simple to use Python API for drone controlling inside python drone simulator
- MiniMap, command and coordinate system help for understanding of the python codes
- Multiple obstacles for drone flight training
---
## Getting Started
Follow these steps to get started with the Drone Simulator:

> **IMPORTANT NOTE:** This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.

### Setup Instructions
- [Windows Setup](#windows-setup)
- [Mac Setup](#mac-setup)

## Windows Setup
### Pre-requisites Windows

Before using the simulator, make sure you have the following installed:

1. Python 3.11
   - [Python Windows Store Install Link](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=en-us&gl=HK&ocid=pdpshare)
   - Install using the Windows Store
   
   ![Python Store](https://github.com/user-attachments/assets/468f10a4-1159-400c-a489-90fc0612e00c)
   
   - Select View in Store
   
   ![Python Search](https://github.com/user-attachments/assets/ffd89487-ea79-4987-addd-01e29ffaced0)

2. Install JupyterLab
   - Open terminal/command prompt and run:
   ```bash
   pip install jupyterlab
   ```
   
   ![Jupyter Install](https://github.com/user-attachments/assets/cdef80a6-9abe-464d-aa7c-fdd0dd75b9c2)

3. Download Required Files
   - Download JupyterLab Files: [Download JupyterLab Files](https://github.com/10botics/codrone-simulator/blob/main/Drone%20Simulator.zip)
   ![image](https://github.com/user-attachments/assets/d7daf959-4b1a-4ae2-acfe-26e78641a49b)
   - Download the [Drone Simulator](https://github.com/10botics/codrone-simulator/releases/latest) ( DroneSimWin.zip )
   - Extract Drone Simulator.zip to Desktop
---
### Open JupyterLab
1. Open Drone Simulator Folder on the Desktop
2. Type CMD into the Address Bar
   ![image](https://github.com/user-attachments/assets/2fe6ddbe-7104-402b-a691-0ab9253e5d16)
3. Press Enter to Open Command Prompt
4. Type into the Command Prompt:
   ```bash
   jupyter lab
   ```
   ![image](https://github.com/user-attachments/assets/499c6661-c4eb-411f-8406-16fdcd1e580b)
5. Press Enter to Open JupyterLab
6. JupyterLab will open in your default web browser ( Image Below for refernce )
   ![image](https://github.com/user-attachments/assets/4fd82f05-199c-4012-8fc2-6df15a7990fe)



---
### Running Simulator
1. Open DroneSim Folder inside the Drone Simulator Folder
2. Run Drone.exe

![image](https://github.com/user-attachments/assets/3e4a8ec0-4c17-42ab-935a-66cef9b43cac)

3. Wait for the simulator to open
4. Allow Firewall Access

![image](https://github.com/user-attachments/assets/12fbed66-ff86-4b30-aa56-14cc0cf57293)

5. Select Free Play

![image](https://github.com/user-attachments/assets/bd0d8d5d-c9a6-4a6d-bc5e-2bcafe4b1b20)

---
### Test Hello World Python File to Move Drone
1. Open Drone Simulator Folder on the Desktop
2. Type CMD into the Address Bar
   ![image](https://github.com/user-attachments/assets/2fe6ddbe-7104-402b-a691-0ab9253e5d16)
3. Press Enter to Open Command Prompt
4. Start JupyterLab by running in terminal:
    ```bash
    jupyter lab
    ```
5. Open the HelloWorld.ipynb file in JupyterLab
![image](https://github.com/user-attachments/assets/298290ce-3d8f-4385-a632-09491740a3c1)
6. Make sure you see this window in the simulator
![image](https://github.com/user-attachments/assets/8973434f-f91e-4903-a16a-b88c335b4e62)

7. Follow the instructions in the notebook to move the drone in the simulator
---

## Mac Setup
### Prerequisites for Mac
1. Install Python 3.11
   - Click Here to Download [Python 3.11](https://www.python.org/downloads/release/python-3110/)
   - Scroll Down to "macOS 64-bit universal2 installer"
![image](https://github.com/user-attachments/assets/34c76213-a5bc-4bc3-88ea-0a1a0961e830)
   - Open the downloaded .pkg file
   - Follow the installation wizard:
     1. Click "Continue" through the Introduction
     2. Review and accept the license agreement
     3. Select the installation destination
     4. Click "Install" and enter your password if prompted
     5. Wait for installation to complete
     6. Click "Close" to finish
   - Verify installation by opening Terminal and running:
     ```bash
     python3 --version
     ```
  ![image](https://github.com/user-attachments/assets/25b7bfac-d31b-45e5-92a5-4a0c4fd92208)
   - Note: If Python is already installed, you'll see your current version number

2. Install JupyterLab
   - Open Terminal
   - Run the following command:
     ```bash
     pip3 install jupyterlab
     ```
     ![image](https://github.com/user-attachments/assets/4ad83ab1-0eae-404f-8388-5445d35c3b4c)

3. Download Required Files
   - Download JupyterLab Files: [Download JupyterLab Files](https://github.com/10botics/codrone-simulator/blob/main/Drone%20Simulator.zip)
   - Download the [Drone Simulator](https://github.com/10botics/codrone-simulator/releases/latest)
   - Create a folder on Desktop named "Drone_Simulator"
   - Extract JupyterLab files into the folder

### Opening JupyterLab
1. Open the Drone_Simulator folder on your Desktop
2. Right-click (or Control+click) inside the Drone_Simulator folder [ADD IMAGE]
3. Select "New Terminal at Folder" from the menu
   - If you don't see this option:
     1. Press Command + Space to open Spotlight Search
     2. Type "Terminal" and press Enter
     3. In Terminal, type:
        ```bash
        cd Desktop/Drone_Simulator
        ```
        [ADD IMAGE]
4. In the Terminal window, start JupyterLab:
   ```bash
   jupyter lab
   ```
   [ADD IMAGE]
5. Your default web browser will open with JupyterLab [ADD IMAGE]

### Running Simulator
1. Extract the Simulator
   - Locate the downloaded Drone Simulator zip file
   - Double click to extract the contents [ADD IMAGE]

2. Move to Applications
   - Drag the extracted Drone Simulator app to your Applications folder [ADD IMAGE]

3. Access Package Contents
   - Right-click (or Control+click) on the Drone Simulator app in Applications
   - Select "Show Package Contents"
   - Navigate to Contents/MacOS folder [ADD IMAGE]

4. Set Permissions
   - To open Terminal at the MacOS folder location:
     1. Right-click (or Control+click) in the MacOS folder
     2. Select "New Terminal at Folder"
   - Run:
     ```bash
     chmod +x Drone
     ```
     [ADD IMAGE]

5. Launch Simulator
   - In Terminal, run:
     ```bash
     ./Drone
     ```
   - The simulator window should open [ADD IMAGE]

6. Select Mode
   - Click the "Freeplay" button to enter freeplay mode
   ![image](https://github.com/user-attachments/assets/bd0d8d5d-c9a6-4a6d-bc5e-2bcafe4b1b20)

Note: After completing these steps, you can also launch the simulator directly from your Applications folder by double-clicking the Drone app.

### Hello World Example
A sample notebook with a basic drone program is provided in `hello_world.ipynb`.

1. Open JupyterLab as described above

2. Make sure the simulator window is open and in Freeplay mode
   - If not already open, launch the simulator following the steps above
   - Click "Freeplay" to enter freeplay mode
   ![image](https://github.com/user-attachments/assets/8973434f-f91e-4903-a16a-b88c335b4e62)

3. Open hello_world.ipynb
   - Click the file browser icon in the left sidebar
   - Navigate to and double-click hello_world.ipynb [ADD IMAGE]

4. Run the code
   - Follow along with the notebook instructions
   - Run each cell by clicking the "Run" button (play icon) or pressing Shift+Enter [ADD IMAGE]

5. Congratulations! You've run your first drone program



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
