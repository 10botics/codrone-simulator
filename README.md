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
   ![image](https://github.com/user-attachments/assets/d7daf959-4b1a-4ae2-acfe-26e78641a49b)
   - Download the [Drone Simulator](https://github.com/10botics/codrone-simulator/releases/latest) ( DroneSimMac.zip )
   - Extract Drone Simulator.zip to Desktop

### Opening JupyterLab
1. Open the Drone Simulator folder on your Desktop
2. Right-click (or Control+click) inside the Drone_Simulator folder <img width="379" alt="Screenshot 2024-12-20 at 11 27 45 AM" src="https://github.com/user-attachments/assets/f156d5b3-ef84-4100-9893-09974779b6e9" />

3. Select "New Terminal at Folder" from the menu
   - If you don't see this option:
     1. Press Command + Space to open Spotlight Search
     2. Type "Terminal" and press Enter
     3. In Terminal, type:
        ```bash
        cd Desktop/Drone_Simulator
        ```
4. In the Terminal window, start JupyterLab:
   ```bash
   jupyter lab
   ```
   <img width="387" alt="Screenshot 2024-12-20 at 12 14 44 PM" src="https://github.com/user-attachments/assets/055cc140-64a2-4410-87fd-ebd9a9f1c365" />

5. Your default web browser will open with JupyterLab 
<img width="850" alt="Screenshot 2024-12-20 at 11 55 27 AM" src="https://github.com/user-attachments/assets/5abe350b-6818-4364-bcf3-f59e0beb667a" />


### Running Simulator
1. Extract the Simulator
   - Locate the downloaded Drone Simulator zip file
   - Double click to extract the contents
   
      <img width="117" alt="Screenshot 2024-12-20 at 11 56 41 AM" src="https://github.com/user-attachments/assets/7e81133a-0a41-49c9-8456-dbb04d9c6bde" />


2. Move to Applications
   - Drag the extracted Drone Simulator app to your Applications folder
   <img width="553" alt="Screenshot 2024-12-20 at 11 58 25 AM" src="https://github.com/user-attachments/assets/4b3a9bce-8947-4176-b1e0-8aebe535d91a" />


3. Access Package Contents
   - Right-click (or Control+click) on the Drone Simulator app in Applications
   - Select "Show Package Contents"
   <img width="392" alt="Screenshot 2024-12-20 at 11 59 25 AM" src="https://github.com/user-attachments/assets/858a36e3-4355-4126-8c96-029b7c215d1c" />

   - Navigate to Contents/MacOS folder
   <img width="275" alt="Screenshot 2024-12-20 at 12 00 48 PM" src="https://github.com/user-attachments/assets/f18ea8a6-a870-4b34-9928-bf28bede89b1" />


4. Set Permissions
   - To open Terminal at the MacOS folder location:
     1. Right-click (or Control+click) in the MacOS folder
     2. Select "New Terminal at Folder"
     <img width="363" alt="Screenshot 2024-12-20 at 12 01 45 PM" src="https://github.com/user-attachments/assets/eab5cfd7-765c-4ced-bf3f-80666bbf9f38" />

   - Switch to bash shell:
     ```bash
     bash
     ```
     <img width="387" alt="Screenshot 2024-12-20 at 1 35 56 PM" src="https://github.com/user-attachments/assets/a9e9380a-ef9f-4762-85cf-28a82ca2fb02" />

   - Run:
     ```bash
     chmod +x Drone
     ```
     <img width="489" alt="Screenshot 2024-12-20 at 1 32 47 PM" src="https://github.com/user-attachments/assets/30a7eb89-4864-48cb-b165-96cb03968def" />


5. Launch Simulator
   - In Terminal, run:
     ```bash
     ./Drone
     ```
     <img width="504" alt="Screenshot 2024-12-20 at 1 33 18 PM" src="https://github.com/user-attachments/assets/03d9e698-e98d-49c4-9db1-eec481139670" />

   - If you see an error saying "cannot open", follow these steps:
   <img width="317" alt="Screenshot 2024-12-20 at 1 42 09 PM" src="https://github.com/user-attachments/assets/b9982b8d-5080-42fa-b47a-9f74367e8e5b" />
     1. Close the Terminal window
     2. Go to your Applications folder
     3. Open a new Terminal window
     <img width="452" alt="Screenshot 2024-12-20 at 3 11 36 PM" src="https://github.com/user-attachments/assets/d15a9601-dd33-4d0d-ab07-3ee1f9d8c8aa" />


     4. Enter the following command:
        ```bash
        xattr -r -d com.apple.quarantine /Applications/DroneSimMac.app
        ```
        <img width="666" alt="Screenshot 2024-12-20 at 3 13 21 PM" src="https://github.com/user-attachments/assets/cfa63515-a220-4679-849a-90d3552c6f25" />


   - The simulator window should open 
   <img width="945" alt="Screenshot 2024-12-20 at 12 10 25 PM" src="https://github.com/user-attachments/assets/463fee58-eaa8-4f9a-845c-2bc9557307d1" />

   
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
   - Navigate to and double-click hello_world.ipynb 
   <img width="879" alt="Screenshot 2024-12-20 at 12 11 20 PM" src="https://github.com/user-attachments/assets/fa298a3b-a5c5-44c8-b732-72681488977e" />


4. Run the code
   - Follow along with the notebook instructions
   - Run each cell by clicking the "Run" button (play icon) or pressing Shift+Enter

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
