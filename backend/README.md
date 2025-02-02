DEV SETUP
1. python3 -m venv venv
2. source venv/bin/activate
3. pip3 install fastapi uvicorn requests fastapi-cors
4. pip install "fastapi[standard]"
5. to run server
source venv/bin/activate
fastapi dev
or
uvicorn main:app --reload
6. to handle wrong or no interpreter error:
    Open VS Code and load your project.
    Open the Command Palette:
    Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (Mac).
    Access Workspace Settings:
    Type Preferences: Open Workspace Settings (JSON) and select it.
    This will open the settings.json file specific to your workspace.
    In the opened settings.json file, add or update the following configurations:
    {
        "python.defaultInterpreterPath": "backend/venv/bin/python",
        "python.venvPath": "${workspaceFolder}/backend/venv",
        "python.analysis.extraPaths": [
            "${workspaceFolder}/backend"
        ],
        "python.terminal.activateEnvironment": true
    }