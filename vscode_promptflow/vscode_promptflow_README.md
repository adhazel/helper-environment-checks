# vscode_promptflow: Setup and test steps

This informal guide will help you setup and test the Prompt Flow SDK using Visual Studio Code.

## Learn more
- [Prompt flow EcoSystem Overview](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/community-ecosystem?view=azureml-api-2#prompt-flow-sdkcli)
- [Open Source Promptflow GitHub Repo](https://github.com/microsoft/promptflow)
    - [Promptflow SDK Quickstart](https://github.com/microsoft/promptflow/blob/main/docs/how-to-guides/quick-start.md)
- [Prompt flow SDK Reference](https://microsoft.github.io/promptflow/reference/index.html)


## Pre-requisite

- A Python environment with Jupyter Notebook support (such as Jupyter Lab or the Python extension for Visual Studio Code).
- A python environment. Follow the steps in [vscode_python](../vscode_python/vscode_python_README.md).
- Know how or desire to learn to program with Python :)
- An Azure OpenAI resource you can access the keys for. A GPT model is deployed and available for your use.

## Activate your virtual environment

1. Select **Terminal** > **New Terminal**.
1. From the **Terminal** window, (typically on the bottom of your screen), click the `+` button and launch the **Command Prompt** terminal type.
1. Type the following to execute the virtual environment activate bat file script: `"./.venv/Scripts/Activate.bat"`.
1. Ensure that the terminal now shows a `(.venv)` prefix. 

## Use a requirements file to install library dependencies

1. Click on the **Explorer** icon in the left sidebar (or press ```Ctrl + Shift + E```). 
1. Create a ```vscode_promptflow``` folder if it does not exist. Click on the folder name.
1. Hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `requirements.txt` and click **Enter**.
1. Add this below to the file. Then, save the file (`Ctrl + S`).
    ```
    promptflow
    promptflow-tools
    ```
1. In the **Terminal** window, you should have a cmd terminal that is showing the `(.venv)` prefix. Within this terminal, type `pip install -r ./vscode_promptflow/requirements.txt` and press **Enter**.
    - This may take several minutes. It is finished when a new line appears prefixed with `(.venv)`.

## Get Azure OpenAI API Base, Key, & Deployment Name

1. Open Azure and navigate to the Azure OpenAI resource.
1. On **Resource Management > Keys and Endpoint**, copy the API URL from the **Endpoint** attribute. 
1. On **Resource Management > Keys and Endpoint**, copy the API key from the **KEY 1** attribute. 
1. Capture the deployment name for the GPT model you intend you use for this guide. You can capture this using either Azure OpenAI Studio or AI Studio.
    - Using Azure OpenAI Studio: 
        1. Go to [oai.azure.com](oai.azure.com) and complete the prompts to select a directory, subscription, and Azure OpenAI resource.
        1. On the **Deployments** item from the left sidebar, review the deployment names. Note the **Deployment Name** for one of the models from the 'gpt*' **Model name** family.
    - Using Azure AI Studio: 
        1. Go to [ai.studio.com](ai.studio.com) and; on the upper right side of the page, select the Hub down-carret to expand the **Hub** selection pane. Select the Directory (tenant), Subscription, and Hub.
        1. On the **Shared resources > Deployments** item from the left sidebar, review the deployment names. Note the **Name** for one of the models from the 'gpt*' **Model name** family.

## Exploring promptflow

1. Run the command to initiate a prompt flow from a chat template, it creates folder named my_chatbot and generates required files within it:
    ```
    pf flow init --flow ./vscode_promptflow/my_chatbot --type chat
    ```
1. Establish a connection by running the command, using the azure_openai.yaml file in the my_chatbot folder. 
    
    **Important**: Do not save the key in the azure_openai.yaml file -- instead, replace the api key and base values you copied in an earlier section into the command below.
    
    ```
    pf connection create --file ./vscode_promptflow/my_chatbot/azure_openai.yaml --set api_key=<your_api_key> api_base=<your_api_base> --name open_ai_connection
    ```

1. Open the file ```./vscode_promptflow/my_chatbot/flow.dag.yaml```. This file outlines the flow, including inputs/outputs, nodes, connection, and the LLM model, etc.
1. Change the value on line 22 for deployment_name to the deployment name you captured in the above section. Save the file (```Ctrl + S```).
1. Interact with your chatbot in the VS Code terminal by running the below command.
    ```
    pf flow test --flow ./vscode_promptflow/my_chatbot --interactive
    ```
    Here is a sample interaction: 
    - User: ```Tell me a joke about books.```
    - Bot: Sure, here's a book-inspired joke for you:
    
        Why did the book go to the doctor?
        
        Because it had a bad case of the "story-ache"!
    - User: ```Good one, tell me another one, but make it reference a fairy tale.```
    - Bot: Certainly! Here's a fairy tale-inspired joke for you:

        Why did Cinderella get kicked off the soccer team?

        Because she always ran away from the ball, thinking it would turn into a pumpkin at midnight!
1. Press Ctrl + C to end the session once you are ready.

## (Optional) Use a requirements file to install commonly used library dependencies with prompt flow and llmops

1. Click on the **Explorer** icon in the left sidebar (or press ```Ctrl + Shift + E```). 
1. Create a ```vscode_promptflow``` folder if it does not exist. Click on the folder name.
1. Hover over the workspace header and click the **New File** icon to create a file within this folder. Name the new file `llmops_requirements.txt` and click **Enter**.
1. Add libaries to the llmops_requirements.txt file:
    - Enter the below:
        ```
        ipykernel
        nbstripout
        nbconvert
        promptflow
        promptflow-tools
        ```
    - If you are using Azure DevOps for LLMOps, add additional libraries documented here to the file: [GitHub/microsoft/llmops-promptflow-template/.azure-pipelines/requirements/](https://github.com/microsoft/llmops-promptflow-template/tree/main/.azure-pipelines/requirements)

    - If you are using github for LLMOps, add additional libraries documented here to the file: [GitHub/microsoft/llmops-promptflow-template/.github/requirements/](https://github.com/microsoft/llmops-promptflow-template/tree/main/.github/requirements)

1. Ensure there are no duplicate libraries in the file (if there are, keep the latest version) and save it (`Ctrl + S`).
1. In the **Terminal** window, you should have a cmd terminal that is showing the `(.venv)` prefix. Within this terminal, type `pip install -r ./vscode_promptflow/llmops_requirements.txt` and press **Enter**.
    - This may take several minutes. It is finished when a new line appears prefixed with `(.venv)`.

[[Back to top](#vscode_promptflow-setup-and-test-steps)]



