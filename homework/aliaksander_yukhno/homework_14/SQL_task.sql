insert into students (name, second_name, group_id) values ('Alex', 'Yuk', 1)

insert into books (title, taken_by_student_id) values ('Economy', 100004)

insert into books (title, taken_by_student_id) values ('Biology', 100004)

insert into books (title, taken_by_student_id) values ('Fizzy lang', 100004)

insert into `groups` (title, start_date, end_date) values ('QPy', 'nov', 'jan') 

update students set group_id = '25218' where id = '100004'

insert into subjects (title) values ('Math') 

insert into subjects (title) values ('Biology')

insert into subjects (title) values ('Economy') 

insert into subjects (title) values ('Physics') 

insert into lessons  (title, subject_id) values ('Addition', '23927') 

insert into lessons  (title, subject_id) values ('Multiplication', '23927') 

insert into lessons  (title, subject_id) values ('Flowers', '23928')

insert into lessons  (title, subject_id) values ('Mammals', '23928')

insert into lessons  (title, subject_id) values ('Forex', '23929')

insert into lessons  (title, subject_id) values ('Banks', '23929') 

insert into lessons  (title, subject_id) values ('Velocity', '23930') 

insert into lessons  (title, subject_id) values ('Energy', '23930') 

insert marks (value, lesson_id, student_id) values ('5', '77618', '100004')

insert marks (value, lesson_id, student_id) values ('10', '77619', '100004')

insert marks (value, lesson_id, student_id) values ('9', '77620', '100004')

insert marks (value, lesson_id, student_id) values ('4', '77621', '100004')

insert marks (value, lesson_id, student_id) values ('6', '77622', '100004')

insert marks (value, lesson_id, student_id) values ('1', '77623', '100004')

insert marks (value, lesson_id, student_id) values ('8', '77624', '100004')

insert marks (value, lesson_id, student_id) values ('2', '77625', '100004')

select * from marks where student_id = '100004'

select * from books where taken_by_student_id = '100004'

select *
from students
left join `groups` ON students.group_id = `groups`.id
left join books ON books.taken_by_student_id = students.id
left join marks ON marks.student_id = students.id
left join lessons ON marks.lesson_id = lessons.id
left join subjects ON lessons.subject_id = subjects.id
where students.id = '100004'; 

