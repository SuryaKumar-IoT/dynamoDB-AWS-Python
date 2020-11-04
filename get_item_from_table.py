import boto3
from boto3.dynamodb.conditions import Key
dynamodb=boto3.resource("dynamodb",region_name="us-east-1")

table=dynamodb.Table('PhoneBook')

result=table.get_item(Key={"ID": 7799204041, "Name": "Surya Kumar V"})
print(result['Item'])

