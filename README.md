# Github Bot
- **Author**: Alex Nguyen
- **License**: MIT
- **Description**: Simple python-based github bot that will fetch Github repos from a given account


#### To run this application
- Python >= v3.6
- Clone this repo: ```git clone https://github.com/usefulmana/github-bot.git```
- Move to the bot folder: ```cd github-bot```
- Install dependencies: ```pip install -r requirements.txt```
- Activate your python virtual env
- Move to the app folder: ```cd app```
- Create a .env file with the following values (or you can use actual env variables):
```
AUTH_TOKEN = <GITHUB_TOKEN>
GITHUB_URL = <GET_URL>
DB_STRING = <DB_CONNECTION_STRING>
```
- GITHUB_TOKEN can be obtained by visiting **Github** &#8594; **Settings** &#8594;
**Developer Settings** &#8594; **Personal Access Token** &#8594; **Generate New Token**
- GET_URL can be customised. Read more about it [here](https://developer.github.com/v3/repos/)
- Read about DB_CONNECTION_STRING [here](https://docs.sqlalchemy.org/en/13/core/engines.html)
- To run the app: ```python bot.py```