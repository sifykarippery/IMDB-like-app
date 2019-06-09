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

----------------------------------------------------- TABLE CREATION --------------------------------------------------------------

 -- Table: public.profiles

-- DROP TABLE public.profiles;

CREATE TABLE public.profiles
(
  id integer NOT NULL DEFAULT nextval('profiles_id_seq'::regclass),
  firstname character varying(50),
  lastname character varying(50),
  dob date,
  address character varying(50),
  CONSTRAINT profiles_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.profiles
  OWNER TO odoo12;

-- Table: public.movies

-- DROP TABLE public.movies;

CREATE TABLE public.movies
(
  id integer NOT NULL DEFAULT nextval('movies_id_seq'::regclass),
  moviename character varying(50),
  releasedate date,
  budget money,
  collection money,
  description text,
  CONSTRAINT movies_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.movies
  OWNER TO odoo12;

-- Table: public.actors

-- DROP TABLE public.actors;

CREATE TABLE public.actors
(
  id integer NOT NULL DEFAULT nextval('actors_id_seq'::regclass),
  profileid integer,
  note character varying(50),
  CONSTRAINT actors_pkey PRIMARY KEY (id),
  CONSTRAINT actors_profileid_fkey FOREIGN KEY (profileid)
      REFERENCES public.profiles (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.actors
  OWNER TO odoo12;

-- Table: public.directors

-- DROP TABLE public.directors;

CREATE TABLE public.directors
(
  id integer NOT NULL DEFAULT nextval('directors_id_seq'::regclass),
  note text,
  profileid integer,
  CONSTRAINT directors_pkey PRIMARY KEY (id),
  CONSTRAINT directors_profileid_fkey FOREIGN KEY (profileid)
      REFERENCES public.profiles (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.directors
  OWNER TO odoo12;

-- Table: public.producers

-- DROP TABLE public.producers;

CREATE TABLE public.producers
(
  id integer NOT NULL DEFAULT nextval('producers_id_seq'::regclass),
  note text,
  profileid integer,
  CONSTRAINT producers_pkey PRIMARY KEY (id),
  CONSTRAINT producers_profileid_fkey FOREIGN KEY (profileid)
      REFERENCES public.profiles (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.producers
  OWNER TO odoo12;

-- Table: public.movieactors

-- DROP TABLE public.movieactors;

CREATE TABLE public.movieactors
(
  id integer NOT NULL DEFAULT nextval('movieactors_id_seq'::regclass),
  actorid integer,
  movieid integer,
  CONSTRAINT movieactors_pkey PRIMARY KEY (id),
  CONSTRAINT movieactors_actorid_fkey FOREIGN KEY (actorid)
      REFERENCES public.actors (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT movieactors_movieid_fkey FOREIGN KEY (movieid)
      REFERENCES public.movies (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.movieactors
  OWNER TO odoo12;

-- Table: public.moviedirectors

-- DROP TABLE public.moviedirectors;

CREATE TABLE public.moviedirectors
(
  id integer NOT NULL DEFAULT nextval('moviedirectors_id_seq'::regclass),
  directorid integer,
  movieid integer,
  CONSTRAINT moviedirectors_pkey PRIMARY KEY (id),
  CONSTRAINT moviedirectors_directorid_fkey FOREIGN KEY (directorid)
      REFERENCES public.directors (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT moviedirectors_movieid_fkey FOREIGN KEY (movieid)
      REFERENCES public.movies (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.moviedirectors
  OWNER TO odoo12;

-- Table: public.movieproducers

-- DROP TABLE public.movieproducers;

CREATE TABLE public.movieproducers
(
  id integer NOT NULL DEFAULT nextval('movieproducers_id_seq'::regclass),
  producerid integer,
  movieid integer,
  CONSTRAINT movieproducers_pkey PRIMARY KEY (id),
  CONSTRAINT movieproducers_movieid_fkey FOREIGN KEY (movieid)
      REFERENCES public.movies (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE,
  CONSTRAINT movieproducers_producerid_fkey FOREIGN KEY (producerid)
      REFERENCES public.producers (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.movieproducers
  OWNER TO odoo12;




