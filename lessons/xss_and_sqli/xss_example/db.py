import sqlite3
import html

def connect_db():
    db = sqlite3.connect('test.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, comment TEXT)')
    db.commit()
    return db


def insert_comment(comment):
    session = connect_db()
    #comment = html.escape(comment)
    #print(comment)
    session.cursor().execute(f"INSERT INTO comments (comment) VALUES ('{comment}')")
    session.commit()
    

def get_comments():
    session = connect_db()
    results = []
    for (comment,) in session.cursor().execute('SELECT comment FROM comments').fetchall():
        results.append(comment)
    return results