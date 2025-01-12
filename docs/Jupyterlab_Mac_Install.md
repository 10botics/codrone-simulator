# MacOS Setup

## ⚠️ **CRITICAL INSTALLATION NOTICE** ⚠️
This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.

## MacOS Jupyter Lab Setup

1. Install JupyterLab
   - Open Terminal
   - Run the following command:
     ```bash
     pip3 install jupyterlab
     ```
     ![image](https://github.com/user-attachments/assets/4ad83ab1-0eae-404f-8388-5445d35c3b4c)

2. Download Required Files
   - Download JupyterLab Files: [Download JupyterLab Files](https://raw.githubusercontent.com/10botics/codrone-simulator/refs/heads/main/Drone%20Simulator.zip)
   - Extract Drone Simulator.zip to Desktop

   ![MacVideosssss1](https://github.com/user-attachments/assets/10533ec1-f6bf-4f2b-a7b9-65119bb47dbe)



### Opening JupyterLab
1. Find the Drone Simulator folder on your Desktop

2. Right-click (or Control+click) inside the Drone_Simulator folder

   <img width="379" alt="Screenshot 2024-12-20 at 11 27 45 AM" src="https://github.com/user-attachments/assets/f156d5b3-ef84-4100-9893-09974779b6e9" />

4. Select "New Terminal at Folder" from the menu
   - If you don't see this option:
     1. Press Command + Space to open Spotlight Search
     2. Type "Terminal" and press Enter
     3. In Terminal, type:
        ```bash
        cd Desktop/Drone_Simulator
        ```

5. In the Terminal window, start JupyterLab:
   ```bash
   jupyter lab
   ```
   <img width="387" alt="Screenshot 2024-12-20 at 12 14 44 PM" src="https://github.com/user-attachments/assets/055cc140-64a2-4410-87fd-ebd9a9f1c365" />

6. Your default web browser will open with JupyterLab
   <img width="850" alt="Screenshot 2024-12-20 at 11 55 27 AM" src="https://github.com/user-attachments/assets/5abe350b-6818-4364-bcf3-f59e0beb667a" />


### Next Step, Test Hello World Python File [HelloWorld_Jupy.md](./HelloWorld_Jupy.md)
