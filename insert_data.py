import boto3

dynamodb=boto3.resource("dynamodb",region_name="us-east-1")

table=dynamodb.Table('PhoneBook')
table.put_item(Item={
    'ID':9502350936,
    'Name':"Sindhu"
    }
)
print(table.scan())
