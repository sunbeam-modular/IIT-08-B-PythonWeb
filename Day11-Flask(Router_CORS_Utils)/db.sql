CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(100),
    mobile VARCHAR(10)
);

CREATE TABLE students(
    rollno INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    email VARCHAR(50),
    course VARCHAR(30)
);

INSERT INTO students(name, email, course) VALUES('John', 'john@gmail.com', 'DAC');
INSERT INTO students(name, email, course) VALUES('Dagny', 'dagny@gmail.com', 'DMC');
INSERT INTO students(name, email, course) VALUES('Jane', 'jane@gmail.com', 'DAC');
