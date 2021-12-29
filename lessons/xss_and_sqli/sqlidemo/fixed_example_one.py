import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres'
)

def safe_is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("SELECT admin FROM users WHERE name = %(name)s", {
            'name': username
        })
        result = cursor.fetchone()
    if result is None:
        return False
    admin, = result
    return admin

print(safe_is_admin('user-4'))

print(safe_is_admin("'; select true; --"))