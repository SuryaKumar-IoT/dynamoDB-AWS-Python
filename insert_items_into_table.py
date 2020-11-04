import boto3
# Create a table called Employee
 
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
mytable = dynamodb.create_table(
TableName= 'Employee',KeySchema=[
    {
        'KeyType': 'HASH',
        'AttributeName': 'Id'
    },
    {
        'KeyType': 'RANGE',
        'AttributeName': 'Sal'
    }],
    AttributeDefinitions=[
    {
        'AttributeName': 'Id',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'Sal',
        'AttributeType': 'N'
    }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)
# Wait until the table exists.
mytable.meta.client.get_waiter('table_exists').wait(TableName='Employee')
print('Table is ready, please continue to isert data.')
 
# Insert the data into dynamodb table
mytable.put_item(
Item={
'Id': 1,
'FirstName': 'Ramasankar',
'LastName': 'Molleti',
'Dept': 'IT',
'Sal': 5000
}
)
mytable.put_item(
Item={
'Id': 1,
'FirstName': 'Sourav',
'LastName': 'Mukherjee',
'Dept': 'IT',
'Sal': 10000
}
)
mytable.put_item(
Item={
'Id': 1,
'FirstName': 'Praveen',
'LastName': 'Kumar',
'Dept': 'Finance',
'Sal': 5000
}
)
mytable.put_item(
Item={
'Id': 1,
'FirstName': 'Suresh',
'LastName': 'Kumar',
'Dept': 'Finance',
'Sal': 12000
}
)
 
response = mytable.scan()
 
for i in response['Items']:
    print("added item:", i['Id'], ":", i['FirstName'], ":", i['LastName'], ":", i['Dept'], ":", i['Sal'])
