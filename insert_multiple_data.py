import boto3

dynamodb=boto3.resource("dynamodb",region_name="us-east-1")
table=dynamodb.Table('PhoneBook')

with table.batch_writer() as batch:
    batch.put_item(Item={"ID": 9703492040, "Name": "Praveen Kumar"})
    batch.put_item(Item={"ID": 9577566577, "Name": "Annaya"})
    batch.put_item(Item={"ID": 7660801991, "Name": "Darling"})
    batch.put_item(Item={"ID": 9577522533, "Name": "abhinav"})

print("ok")
