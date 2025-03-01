import sqlite3

# Connect to SQLite database (Creates 'student.db' if not exists)
connection = sqlite3.connect("student.db")

# Creating a cursor object
cursor = connection.cursor()

# SQL to create the STUDENT table
table_info = '''
    CREATE TABLE IF NOT EXISTS STUDENT (
        NAME TEXT,
        CLASS TEXT,
        SECTION TEXT,
        MARKS INT
    )
'''

# Execute table creation
cursor.execute(table_info)

# Clear existing records in the STUDENT table
cursor.execute("DELETE FROM STUDENT")

# Insert records into STUDENT table
cursor.executemany('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)''', [
    ('kavya', 'datascience', 'A', 80),
    ('Sravya', 'datascience', 'C', 50),
    ('bhavya', 'ML', 'A', 80),
    ('havya', 'datascience', 'B', 83),
    ('navya', 'AI', 'A', 19),
    ('keerthi', 'datascience', 'B', 70),
    ('divya', 'AI', 'C', 64),
    ('lavanya', 'ML', 'A', 46)
])

# Commit changes
connection.commit()

# Fetch and display all records
print('The inserted records are:')
data = cursor.execute('SELECT * FROM STUDENT')

for row in data:
    print(row)

# Close the database connection
connection.close()