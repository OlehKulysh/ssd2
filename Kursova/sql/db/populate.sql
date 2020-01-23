

insert into faculties values ('RTF', 30, 61);
insert into faculties values ('FEL', 40, 71);
insert into faculties values ('IPSA', 60, 100);

insert into techers values (123456, 'Ivanov Ivan Ivanovich', 100000, 'RTF');
insert into techers values (654321, 'Ivanov Ivan Petrov', 120000, 'FEL');
insert into techers values (987654, 'Ivanov Oleh Ivanovich', 80000, 'IPSA');

insert into educational_buildings values (15, 'SBU');
insert into educational_buildings values (13, 'CRU');
insert into educational_buildings values (17, 'SS');

insert into groups values ('km-32', 'RTF', 25);
insert into groups values ('kr-42', 'RTF', 26);
insert into groups values ('wm-15', 'RTF', 35);

insert into AUDIENCES_end_lesson values (1, 15, 25, 4, 4, 123456, 'km-32');
insert into AUDIENCES_end_lesson values (2, 13, 45, 3, 4, 654321, 'kr-42');
insert into AUDIENCES_end_lesson values (3, 17, 92, 5, 4, 987654, 'wm-15');

insert into question_teacher values (123456, 0);
insert into question_teacher values (654321, 0);
insert into question_teacher values (987654, 0);

insert into question_EDUCATIONAL_BUILDINGS values (15, 0);
insert into question_EDUCATIONAL_BUILDINGS values (13, 0);
insert into question_EDUCATIONAL_BUILDINGS values (17, 0);