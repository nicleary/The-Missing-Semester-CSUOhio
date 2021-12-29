import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres'
)

def get_user(username: str):
    results = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = '%s'" % username)
        for result in cursor:
            results.append(result)
    return results

print(get_user('user-1'))

print(get_user("'; SELECT * FROM users; --"))