users = [
    {
        "name": "ali",
        "age": 19
    },
    {
        "name": "vali",
        "age": 21
    },
    {
        "name": "jon",
        "age": 20
    },
]

oldest = users[0]
for user in users[1:]:
    if oldest['age'] < user['age']:
        oldest = user

print(oldest)
