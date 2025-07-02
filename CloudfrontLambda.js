const AWS = require('aws-sdk');
const dynamodb = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
    const { rollno, name, subject, rating } = JSON.parse(event.body);

    const params = {
        TableName: "FeedbackTable",
        Item: { rollno, name, subject, rating }
    };

    try {
        await dynamodb.put(params).promise();
        return {
            statusCode: 200,
            headers: {
                "Access-Control-Allow-Origin": "https://dd2iz5boum8an.cloudfront.net/", // or your domain
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST"
            },
            body: JSON.stringify({ message: "Feedback submitted!" })
        };
    } catch (err) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: err.message })
        };
    }
};


