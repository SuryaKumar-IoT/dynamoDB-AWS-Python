import boto3

dynamodb=boto3.resource("dynamodb",region_name="us-east-1")

table=dynamodb.Table('PhoneBook')

result=table.scan()
for i in result['Items']:
    print("ID:",i['ID'],",Name:",i['Name'])
