import boto3


function_name = "NiceAssignmentStack-NiceAssignmentFunction766FC65A-QKlVsgaJLNb8"

# Create Lambda client
client = boto3.client("lambda", region_name="eu-central-1")

# Invoke Lambda
response = client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',  # Wait for the function to finish
    Payload=b'{}'
)

print("Lambda invoked successfully!")
print(response['Payload'].read().decode())