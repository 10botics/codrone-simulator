

## Install Drone Simulator

## ⚠️ **CRITICAL INSTALLATION NOTICE** ⚠️
==================================
> This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.


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


   ### return to [README.md](./README.md)