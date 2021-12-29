import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres'
)

def fixed_get_user(username: str):
    results = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE name = %(name)s",
                       {
                           'name': username
                       })
        for result in cursor:
            results.append(result)
    return results

print(fixed_get_user('user-1'))

print(fixed_get_user("'; SELECT * FROM users; --"))