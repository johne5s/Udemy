import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
users = [
    (1, 'jose', 'asdf'),
    (2, 'john', 'asdf'),
    (3, 'jj', 'asdf'),
    (4, 'sara', 'asdf')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()