-- Run this file to initialize the database, schema, and tables for PurpleAir Monitor Readings in Minneapolis
-- You can run this by using a psql command like:
-- psql "host=postgres.cla.umn.edu user=<your_username> password=<your_password> " -f initialize_db.sql

CREATE DATABASE "MplsCommunityAir"; -- Create the database

\c MplsCommunityAir; -- Connect to database

CREATE SCHEMA PurpleAir; -- Create Schema

CREATE EXTENSION postgis; -- Add spatial extensions
CREATE EXTENSION postgis_topology;

CREATE TABLE PurpleAir.MplsPurpleAirSensors -- Create table to store information on each sensor
(
    sensor_id serial, -- Unique identifier
	custodian_type text, -- Volunteer, business, MPRB (Parks & Rec), etc.
	hardware text, -- info on hardware & model
	firmware text, -- info on firmware
	date_created date, -- Date of creation
	last_modified date, -- Last time maintained
	last_seen timestamp [ 0 ], -- last data submission
	active bool, -- 0 means no longer active, 1 means active
	altitude double precision,
	geom geometry
);

CREATE TABLE PurpleAir.MplsPurpleAirHistoric -- Create table to store historic readings
(
    sensor_id int, -- Unique identifier
    timestamp timestamp [ 0 ], -- Timestamp
    a_sensor_reading float, --
    a_sensor_error_flag bool,
    b_sensor_reading float,
    b_sensor_error_flag bool,
    temperature float,
    relative_humidity float
);
