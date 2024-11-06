import boto3,time

queue_url = "https://sqs.us-east-2.amazonaws.com/337225672478/GouravSQS"


# This function receives messages from the specified SQS queue.
def receive_messages(queue_url):
    sqs_client = boto3.client(
        'sqs',
        region_name='us-east-2',
    )

    # Continuously gets the message from the queue . This loop runs indefinitely.
    while True:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=10
        )

        messages = response.get('Messages', [])

        # Process any received messages if there are any in the response.
        if messages:
            for message in messages:
                print(f"Received message: {message['Body']}")
                # sqs_client.delete_message(
                #     QueueUrl=queue_url,
                #     ReceiptHandle=message['ReceiptHandle']
                # )
#use mysql and save the data

        # Print a message if no messages were received in response.
        else:
            print("No messages received")

        time.sleep(5)  # Wait before polling again


if __name__ == "__main__":
    receive_messages(queue_url)