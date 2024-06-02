# vscode_python: Setup and test steps

Use the following steps as an informal guide to setting up VS Code to run python and python notebooks.

## Pre-requisites
- Know how or desire to learn to program with Python :)

## Install and Configure
1. A workstation with the following options:
    - Option 1 - Local machine or VM equipped with the following tools:
        - [Python 3.10](https://www.python.org/downloads/release/python-31011/): Install Python on your workstation. Ensure you select the options to add the install directory to your workstation paths.
        - [VS Code](https://code.visualstudio.com/download) Install the desktop version on your workstation
    - Option 2 - Develop in VS Code for the Web

1. Open VS Code.
1. Select **Extensions** from the left sidebar (or press ```Ctrl + Shift + X```). 
    - Enable the Microsoft published `Python` extension.
    - Enable the Microsoft published `Python Debugger` extension.
    - Enable the Microsoft published `Pylance` extension.
    - (Optional) Enable the Microsoft published `PowerShell` extension.

## Create a Workspace Folder and Python Environment

1. Create a new folder on your local machine where you want to store your project files. You can do this outside of VS Code using your operating system’s file explorer.
1. Within VS Code **File** menu, select **Open Folder**. Navigate to the folder you created above and open it within VS Code.
1. Click on the **Explorer** icon in the left sidebar (or press ```Ctrl + Shift + E```). Hover over the workspace header and click the **New Folder** icon. Name the new folder `vscode_python` and click **Enter**.
1. Select **View** > **Command Palette**. Then type `Python: Create environment` and press **Enter**.
1. Select the **Venv** option.
1. Choose the python installation path from the above steps.
1. Select **Terminal** > **New Terminal**.
1. From the **Terminal** window, (typically on the bottom of your screen), click the `+` button and launch the **Command Prompt** terminal type.
1. Type the following to execute the virtual environment activate bat file script: `"./.venv/Scripts/Activate.bat"`.
1. Ensure that the terminal now shows a `(.venv)` prefix. 

## Use a requirements file to pip install ipykernel, which can be used to run python notebooks

1. Click on the **Explorer** icon in the left sidebar (or press ```Ctrl + Shift + E```). 
1. Select the `vscode_python` folder. Then, hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `requirements.txt` and click **Enter**.
1. Add this text to line 1 in the file: `ipykernel==6.29.4`. Then, save the file (`Ctrl + S`).
1. In the **Terminal** window, you should have a cmd terminal that is showing the `(.venv)` prefix. Within this terminal, type `pip install -r ./vscode_python/requirements.txt` and press **Enter**.
    - This may take several minutes. It is finished when a new line appears prefixed with `(.venv)`.

## Test python files

1. Click on the **Explorer** icon in the left sidebar (or press ```Ctrl + Shift + E```).
1. In the **Explorer** panel, select the `vscode_python` folder. Then, hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `python-test.py` and click **Enter**.
1. Enter the text `print('hello world!')` into the file when it opens and save the file (`Ctrl + S`).
1. With the cursor inside of the file contents, on the upper right side of the file, click the **Run Python File** icon.
1. Examine the **Terminal** window and ensure you see `hello world!`. Triage if unsuccessful.
1. (Optional) Run the python-test.py file as a subprocess with an attached virtual environment. 
    1. In the Command Prompt terminal, type `python` and press enter. The cursor should then appear after the characters `>>>`. 
    1. Replicate the sample file [run_python_in_venv.py](/vscode_python/run_python_in_venv.py) in your local environment.
    1. Type `exec(open("./vscode_python/run_python_in_venv.py").read())` in the python shell and press enter.
    1. Examine the **Terminal** window and ensure you see `hello world!`. Triage if unsuccessful.


## Test python notebooks

1. In the **Explorer** panel, select the `vscode_python` folder. Then, hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `notebook-test.ipynb` and click **Enter**.
1. From within the ipynb file, select **View** > **Command Palette**. Then type `Notebook: Select Notebook Kernel` and press **Enter**. When prompted, select `Python Environment` and then select the option aligned with your virtual environment (e.g. `Python 3.10.** ('.venv': venv)`).
1. In the available cell, type `print('hello notebook!')`.
1. Click the **Execute cell** icon to the left of the cell to execute the cell's command. Ensure that `hello notebook!` prints in the cell output. Triage if unsuccessful.

## Cleanup 

Optionally, clean up any terminal windows opened. You can do this by clicking the barbage bin icon for each terminal window shown until the Terminal panel disappears. You can also issue a `clear` command to clear any previous commands from the window. 

From a new Command Prompt terminal, you can use one of the following to activate your virtual environment again: `".venv/Scripts/Activate.bat"`.

[[Back to top](#vscode_python-setup-and-test-steps)]