CREATE DATABASE DB
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Ukrainian_Ukraine.1251'
    LC_CTYPE = 'Ukrainian_Ukraine.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

DROP TABLE faculties;
DROP TABLE TEACHERS;
DROP TABLE EDUCATIONAL_BUILDINGS;
DROP TABLE "groups";
DROP TABLE AUDIENCES_end_lesson;
drop table question_teacher;
drop table question_EDUCATIONAL_BUILDINGS;


CREATE TABLE faculties(
    NAME_FACULTY character(11) NOT NULL PRIMARY KEY,
    STUDENTS_COUNT bigint,
    TEACHERS_COUNT BIGINT
);

CREATE TABLE TEACHERS(
    PASSPORT_NUMBER character(11) NOT NULL PRIMARY KEY,
    FULL_NAME character(50),
    SALARY bigint,
    FACULTY character(11)
);

CREATE table EDUCATIONAL_BUILDINGS(
    number_BUILDING bigint primary key,
    name_BUILDING character (50)
);

create table groups(
    name_groups character (11) not null primary key ,
    name_FACULTY character(11),
    count_student bigint
);

create table AUDIENCES_end_lesson(
    di_lesson bigint not null primary key,
    number_BUILDING bigint,
    number_audience bigint,
    day_lesson bigint,
    number_lesson bigint,
    PASSPORT_NUMBER_teacher character(11),
    name_group character(11)
);


create table question_teacher(
    TEACHER_PASSPORT_NUMBER character (50),
    count_question int
);



create table question_EDUCATIONAL_BUILDINGS(
    number_EDUCATIONAL_BUILDINGS int,
    count_question int
);


ALTER TABLE question_EDUCATIONAL_BUILDINGS
    ADD CONSTRAINT ss_EDUCATIONAL_BUILDING_FK  FOREIGN KEY (number_EDUCATIONAL_BUILDINGS) REFERENCES EDUCATIONAL_BUILDINGS (number_BUILDING);


ALTER TABLE question_teacher
    ADD CONSTRAINT TEACHER_PASSPORT_NUMBER_FK  FOREIGN KEY (TEACHER_PASSPORT_NUMBER) REFERENCES teachers (PASSPORT_NUMBER);

ALTER TABLE TEACHERS
    ADD CONSTRAINT FACULTY_FK  FOREIGN KEY (FACULTY) REFERENCES faculties (NAME_FACULTY);

ALTER TABLE groups
    ADD CONSTRAINT name_FACULTY_fk  FOREIGN KEY (name_FACULTY) REFERENCES faculties (NAME_FACULTY);

ALTER TABLE AUDIENCES_end_lesson
    ADD CONSTRAINT number_BUILDING_fk  FOREIGN KEY (number_BUILDING) REFERENCES EDUCATIONAL_BUILDINGS (number_BUILDING);

ALTER TABLE AUDIENCES_end_lesson
    ADD CONSTRAINT PASSPORT_NUMBER_teacher_fk  FOREIGN KEY (PASSPORT_NUMBER_teacher) REFERENCES TEACHERS (PASSPORT_NUMBER);

ALTER TABLE AUDIENCES_end_lesson
    ADD CONSTRAINT name_group_fk  FOREIGN KEY (name_group) REFERENCES "groups" (name_groups);
