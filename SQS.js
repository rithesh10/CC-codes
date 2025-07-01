import { SQSClient, SendMessageCommand, ReceiveMessageCommand } from "@aws-sdk/client-sqs"; 
 
const region = "eu-north-1"; // Change to your queue region
const queueUrl = "https://sqs.eu-north-1.amazonaws.com/123456789012/MyQueue"; // Replace  
const sqs = new SQSClient({ region }); 
 
export const handler = async (event) => { 
    // Send a message 
    const sendCommand = new SendMessageCommand({ 
        QueueUrl: queueUrl, 
        MessageBody: "Hello from Lambda!" 
    }); 
    await sqs.send(sendCommand); 
 
    // Receive a message 
    const receiveCommand = new ReceiveMessageCommand({ 
        QueueUrl: queueUrl, 
        MaxNumberOfMessages: 1, 
        WaitTimeSeconds: 5 
    }); 
    const response = await sqs.send(receiveCommand); 
 
    return { 
        statusCode: 200, 
        body: JSON.stringify({ 
            sent: "Message sent to SQS.", 
            received: response.Messages || [] 
        }) 
    }; 
}; 
