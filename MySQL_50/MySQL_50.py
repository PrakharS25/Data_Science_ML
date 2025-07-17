import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="2512"
)

mycursor = mydb.cursor()
# mycursor.execute("create database CollegeDB")
mycursor.execute("use CollegeDB")
# mycursor.execute("create table Students(Id int Primary key , Name varchar(50) , age int , Department varchar(30))")
# mycursor.execute(" INSERT INTO students (id, name, age, department) VALUES (101, 'Prakhar', 19, 'Computer Science'),(102, 'Suhani', 19, 'Media and Information'),(103, 'Ankit', 20, 'Computer Science'),(104, 'Priyanshu', 21, 'Software Engineering'),(105, 'Manas', 19 , 'Media and Information')")
# mydb.commit()
# mycursor.execute("Select * from students")
# print(mycursor.fetchall())
# mycursor.execute("Select * from students where age > 20")
# print(mycursor.fetchall())
# mycursor.execute("UPDATE Students SET Department= 'Mechanical' WHERE Name= 'Manas'")
# mydb.commit()
# mycursor.execute("delete from students where id = 105")
# mydb.commit()
# mycursor.execute("SELECT * FROM Students ORDER BY Age")
# print(mycursor.fetchall())
# mycursor.execute("SELECT DISTINCT Department FROM Students")
# print(mycursor.fetchall())
# mycursor.execute("SELECT COUNT(*) FROM Students")
# print(mycursor.fetchone())
# mycursor.execute("RENAME TABLE Students TO Students_Info")
# mycursor.execute("ALTER TABLE Students_Info ADD Email VARCHAR(100)")
# mycursor.execute("SELECT * FROM Students_Info WHERE Name LIKE 'A%'")
# print(mycursor.fetchall())
# mycursor.execute("SELECT * FROM Students_Info WHERE Age BETWEEN 18 AND 25")
# # print(mycursor.fetchall())
# mycursor.execute("SELECT * FROM Students_Info ORDER BY Age DESC LIMIT 1")
# print(mycursor.fetchone())
# mycursor.execute("SELECT * FROM Students_Info LIMIT 3")
# print(mycursor.fetchall())

# mycursor.execute("""
#     CREATE TABLE Courses(
#         C_Id INT PRIMARY KEY,
#         C_Name VARCHAR(100),
#         Credits INT       
#         )
# """)
# mycursor.execute("INSERT INTO Courses (C_Id, C_Name, Credits) VALUES (101,'Prakhar',7) , (102,'Suhani',9) , (103,'Ankit',10) , (104,'Priyanshu',9)")
# mydb.commit()
# mycursor.execute("SELECT * FROM Students_Info WHERE Department= 'Computer Science'")
# print(mycursor.fetchall())
# mycursor.execute("SELECT * FROM Students_Info WHERE Department IN ('Computer Science', 'Electrical')")
# print(mycursor.fetchall())
# mycursor.execute("SELECT * FROM Students_Info WHERE Age BETWEEN 20 AND 30")
# print(mycursor.fetchall())
# mycursor.execute("SELECT NOW()")
# print(mycursor.fetchone())
# mycursor.execute("SELECT Name AS S_Name, Age FROM Students_Info")
# print(mycursor.fetchall())
# mycursor.execute("SELECT * FROM Students_Info WHERE Department!= 'Mechanical'")
# print(mycursor.fetchall())
# mycursor.execute("DELETE FROM Students_Info")
# mydb.commit()

# 26-50

# mycursor.execute("""
#     CREATE TABLE Marks(
#         Id INT,
#         Subject VARCHAR(100),
#         Marks INT,
#         FOREIGN KEY (Id) REFERENCES Students_Info(Id)
#         )
# """)
# marks_data= [
#     (101, 'DBMS', 90),
#     (101, 'DSA', 85),
#     (102, 'DBMS', 78),
#     (102, 'DSA', 84),
#     (103, 'DBMS', 87),
#     (103, 'DSA', 89),
#     (104, 'DBMS', 75),
#     (104, 'DSA', 80),
#     (105, 'DBMS', 76),
#     (105, 'DSA', 88)
# ]
# mycursor.executemany("INSERT INTO Marks (S_Id, Subject, Marks) VALUES (%s, %s, %s)", marks_data)
# mydb.commit()
# mycursor.execute("""
#     SELECT s.Id, s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     JOIN Marks m ON s.Id = m.Id
# """)
# print(mycursor.fetchall())

# mycursor.execute("""
#     SELECT Id, AVG(Marks) AS Average_Marks
#     FROM Marks
#     GROUP BY Id
# """)
# print(mycursor.fetchall())

