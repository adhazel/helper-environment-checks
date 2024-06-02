# vscode_azurecli: Setup and test steps

Use the following steps as an informal guide to setting up VS Code to run azure cli in a VS Code Command Prompt terminal or python notebook.

- For a complete list of commands, see https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest.
- The CLI can be ran in many environments -- anywhere where shell scripts can be ran as well as the Azure Cloud Shell. This helper file shows limited options.


## Pre-requisite

- A Python environment with Jupyter Notebook support (such as Jupyter Lab or the Python extension for Visual Studio Code)
    - Complete the steps in [vscode_python](../vscode_python/vscode_python_README.md)

## Install the az cli

1. Select **Terminal** > **New Terminal**.
1. From the **Terminal** window, (typically on the bottom of your screen), click the `+` button and launch the **Command Prompt** terminal type.
1. Enter `az --version`.
1. The version information is returned. To upgrade the az cli, in your terminal, enter `az upgrade`.
1. If the CLI information is not returned, follow the install instructions on [Microsoft Learn: Install Azure CLI on Windows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&tabs=azure-cli).

## Connect to an Azure subscription using the az CLI in the Terminal

1. Open the Azure portal (https://portal.azure.com). 
1. From the **Terminal** window, (typically on the bottom of your screen), click the `+` button and launch the **Command Prompt** terminal type.
1. Run each of the below lines, replacing all caps values with those applicable in your Azure subscription.
    - `set TENANT=xxx` Replace the xxx with the value on the Entra resource Overview page in the **Primary domain** attribute. To ensure it is set correctly, run `echo %TENANT%`.
    - `set SUBSCRIPTION_ID=xxx` Replace the xxx with teh value on the Subscription resource Overview page in the  **Subscription ID** attribute. To ensure it is set correctly, run `echo %SUBSCRIPTION_ID%`.
1. Type `az login --tenant %TENANT%` and press **Enter**. A popup window will appear asking you to sign in. Navigate through the prompts and press **Enter** when asked to select a subscription.
1. Type `az account set -s %SUBSCRIPTION_ID%` and press **Enter**.
1. Type `az account show` and check the output to ensure you are working in the correct subscription.
1. Type `az group list` to return a list of resource groups in this subscription.

## Connect to an Azure subscription using the az CLI in a notebook

1. Follow the steps in [vscode_python](../vscode_python/vscode_python_README.md) to ensure you are able to run python notebooks.
1. In the **Explorer** pane, select the `vscode_python` folder. Then, hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `notebook-test.ipynb` and click **Enter**.
1. From within the ipynb file, select **View** > **Command Palette**. Then type `Notebook: Select Notebook Kernel` and press **Enter**. When prompted, select `Python Environment` and then select the option aligned with your virtual environment (e.g. `Python 3.10.** ('.venv': venv)`).
1. In the 1st cell, type the cli command to login to Azure. If you ahve access to multiple tenants, use the tenant parameter, replacing the value shown below with your tenant Id.See [Find your Microsoft Entra Tenant](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-microsoft-entra-tenant) to find your tenant id. Execute this cell and complete the interactive prompts that appear in a popup window.
    ```
    !az login
    ```

    or

    ```
    !az login --tenant xxx
    ```
1. In a new cell, enter the below. Execute the cell to set the subscription.
    ```
    my_subscription_id = "xxx"
    !az account set --subscription $my_subscription_id
    ```
1. In a new cell, enter one of the below commands as a means of testing your CLI connection. 
    ```
    # show connected account
    !az account show
    ```
    
    or 
    
    ```
     # list resource groups that exist within the subscription
     !az group list
     ```

[[Back to top](#vscode_azurecli-setup-and-test-steps)]