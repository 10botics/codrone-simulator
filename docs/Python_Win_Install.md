## ⚠️ **CRITICAL INSTALLATION NOTICE** ⚠️
==================================
> This installation requires a desktop or laptop computer with full Administrator privileges. Without proper administrator access, the setup process may not work correctly.

## Check Existing Python Installation

If Python is already installed, you can skip to [Jupyterlab_Win_Install.md](./Jupyterlab_Win_Install.md).

To check if Python is installed:
1. Open Command Prompt (cmd)
2. Type the following command:
   ```bash
   python --version
   ```
3. If you see `Python 3.11.0` (or similar version), you can skip to [PART 2: Install pip package]

![image](https://github.com/user-attachments/assets/3c3efdc3-2346-4c9f-abd8-14042a9fabcc)

If Python is not installed, continue reading below.

## Python Installation Methods

We recommend trying Method 1 first. If you encounter any issues, then proceed with Method 2.

1. Python.org Installer (Primary Method)
   - Pros:
     - Automatically adds Python to PATH
     - Full control over installation
     - Works with all tools and libraries
   - Cons:
     - Requires manual download and setup

2. Windows Store Installation (Backup Method)
   - Pros:
     - Easy installation through Store
     - Automatic updates
   - Cons:
     - Does not add Python to PATH
     - Limited control and compatibility

Note: Start with Method 1 (Python.org Installer) as it provides the most reliable setup. Only if you experience problems with Method 1 should you try Method 2 (Windows Store Installation), which is detailed below.


## Install Python 3.11 Python.org Installer

1. Download Python 3.11
   - Click Here to Download [Python 3.11](https://www.python.org/downloads/release/python-3110/)
   - Scroll down to "Windows installer (64-bit)"
   - Click to download the .exe file

   ![image](https://github.com/user-attachments/assets/da319689-faae-4b6f-b2c7-30e32973b650)

2. Install Python 3.11
   - Open the downloaded .exe file
   - IMPORTANT: Check "Add Python.exe to PATH" box

   ![image](https://github.com/user-attachments/assets/f84407af-0e7a-4e46-a717-9985d158b0f1)
   
   - Click "Install Now"

   ![image](https://github.com/user-attachments/assets/8203d721-7018-4add-b5ee-29b97e6b6c93)

   - Wait for installation to complete
   - Click "Close" when finished

   ![image](https://github.com/user-attachments/assets/5b6bc763-dd6f-45d4-8c87-18b83c69ef2d)

3. Verify Installation
   - Open Command Prompt (cmd)
   - Type:
     ```bash
     python --version
     ```
   - You should see "Python 3.11.0" (or similar version)

## Install Python 3.11 Windows Store

1. Python 3.11
   - [Python Windows Store Install Link](https://apps.microsoft.com/detail/9NRWMJP3717K?hl=en-us&gl=HK&ocid=pdpshare)
   - Install using the Windows Store
   
   ![Python Store](https://github.com/user-attachments/assets/468f10a4-1159-400c-a489-90fc0612e00c)
   
   - Select View in Store
   
   ![Python Search](https://github.com/user-attachments/assets/ffd89487-ea79-4987-addd-01e29ffaced0)

  ## ⚠️ IMPORTANT: You MUST add Python to your system PATH for it to work properly ⚠️
   Follow these steps:

   1. Open Command Prompt (cmd)

   ![image](https://github.com/user-attachments/assets/5a7bc964-cf2f-4716-ba8a-d8ee80773b7e)

   2. Run this command to get your Python site packages path:
      ```bash
      python -m site --user-site
      ```

   ![image](https://github.com/user-attachments/assets/ad47de4d-425e-43db-8d81-afd108f6b1af)

   3. Copy the output path (it should end with 'site-packages')

   ![image](https://github.com/user-attachments/assets/4687943d-32b1-42d1-803f-aba0a76b5bb0)

   4. In Notepad:
      - Paste the copied path
      - Replace 'site-packages' at the end with 'Scripts'
      - Save this modified path - you'll need it in the next steps

      ![image](https://github.com/user-attachments/assets/1818f50c-3eef-409f-927c-79e0fe218910)

   5. Add Python to System PATH:
      - Open Windows Search
      - Type "Edit the system environment variables"

      ![image](https://github.com/user-attachments/assets/b8fb4807-03af-4735-b3a7-cbf8afda3768)
      
      - Click "Environment Variables" button

      ![image](https://github.com/user-attachments/assets/38444940-05c3-495c-a810-ae9236256f63)

      - Under "System Variables" section, find "Path"

      ![image](https://github.com/user-attachments/assets/b37a5ba0-5e42-423a-a799-ccf59f4ba743)
      
      - Click "New"
      - Paste the Scripts path you saved earlier

      ![image](https://github.com/user-attachments/assets/bdbde882-5861-48f9-aa14-f57dc4fd717c)

      - Click "OK" on all windows to save changes

   Note: Make sure you paste the path ending in 'Scripts', not 'site-packages'


   ### return to [README.md](/README.md)