# mycursor.execute("""
#     SELECT Id, SUM(Marks) AS Total_Marks 
#     FROM Marks 
#     GROUP BY Id
# """)
# print(mycursor.fetchall())
# mycursor.execute("""
#     SELECT Id, SUM(Marks) as Total
#     FROM Marks
#     GROUP BY Id
#     HAVING Total>200
# """)
# print(mycursor.fetchall())
# mycursor.execute("""
#     SELECT Age, COUNT(*) AS Count
#     FROM Students_Info
#     GROUP BY Age
#     HAVING Count>1
# """)
# print(mycursor.fetchall())
# mycursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s 
#     INNER JOIN Marks m ON s.Id=m.Id
# """)
# print("Inner Join: ", mycursor.fetchall())
# mycursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     LEFT JOIN Marks m ON s.Id=m.Id
# """)
# print("Left Join: ", mycursor.fetchall())
# mycursor.execute("""
#     SELECT s.Name, m.Subject, m.Marks
#     FROM Students_Info s
#     RIGHT JOIN Marks m ON s.Id=m.Id
# """)
# print("Right Join: ", mycursor.fetchall())

# mycursor.execute("""
#     CREATE TABLE Library(
#         Book_Id INT AUTO_INCREMENT PRIMARY KEY,
#         Title VARCHAR(100)
#         )
# """)
# mycursor.execute("""
#     CREATE TABLE Enrollments(
#         Enrollment_No INT AUTO_INCREMENT PRIMARY KEY,
#         Id INT,
#         C_Id INT,
#         FOREIGN KEY (Id) REFERENCES Students_Info(Id),
#         FOREIGN KEY (C_Id) REFERENCES Courses
#         )
# """)
# mycursor.execute("SELECT MAX(Marks) FROM Marks")
# print(mycursor.fetchone())
# mycursor.execute("""
#     CREATE VIEW Student_Total_Marks AS
#     SELECT s.Name, SUM(m.Marks) AS Total_Marks
#     FROM Students_Info s
#     JOIN Marks m ON s.Id=m.Id
#     GROUP BY s.Name
# """)
# mycursor.execute("""
#     SELECT Id, SUM(Marks) AS Total
#     FROM Marks
#     GROUP BY Id
#     HAVING Total> (SELECT AVG(Marks) * COUNT(DISTINCT Subject) FROM Marks)
# """)
# print(mycursor.fetchall())
# mycursor.execute("""
#     CREATE PROCEDURE insert_student(IN SId INT, IN SName VARCHAR(60), IN SAge INT, IN SGender CHAR(1), IN SDept VARCHAR(100))
#     BEGIN
#                INSERT INTO Students_Info(Id, Name, Age, Gender, Department)
#                VALUES(SId, SName, SAge, SGender, SDept);
#     END
# """)
# mycursor.execute("CALL insert_student(106, 'Ravi', 22, 'M', 'Civil')")
# mydb.commit()
# mycursor.execute("""
#     CREATE PROCEDURE update_dept(IN SId INT, IN NewDept VARCHAR(100))
#     BEGIN
#                UPDATE Students_Info SET Department= NewDept WHERE Id= SId;
#     END
# """)
# mycursor.execute("CALL update_dept(106, 'Mechanical')")
# mydb.commit()
# mycursor.execute("""
#     CREATE FUNCTION calculate_grade(Marks INT) RETURNS VARCHAR(10)
#     DETERMINISTIC
#     RETURN
#             CASE
#                 WHEN Marks>= 90 THEN 'A'
#                 WHEN Marks>= 80 THEN 'B'
#                 WHEN Marks>= 70 THEN 'C'
#                 ELSE 'D'
#             END
# """)
# mycursor.execute("SELECT calculate_grade(87)")
# print(mycursor.fetchone())
# mycursor.execute("""
#     CREATE TABLE Student_Log(
#         Log_Id INT AUTO_INCREMENT PRIMARY KEY,
#         Id INT,
#         Action_Time DATETIME       
#         )
# """)
# mycursor.execute("""
#     CREATE TRIGGER log_insert
#     AFTER INSERT ON Students_Info
#     FOR EACH ROW
#     INSERT INTO Student_Log(Id, Action_Time)
#     VALUES(NEW.Id, NOW())
# """)
# try:
#     mydb.start_transaction()
#     mycursor.execute("UPDATE Students_Info SET Age= Age+1 WHERE Id= 101")
#     mycursor.execute("UPDATE Students_Info SET Age= Age+1 WHERE Id= 102")
#     mydb.commit()
# except:
#     mydb.rollback()
# mycursor.execute("""
#     SELECT Name, COUNT(*) FROM Students_Info
#     GROUP BY Name
#     HAVING COUNT(*) > 1
# """)
# print(mycursor.fetchall())
# mycursor.execute("""
#     CREATE TABLE csv_data(
#         id INT,
#         name VARCHAR(100),
#         score INT       
#         )
# """)
# mycursor.execute("CREATE INDEX Information ON Students_Info(Name)")
# mycursor.execute("""
#     SELECT MAX(Marks) FROM Marks
#     WHERE Marks < (SELECT MAX(Marks) FROM Marks)
# """)
# print(mycursor.fetchone())
# mycursor.execute("DROP TABLE Enrollments")
# mycursor.execute("DROP TABLE Courses")
# mydb.commit()