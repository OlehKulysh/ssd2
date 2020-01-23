create role "Ory" with
	login
	nosuperuser
	createdb
	nocreaterole
	inherit
	replication
	connection limit -1
	valid until '2020-01-31T09:26:10+02:00'
	PASSWORD 'xxxxxx';

create DATABASE "OryDB"
    with
    OWNER = "Ory"
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;


drop table "REQUESTS";
drop table "USERS";
drop table "BUILDINGS";
drop table "GROUPS";

create table "BUILDINGS"(
    "NUMB_BUILDING" character(20),
    "JSON" text,
     constraint "BUILDINGS_PK" primary key ("NUMB_BUILDING")
);

create table "GROUPS"(
    "NAME_GROUP" character(20),
    constraint "NAME_GROUP_PK" primary key ("NAME_GROUP")
);

create table "USERS"(
    "LOGIN" character(20),
    "PASSWORD" character(20),
    "NUMB_GROUP" character(20),
    "YEAR" bigint,
     constraint "USERS_PK" primary key ("LOGIN")
);

create table "REQUESTS"(
    "ID" bigint,
    "LOGIN" character(20),
    "BUILDING" character(20),
    "AUDIENCE" bigint,
    "DATA" date,
    "TIME" time,
     constraint "REQUEST_PK" primary key ("ID")
);

alter TABLE "UPA"."USERS"
    ADD CONSTRAINT NUMB_GROUP_FK  FOREIGN KEY("NUMB_GROUP") REFERENCES "GROUPS" ("NAME_GROUP");

alter TABLE "UPA"."REQUESTS"
    ADD CONSTRAINT LOGIN_FK  FOREIGN KEY("LOGIN") REFERENCES "UPA"."USERS" ("LOGIN");

alter TABLE "UPA"."REQUESTS"
    ADD CONSTRAINT BUILDING_FK  FOREIGN KEY("BUILDING") REFERENCES "BUILDINGS" ("UPA"."NUMB_BUILDING");
