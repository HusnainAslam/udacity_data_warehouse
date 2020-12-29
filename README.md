# Data Warehouse - Using Redshift

## Project Overview
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.


## SCHEMA

### Staging Tables
**tbl_events_stg** - Stage table to load data from logs files.
- artist VARCHAR,
- auth VARCHAR,
- firstName VARCHAR,
- gender VARCHAR,
- itemInSession INTEGER,
- lastName VARCHAR,
- length VARCHAR,
- level VARCHAR,
- location VARCHAR,
- method VARCHAR,
- page VARCHAR,
- registration FLOAT,
- sessionId INTEGER,
- song VARCHAR,
- status INTEGER,
- ts BIGINT,
- userAgent VARCHAR,
- userId INTEGER

**tbl_songs_stg** - Stage table to load data from songs data files.
- song_id VARCHAR,
- title VARCHAR,
- artist_id VARCHAR,
- artist_name VARCHAR,
- artist_latitude FLOAT,
- artist_longitude FLOAT,
- artist_location VARCHAR,
- duration FLOAT,
- year INTEGER,
- num_songs FLOAT,

### Fact Table
**tbl_songplays** - Records in log data associated with song plays i.e. records with page NextSong)
- songplay_id IDENTITY(0,1) PRIMARY KEY, _(uniquely indentifies a song play)_
- start_time TIMESTAMP, _(start time of user song play. Foriegn key of time table)_
- user_id INTEGER,
- level VARCHAR,
- song_id VARCHAR,
- artist_id VARCHAR,
- session_id INTEGER,
- location VARCHAR INTEGER,
- user_agent VARCHAR INTEGER

### Dimension Tables
**tbl_user**  - users in the app
- user_id INTEGER PRIMARY KEY,
- first_name VARCHAR, 
- last_name VARCHAR,
- gender VARCHAR,
- level VARCHAR

**tbl_song**  - songs in music database
- song_id VARCHAR PRIMARY KEY, 
- title VARCHAR, 
- artist_id VARCHAR, 
- year INTEGER, 
- duration FLOAT _(Duration of the song in milliseconds)_

**tbl_artist**  - artists in music database
- artist_id VARCHAR PRIMARY KEY, 
- name VARCHAR, 
- location VARCHAR, 
- latitude FLOAT, 
- longitude FLOAT

**tbl_time**  - timestamps of records in  **songplays**  broken down into specific units
- start_time TIMESTAMP PRIMARY KEY, 
- hour INTEGER, 
- day INTEGER, 
- week INTEGER, 
- month INTEGER, 
- year INTEGER, 
- weekday INTEGER


## RUN
- Add cluster, IAM role info in `dwh.cfg` 
- Run `python create_tables.py` to create table
- Run `python etl.py` to load staging table and populate data in Analytical table

## Description of Files
`sql_queries.py` contains all sql queries<br>
`create_tables.py` Drop all tables if exists and Create all tables. Run this to reset tables<br>
`etl.py` Pipeline to load data from s3 to staging and transform it to populate analytical tables.<br>
`dwh.cfg` Hold configuration info of Redshift cluster, IAM role and s3 buckets.<br>
