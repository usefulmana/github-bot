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

#### To deploy to AWS Lambda
- Combine all code into the ```lambda.py``` file
- On Windows, move the file into **venv** &#8594; **Libs** &#8594; **site-packages**
- Replace the ```psycopg2``` folder according to the instruction [here](https://github.com/jkehler/awslambda-psycopg2)
- Zip the content of **site-packages**
- Upload to AWS Lambda
- Raise execution time limit to 30 seconds just to be safe
- Change **Handler** to ```lambda.lambda_handler```
- If you are still confused, unzip the ```deploy.zip``` file to see an example