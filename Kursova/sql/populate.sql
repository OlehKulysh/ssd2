insert into "GROUPS" values('КМ-61');
insert into "GROUPS" values('СС-73');
insert into "GROUPS" values('СБУ-91');


insert into "BUILDINGS" values('1', 'img/K14.png');
insert into "BUILDINGS" values('15', 'img/K14.png');
insert into "BUILDINGS" values('14', 'img/K14.png');

insert into "USERS" values('alex', '111', 'КМ-61', 2016);
insert into "USERS" values('lufar', '111', 'СС-73', 2017);
insert into "USERS" values('god_usop', '111', 'СБУ-91', 2019);

insert into "REQUESTS" values(1, 'alex', '1', 102, '2019-03-14', '21:12:58');
insert into "REQUESTS" values(2, 'lufar', '15', 121, '2019-03-14', '21:12:58');
insert into "REQUESTS" values(3, 'god_usop', '14', 111, '2019-03-14', '21:12:58');

select * from "REQUESTS";