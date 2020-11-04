import boto3
from boto3.dynamodb.conditions import Key
dynamodb=boto3.resource("dynamodb",region_name="us-east-1")

table=dynamodb.Table('PhoneBook')

result=table.query(KeyConditionExpression=Key('ID').eq(7799204041))
print(result)

