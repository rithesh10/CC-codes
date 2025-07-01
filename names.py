import boto3
import random

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')  # Replace with your table name

# Sample data
names = ["Ravi", "Sneha", "Arjun", "Meera", "Amit", "Sara", "Vikram", "Priya", "Kabir", "Anjali",
         "Nikhil", "Tina", "Rakesh", "Neha", "Manoj"]
subjects = ["Math", "Science", "English", "History", "Geography", "Art", "Computer"]

# Insert 15 entries
for i in range(15):
    student_id = f"S{i+1:03}"
    item = {
        'student': student_id,
        'student_name': names[i],
        'fav_sub': random.choice(subjects),
        'rating': round(random.uniform(3.0, 5.0), 1)
    }
    
    # Put item into DynamoDB
    table.put_item(Item=item)

print("✅ 15 items inserted.\n")

# Fetch and print the inserted items
response = table.scan()
for item in response['Items']:
    print(f"{item['student']} | {item['student_name']} | {item['fav_sub']} | Rating: {item['rating']}")
