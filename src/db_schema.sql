CREATE TABLE classrooms (
    classroom_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    tag CHAR(1) NOT NULL
);

CREATE TABLE teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    address VARCHAR(100),
    admission_date DATE,
    salary NUMERIC(10, 2),
    classroom_id INT REFERENCES classrooms(classroom_id)
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(100),
    age INT, 
    admission_date DATE,
    classroom_id INT REFERENCES classrooms(classroom_id)
);
