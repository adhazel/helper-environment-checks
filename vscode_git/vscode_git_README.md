# vscode_git: Setup and test steps

This informal guide walks you through the process of setting up Visual Studio Code (VS Code) to work with GitHub via SSH on Windows. It includes instructions for setting up GitHub SSH keys, cloning a repository, and pushing updates to a branch in GitHub.

## Pre-requisite

- GitHub account
- Install git. If not already installed, you can download it from [Git for Windows](https://gitforwindows.org/). Select the options to include Git Bash in the installation.
- Complete the steps in [vscode_python](../vscode_python/vscode_python_README.md)
- Know how or desire to learn to program with Python :)

## Set up a GitHub SSH Key

1. Open Git Bash. 
1. Run ```ssh-keygen -t rsa -b 4096 -C "your_email@example.com"```, replacing "your_email@example.com" with your GitHub email address.
1. When prompted to "Enter a file in which to save the key," press **Enter**. This accepts the default file location.
1. At the prompt, type a secure passphrase. Store this passphrase in an encrypted password keeper. You will refer to this each time you clone a repository.
1. Start the SSH agent in the background by running ```eval "$(ssh-agent -s)"```.
1. Add your SSH private key to the ssh-agent by running ```ssh-add ~/.ssh/id_rsa```.
1. Copy the SSH public key to your clipboard by running ```cat ~/.ssh/id_rsa.pub | clip```.
1. Go to GitHub. Click the user icon in the upper right corner of the browser window. Select the **Settings** menu item. Got to the **Access / SSH and GPG Keys** page.
1. Click **New SSH Key**, give your key a title, paste the key into the **Key** field, and click **Add SSH Key**.

## Cloning a Repository

1. Go to the GitHub repository and branch you want to clone on the **Code** page.
    - The next section will walk through how to create a new branch and push a commit to it.
1. Click the green **Code** menu and copy the SSH URL (it should start with git@github.com:).
1. Open VS Code without opening a folder.
1. Open the command palette (**View > Command Palette** or ```Ctrl+Shift+P```) and run ```Git: Clone```.
1. Paste the SSH URL and press **Enter**.
1. In the command palette, enter your SSH passphrase from the previous section.
1. Choose a directory to clone the repository to, and click **Select Repository Location**.
1. Once the repository is cloned, click **Open** in the prompt to open the repository.

## Create a branch

1. If continuing from the previous section, skip this step. Ensure you are connected to git by doing one of the below:
    - In VS Code, with a cloned repository open, ensure you see a git branch name in the lower left corner of VS Code. 
    - Click on the **Source Control** icon in the left sidebar (or press ```Ctrl + Shift + G```). Ensure the repo and branch appear in the **Source Control Repositories** area in the **Source Control** panel.
1. Open the command palette (**View > Command Palette** or ```Ctrl+Shift+P```) and run ```Git: Create Branch```.
1. Enter a branch name (such as your name) and press **Enter**.

## Make changes and commit them to a branch
1. If continuing from the previous section, skip this step. Ensure you are connected to the respository **and branch that you want to commit changes to** by doing one of the below:
    - In VS Code, with a cloned repository open, examine the git branch name in the lower left corner of VS Code. 
    - Click on the **Source Control** icon in the left sidebar (or press ```Ctrl + Shift + G```). Ensure the repo and branch appear in the **Source Control Repositories** area in the **Source Control** panel.
1. Make code changes: 
    1. In the **Explorer** page (```Ctrl + Shift + E```), select the `vscode_python` folder. Then, hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `newstuff.txt` and click **Enter**.
    1. Enter something (e.g., `XYZ`) into the file when it opens and save the file (`Ctrl + S`).
1. Click on the "Source Control" icon in the left sidebar (or press ```Ctrl + Shift + G```).
1. Commit changes: 
    1. Enter a commit message in the **Message** field and press ```Ctrl + Enter``` to commit the changes.
    1. Hover over the **Source Control** header and select the elipsis **More Actions** menu. 
    1. Select the **Pull / Push > Sync** menu item. 
    1. Then, click **OK** when prompted to create the branch remotely. 
    1. Type your SSH passphrase in the Command Palette prompt and press ```Enter```.

[[Back to top](#vscode_git-setup-and-test-steps)]


