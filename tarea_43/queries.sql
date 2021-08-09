SQL_1:
SELECT FirstName, FamilyName, Email, LastAccess, Post
FROM users;

SQL_2:
SELECT *
FROM subscribers;

SQL_3:
SELECT GivenName, Email
FROM mailing_list;

SQL_4:
SELECT Username, FullName, MailingAddress
FROM mailing_list;

SQL_5:
SELECT DISTINCT FullName
FROM members;

SQL_6:
SELECT *
FROM members
ORDER BY FullName ASC;

SQL_7:
SELECT *
FROM subscribers
ORDER BY PasswordHash DESC;