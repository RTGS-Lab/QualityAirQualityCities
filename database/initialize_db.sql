-- Run this file to initialize the database, schema, and tables for PurpleAir Monitor Readings in Minneapolis
-- You can run this by using a psql command like:
-- psql "host=postgres.cla.umn.edu user=<your_username> password=<your_password> " -f initialize_db.sql

CREATE DATABASE "MplsCommunityAir"; -- Create the database


-- Connect to database This needs a password!

\c "MplsCommunityAir";

CREATE SCHEMA "PurpleAir"; -- Create Schema

CREATE EXTENSION postgis; -- Add spatial extensions
CREATE EXTENSION postgis_topology;
CREATE EXTENSION postgis_raster; --add raster extension

CREATE TABLE Minneapolis_Boundary
(
    CTU_ID int,
    CTU_NAME text,
    CTU_CODE text,
    geometry geometry
);

CREATE TABLE MPCA_Facilities -- Create table to store information on each facility
(
    FACILITY_ID int, -- Unique identifier
    FACILITY_NAME text,
    INDUSTRY_TYPE text, -- (from last report, will be list string)
    NAICS_CODE text, -- a code to classify industry (from last report, will be list string)
    COUNTY text,
    LAST_REPORT int, -- last year of submission
    geometry geometry
);

CREATE TABLE MPCA_Facilities_HOLD -- facilities with Quality issues
(
    FACILITY_ID int, -- Unique identifier
    Error_Codes text -- Descriptor on the issue(s) with the facility (list string)
);

CREATE TABLE MPCA_Permitted_Emissions -- Create table to store historic facility emissions
(
    FACILITY_ID int, -- Unique identifier
    YEAR int, 
    POLLUTANT text,
    LBS_EMITTED float
);

CREATE TABLE MNDOT_Current_AADT_Segments -- Create table to store information on Current AADT segments
( 
    SEQUENCE_NUMBER int, -- Unique identifier
    ROUTE_LABEL text,
    STREET_NAME text,
    DAILY_FACTOR text,
    SEASONAL_FACTOR text,
    AXLE_FACTOR text,
    CURRENT_YEAR int,
    CURRENT_VOLUME int,
    geometry geometry
);

CREATE TABLE MPLSZoning -- Ethan work
(
    ZONE_CODE text, 
    ERROR_CODE text,
    geometry geometry
);

CREATE TABLE WIND_HISTORIC --create table to historic NOAA data
(
	STATION VARCHAR(255),
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    DATE DATE,
    MONTH INT,
    DAY INT,
    HOUR INT,
    HLY_WIND_AVGSPD FLOAT,
    HLY_WIND_VCDIR FLOAT,
    ERROR_WINDSPD INT,
    ERROR_WINDVCTR INT,
    WIND_INTENSITY INT,
    WIND_VCT_CATEGORY INT,
    WKT geometry
);

CREATE TABLE PURPLEAIR_STATIONS
(
	sensor_index int,
	last_modified int, 
	date_created int,
	last_seen int, 
	name varchar(100),
	location_type int, 
	firmware_version varchar(30),
	uptime int,
	position_rating int,
	latitude float,
	longitude float,
	altitude int,
	channel_state int,
	channel_flags int,
	WKT geometry
);

CREATE TABLE PURPLEAIR_REALTIME
(
    sensor_index int,
    timestamp timestamp,
    humidity int, 
    temperature int,
    pressure float,
    pm2_5 float,
);

CREATE TABLE PURPLEAIR_REALTIME_ERRORS
(
    sensor_index int,
    timestamp timestamp,
    humidity_error text,
    temperature_error text,
    pressure_error text,
    pm2_5 text
);

CREATE TABLE PURPLEAIR_HISTORIC
(
    sensor_index int,
    timestamp timestamp,
    humidity int, 
    temperature int,
    pressure float,
    pm2_5 float,
);

CREATE TABLE PURPLEAIR_HISTORIC_ERRORS
(
    sensor_index int,
    timestamp timestamp,
    humidity_error text,
    temperature_error text,
    pressure_error text,
    pm2_5 text
);

-- CREATE TABLE PurpleAir.:MplsPurpleAirSensors -- Create table to store information on each sensor
-- (
--     sensor_id serial, -- Unique identifier
-- 	custodian_type text, -- Volunteer, business, MPRB (Parks & Rec), etc.
-- 	hardware text, -- info on hardware & model
-- 	firmware text, -- info on firmware
-- 	date_created date, -- Date of creation
-- 	last_modified date, -- Last time maintained
-- 	last_seen timestamp [ 0 ], -- last data submission
-- 	active bool, -- 0 means no longer active, 1 means active
-- 	altitude double precision,
-- 	geom geometry
-- );
-- 
-- CREATE TABLE PurpleAir.:MplsPurpleAirHistoric -- Create table to store historic readings
-- (
--     sensor_id int, -- Unique identifier
--     timestamp timestamp [ 0 ], -- Timestamp
--     a_sensor_reading float, --
--     a_sensor_error_flag bool,
--     b_sensor_reading float,
--     b_sensor_error_flag bool,
--     temperature float,
--     relative_humidity float
-- );
