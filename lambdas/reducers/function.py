import boto3

from netCDF4 import Dataset

def handler(event: dict, context: dict) -> dict:
    return {"statusCode": 200, "body": "Reducer Lambda"}