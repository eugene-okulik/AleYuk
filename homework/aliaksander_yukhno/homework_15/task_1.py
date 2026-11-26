import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)",
               ('Alex', 'Yuk'))
student_id = cursor.lastrowid

insert_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
        ('Economy', student_id),
        ('Biology', student_id),
        ('Fizzy lang', student_id)
    ]
)
cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ('QPy', 'nov', 'jan'))
group_id = cursor.lastrowid

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
               (group_id, student_id))

cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Math',))
math_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Biology',))
bio_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Economy',))
econ_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES (%s)",
               ('Physics',))
phys_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Addition', math_id))
add_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Multiplication', math_id))
mult_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Flowers', bio_id))
flow_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Mammals', bio_id))
mam_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Forex', econ_id))
forex_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Banks', econ_id))
bank_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Velocity', phys_id))
velo_id = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ('Energy', phys_id))
energy_id = cursor.lastrowid

insert_query = "INSERT INTO marks (`value`, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query,
    [
        ("5", add_id, student_id),
        ("10", mult_id, student_id),
        ("9", flow_id, student_id),
        ("4", mam_id, student_id),
        ("6", forex_id, student_id),
        ("1", bank_id, student_id),
        ("8", velo_id, student_id),
        ("2", energy_id, student_id),
    ],
)

db.commit()

cursor.execute("SELECT * FROM marks WHERE student_id = %s",
               (student_id,))
print(f'Все оценки студента с id = {student_id}')
for row in cursor.fetchall():
    print(row)
print()

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s",
               (student_id,))
print(f'Все книги, которые находятся у студента с id = {student_id}')
for row in cursor.fetchall():
    print(row)
print()

select_query = """
SELECT *
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN books ON books.taken_by_student_id = students.id
LEFT JOIN marks ON marks.student_id = students.id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjects ON lessons.subject_id = subjects.id
WHERE students.id = %s;
"""
cursor.execute(select_query, (student_id,))
print(f'Вся информация о студенте с id = {student_id}')
for row in cursor.fetchall():
    print(row)
print()

db.close()
