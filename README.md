# Python Auto Commit Bot

This is an auto-commit robot. It monitors a specified directory and commits (via git) any change it detects.

## How to run

### Prerequisites

- Python version 3.x.x must be installed.  

### Steps

1. Download the code zip and unzip afterwards. Alternatively, clone the repository using the following command:  
`git clone https://github.com/collinsezedike/commit-bot.git`

2. Create a virtual environment using the following command:  
`python -m venv venv`  

3. Activate the virtual environment using the following command:  
`venv\scipts\activate` or `source venv/bin/activate`  
    Follow [this guide](https://docs.python.org/3/library/venv.html) if you encounter any issues.

4. Install the dependencies using this command:  
`pip install -r requirements.txt`  

5. Start the bot with this command.  
`python main.py <targer-directory>`  
    Replace "\<targer-directory\>" with the path to the directory you want the robot to monitor.  

## Notes

- Run all commands inside the root directory of the codebase. This directory should be `commit-bot/` or `commit-bot-main/`, depending on whether you cloned or downloaded the code.

- If the target directory path does not already exist, the robot will not create it. It will terminate the execution with an error.  

- The robot requires an internet connection to create a `.gitignore` file if it does not exist in the target directory. Aside from this, the robot operations work completely offline.

- The robot does not push committed changes to Github. Yet.  

- The robot creates log files which will not be committed. You can delete them if you wish; they do not affect the robot's operation. In future, I may allow a `--no-log` flag which tells the robot not to create log files.
