# Windows Setup

## ⚠️ **CRITICAL INSTALLATION NOTICE** ⚠️
==================================
> This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.

## Windows Jupyter Lab Setup

1. Install JupyterLab

   Open terminal/command prompt:


   ![image](https://github.com/user-attachments/assets/8c573a20-fa64-41d8-bcbe-d7c848c9332f)
   
   Run the code below:
   ```bash
   pip install jupyterlab
   ```
   
   ![image](https://github.com/user-attachments/assets/9479a111-2aa9-4954-9a74-f0821a2c59e4)


2. Download Required Files
   - Download JupyterLab Files: [Download JupyterLab Files](https://github.com/10botics/codrone-simulator/blob/main/Drone%20Simulator.zip)
   ![image](https://github.com/user-attachments/assets/d7daf959-4b1a-4ae2-acfe-26e78641a49b)

3. Extract Files
   - Locate the downloaded Drone Simulator.zip file
   - Right-click and select "Extract All..."
   - Choose "Desktop" as the destination
   - Click "Extract"
   
   ![image](https://github.com/user-attachments/assets/4b0905b0-901a-4248-81e7-402ccae49066)
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
6. Open the Codrone Simulator and select "Free Play"
![image](https://github.com/user-attachments/assets/a3f1c34a-4dfa-451c-b784-702e550f6e1e)
7. Make sure you see this window in the simulator
![image](https://github.com/user-attachments/assets/8973434f-f91e-4903-a16a-b88c335b4e62)

8. Follow the instructions in the notebook to move the drone in the simulator


### return to [README.md](./README.md)