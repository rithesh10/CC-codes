import boto3
import random
from decimal import Decimal  # ✅ required for DynamoDB number types

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')  # Replace with your table name

# Sample data
names = ["Ravi", "Sneha", "Arjun", "Meera", "Amit", "Sara", "Vikram", "Priya", "Kabir", "Anjali",
         "Nikhil", "Tina", "Rakesh", "Neha", "Manoj"]
subjects = ["Math", "Science", "English", "History", "Geography", "Art", "Computer"]

# Insert 15 entries with student ID as string (e.g., "S001")
for i in range(15):
    student_id = f"S{i+1:03}"  # S001, S002, ..., S015
    item = {
        'student': student_id,
        'student_name': names[i],
        'fav_sub': random.choice(subjects),
        'rating': Decimal(str(round(random.uniform(3.0, 5.0), 1)))  # ✅ Convert float to Decimal
    }

    # Insert item into DynamoDB
    table.put_item(Item=item)

print("✅ Successfully inserted 15 student records.\n")

# Fetch and print the inserted records
response = table.scan()
for item in response['Items']:
    print(f"{item['student']} | {item['student_name']} | {item['fav_sub']} | Rating: {item['rating']}")
