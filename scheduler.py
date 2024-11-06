import boto3,time
from schedule import Scheduler


QUEUE_URL = "https://sqs.us-east-2.amazonaws.com/337225672478/GouravSQS"

# This function receives messages from the specified SQS queue.
def receive_messages():
    sqs_client = boto3.client(
        'sqs',
        region_name='us-east-2',
    )
    response = sqs_client.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=5,
        WaitTimeSeconds=10  # Long polling
    )

    messages = response.get('Messages', [])

    # Process any received messages if there are any in the response.
    if messages:
        for message in messages:
            print(f"Received message: {message['Body']}")
            # sqs_client.delete_message(
            #     QueueUrl=QUEUE_URL,
            #     ReceiptHandle=message['ReceiptHandle']
            # )

    # Print a message if no messages were received in response.
    else:
        print("No messages received")

# Create a scheduler object to manage scheduled tasks
scheduler = Scheduler()

# Schedule the receive_messages function to run every 20 seconds
scheduler.every(20).seconds.do(receive_messages)

while True:
    # Continuously check for scheduled tasks and execute them if they are ready.
    scheduler.run_pending()
    time.sleep(1)
