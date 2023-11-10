import json

def lambda_handler(event, context):
    # Print the incoming event for debugging purposes
    print("Received event: " + json.dumps(event, indent=2))

    # Extract relevant information from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Perform some processing or log information
    print(f"File '{key}' was added to bucket '{bucket}'.")

    # You can return a response if needed
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
