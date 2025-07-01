import boto3
import time
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# SNS client
sns = boto3.client('sns')

# Replace with your actual SNS topic ARN
TOPIC_ARN = 'arn:aws:sns:REGION:ACCOUNT_ID:CanteenOrderNotifications'

# Ordered food delivery flow with delay in seconds
ORDER_STATUS_FLOW = [
    ("Order Placed", "Order placed successfully. Thank you for ordering from our canteen!", 2),
    ("Preparing", "Your food is being freshly prepared by our kitchen team.", 5),
    ("Ready", "Your food is ready for pickup. Our delivery agent will arrive soon.", 5),
    ("Out for Delivery", "Your food is out for delivery. Please be available to receive it.", 5),
    ("Delivered", "Your food has been delivered. Enjoy your meal!", 0),
]

def publish_notification(subject: str, message: str) -> None:
    """
    Publishes a message to the SNS topic with a given subject and message.
    """
    try:
        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Subject=subject,
            Message=message
        )
        logger.info(f"Published '{subject}' notification | Message ID: {response['MessageId']}")
    except Exception as e:
        logger.error(f"Error publishing SNS message: {e}")
        raise

def lambda_handler(event, context):
    """
    Lambda function handler to simulate a canteen order flow and notify via SNS.
    """
    try:
        for subject, message, delay in ORDER_STATUS_FLOW:
            publish_notification(subject, message)
            if delay > 0:
                logger.info(f"Waiting {delay} seconds before next update...")
                time.sleep(delay)

        return {
            'statusCode': 200,
            'body': 'Order flow completed. All notifications sent successfully.'
        }

    except Exception as error:
        logger.error(f"Order flow failed: {error}")
        return {
            'statusCode': 500,
            'body': 'Failed to send all notifications.'
        }
