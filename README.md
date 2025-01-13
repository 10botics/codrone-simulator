# Codrone Simulator

![image](https://github.com/user-attachments/assets/3a7d0107-2747-41c6-9f2b-0d075df50f97)

<p align="center">
  <a href="https://apps.microsoft.com/detail/9P03665Z63QG?hl=en-us&gl=HK&ocid=pdpshare">
    <img src="https://github.com/user-attachments/assets/41758171-68b8-49c5-81cb-68fe62ba5bd0" alt="Get it from Microsoft Store" width="200"/>
  </a>
  <a href="https://apps.apple.com/hk/app/codrone-simulator/id6739762056?mt=12">
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

Windows
  ```bash
  pip install codrone_simulator
  ```
MacOS
  ```bash
  pip3 install codrone_simulator
  ```
## Install Drone Simulator


  - [Drone Simulator Windows Installation Guide](./docs/DroneSim_Win_Install.md)

  - [Drone Simulator MacOS Installation Guide](./docs/DroneSim_Mac_Install.md)


## JupyterLab
JupyterLab is an interactive development environment that allows you to create and run Python code in notebook format. For the Codrone Simulator.

  - [JupyterLab Windows Installation Guide](./docs/Jupyterlab_Win_Install.md)

  - [JupyterLab MacOS Installation Guide](./docs/Jupyterlab_Mac_Install.md)

## Hello World
Create your first drone program with the Hello World example.

  - [Hello World Jupyterlab Guide](./docs/HelloWorld_Jupy.md)


## Obstacle Editor Feature 
- Link to Obstacle Editor README: [Obstacle Editor README](./docs/ObstacleEditorREADME.md)

## Original and Custom Drone API 
  Link to Original and Custom API: [Original and Custom Drone API](./docs/Drone_Original_Custom_API.md)


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
