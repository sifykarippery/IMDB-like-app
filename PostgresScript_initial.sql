username:- imdb_user
password:- Password@123


CREATE ROLE imdb_user LOGIN
  ENCRYPTED PASSWORD 'md5e96ff20676ddae46e80280c8bf4a111a'
  SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION CONNECTION LIMIT 250;
GRANT pg_signal_backend TO imdb_user;

CREATE DATABASE "IMDBDev"
  WITH ENCODING='UTF8'
       OWNER=imdb_user
       CONNECTION LIMIT=-1;

      
       CREATE TABLE profile(
   id SERIAL PRIMARY KEY,
   firstname VARCHAR (50),
   lastname VARCHAR (50),
   dob Date,
   address VARCHAR(50)
);

INSERT INTO Profiles(firstname,lastname,dob,address)
VALUES
('Mayavi','Mathrikan','12-3-1889','mayavihouse'),
('Dakini','Mathrikan','3-4-1889','kuttichathanhouse'),
('Kutusan','Mathrikan','12-1-1838','kuttichathanhouse'),
('Luttappi','Mathrikan','11-3-1889','kuttichathanhouse'),
('Raju','Rada','10-7-1889','mayavihouse');

CREATE TABLE Movies(
   id SERIAL PRIMARY KEY,
   moviename VARCHAR (50),
   releasedate Date,
   budget MONEY,
   collection MONEY,
   description TEXT
);