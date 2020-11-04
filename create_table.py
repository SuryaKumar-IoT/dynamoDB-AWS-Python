import boto3

#dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb=boto3.client(
    "dynamodb",
    aws_access_key_id="AKIAXHI5XG5NM4OBVWYK",
    aws_secret_access_key="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",
    region_name="us-east-1"
)

table = dynamodb.create_table(
    TableName='PhoneBook',
    KeySchema=[
        {
            'AttributeName': 'ID',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:Creating")
