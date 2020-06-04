import os
from app.bot import run
import json


def lambda_handler(event='', context=''):
    what_to_print = os.environ.get("GITHUB_URL")
    if what_to_print:
        run()
        return {
            'statusCode': 200,
            'body': json.dumps(what_to_print)
        }
    return {
        'statusCode': 500,
        'body': json.dumps("Failed!")
    }


if __name__ == '__main__':
    lambda_handler()
