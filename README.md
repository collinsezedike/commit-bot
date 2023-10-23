# Python Auto Commit Bot

This is an auto commit robot. It monitors a specified directory and commits (via git) any change it detects.

## How to run

### Prequisites

- Python version 3.x.x must be installed.  

### Steps

1. Download the code zip and unzip afterward. Alternatively, clone the repository using the following command:  
`git clone https://github.com/collinsezedike/commit-bot.git`

2. Create a virtual environment using the following command:  
`python -m venv venv`  

3. Activate the virtual environment using the following command:  
`venv\scipts\activate` or `source venv/bin/activate`  
    Follow [this guide](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html) if your encounter any issue.

4. Install the dependencies using this command:  
`pip install -r requirements.txt`  

5. Start the bot with this command.  
`python main.py <targer-directory>`  
    Replace "\<targer-directory\>" with the path to the directory you want the robot to monitor.  

## Notes

- Make sure to run all commands inside root directory of the codebase. This directory should be `commit-bot/` or `commit-bot-main/`, depending on whether you cloned or downloaded the code.

- If the target directory path does not already exist, the robot will not create it. It will terminate the execution with an error.  

- The robot requires an internet connection to create a `.gitignore` file if it does not exists in the target directory. Aside this, the operation works completely offline.

- The robot does not push the committed changes to Github. Yet.  

- The robot creates log files that will not be committed.
