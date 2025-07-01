import boto3
from collections import defaultdict

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('students')

response = table.scan()
items = response['Items']

sorted_items = sorted(items, key=lambda x: x['student_name'])

print("\nStudents in alphabetical order by student_name:")
for item in sorted_items:
    print(f"{item['student']} | {item['student_name']} | {item['fav_sub']} | Rating: {item['rating']}")
count_rating_5 = sum(1 for item in items if int(item['rating']) == 5)
print(f"\nCount of students with rating = 5: {count_rating_5}")
ratings_by_sub = defaultdict(list)
for item in items:
    ratings_by_sub[item['fav_sub']].append(int(item['rating']))
print("\nAverage rating per subject:")
for subject, ratings in ratings_by_sub.items():
    avg = sum(ratings) / len(ratings)
    print(f"{subject}: {avg:.2f}")
student_id_to_update = 'S01'
new_name = 'Alicia'
table.update_item(
    Key={'student': student_id_to_update},
    UpdateExpression='SET student_name = :newname',
    ExpressionAttributeValues={':newname': new_name}
)
print(f"\nUpdated student_name of student '{student_id_to_update}' to '{new_name}'")
seen = set()
for item in sorted_items:
    key = (item['student_name'], item['fav_sub'])
    if key in seen:
        # Delete duplicate item by primary key 'student'
        table.delete_item(Key={'student': item['student']})
        print(f"Deleted duplicate: {item['student']} | {item['student_name']} | {item['fav_sub']}")
    else:
        seen.add(key)
print("\nDuplicate removal complete.")
