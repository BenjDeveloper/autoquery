-- Classrooms
INSERT INTO classrooms (name, tag) VALUES
('Section A', 'A'),
('Section B', 'B'),
('Section C', 'C');

-- Teachers
INSERT INTO teachers (first_name, last_name, address, admission_date, salary, classroom_id) VALUES
('Maria', 'Perez', '123 Fake Street', '2021-09-01', 2800.00, 1),
('Juan', 'Garcia', '456 Main Avenue', '2020-03-15', 3100.00, 2),
('Laura', 'Sanchez', '789 Central Plaza', '2022-05-10', 2950.50, 3);

-- Students
INSERT INTO students (first_name, last_name, email, address, admission_date, classroom_id) VALUES
('Amelia', 'Martinez', 'amelia.martinez@school.com', '357 Martinez Street', '2022-01-10', 1),
('Ethan', 'Anderson', 'ethan.anderson@school.com', '995 Anderson Street', '2022-01-10', 2),
('Ava', 'Johnson', 'ava.johnson@school.com', '537 Johnson Street', '2022-01-10', 3),
('Evelyn', 'Johnson', 'evelyn.johnson@school.com', '333 Johnson Street', '2022-01-10', 1),
('Liam', 'Garcia', 'liam.garcia@school.com', '201 Garcia Street', '2022-01-10', 2),
('Emma', 'Johnson', 'emma.johnson@school.com', '746 Johnson Street', '2022-01-10', 3),
('Isabella', 'Martin', 'isabella.martin@school.com', '310 Martin Street', '2022-01-10', 1),
('Benjamin', 'Thompson', 'benjamin.thompson@school.com', '505 Thompson Street', '2022-01-10', 2),
('Harper', 'Taylor', 'harper.taylor@school.com', '292 Taylor Street', '2022-01-10', 3),
('Mason', 'Rodriguez', 'mason.rodriguez@school.com', '278 Rodriguez Street', '2022-01-10', 1),
('Sophia', 'Smith', 'sophia.smith@school.com', '890 Smith Street', '2022-01-10', 2),
('Lucas', 'Moore', 'lucas.moore@school.com', '144 Moore Street', '2022-01-10', 3),
('Charlotte', 'Brown', 'charlotte.brown@school.com', '798 Brown Street', '2022-01-10', 1),
('James', 'Taylor', 'james.taylor@school.com', '101 Taylor Street', '2022-01-10', 2),
('Mia', 'Williams', 'mia.williams@school.com', '614 Williams Street', '2022-01-10', 3),
('Logan', 'Hernandez', 'logan.hernandez@school.com', '753 Hernandez Street', '2022-01-10', 1),
('Elijah', 'Davis', 'elijah.davis@school.com', '183 Davis Street', '2022-01-10', 2),
('Olivia', 'Wilson', 'olivia.wilson@school.com', '692 Wilson Street', '2022-01-10', 3),
('Noah', 'Jones', 'noah.jones@school.com', '876 Jones Street', '2022-01-10', 1),
('Emily', 'White', 'emily.white@school.com', '315 White Street', '2022-01-10', 2),
('Daniel', 'Miller', 'daniel.miller@school.com', '204 Miller Street', '2022-01-10', 3),
('Chloe', 'Smith', 'chloe.smith@school.com', '487 Smith Street', '2022-01-10', 1),
('Sebastian', 'Jackson', 'sebastian.jackson@school.com', '630 Jackson Street', '2022-01-10', 2),
('Ella', 'Taylor', 'ella.taylor@school.com', '256 Taylor Street', '2022-01-10', 3),
('Alexander', 'Moore', 'alexander.moore@school.com', '912 Moore Street', '2022-01-10', 1),
('Grace', 'Thomas', 'grace.thomas@school.com', '134 Thomas Street', '2022-01-10', 2),
('Henry', 'Brown', 'henry.brown@school.com', '371 Brown Street', '2022-01-10', 3),
('Sofia', 'Johnson', 'sofia.johnson@school.com', '801 Johnson Street', '2022-01-10', 1),
('Jack', 'Davis', 'jack.davis@school.com', '422 Davis Street', '2022-01-10', 2),
('Aria', 'Miller', 'aria.miller@school.com', '211 Miller Street', '2022-01-10', 3);
