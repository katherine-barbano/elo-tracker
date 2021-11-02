-- Feel free to modify this file to match your development goal.
-- Here we only create 3 tables for demo purpose.
Drop Table Rankables;
Drop Table Users;
Drop Table Products;
Drop Table Purchases;
Drop Table League;
Drop Table Activity;
Drop Table Matches;

CREATE TABLE Users (
    id INT GENERATED BY DEFAULT AS IDENTITY,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL
);

CREATE TABLE Products (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    price FLOAT NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE Purchases (
    id INT NOT NULL PRIMARY KEY,
    uid INT NOT NULL,
    pid INT NOT NULL,
    time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC')
);

CREATE TABLE League (
    l_id VARCHAR(255) NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    president VARCHAR(255) NOT NULL
);

CREATE TABLE Member_of (
    l_id VARCHAR(255) NOT NULL,  -- REFERENCES League.l_id (schema "league" does not exist)
    user_id VARCHAR(255) NOT NULL, --  REFERENCES Users.id
    status VARCHAR(255) NOT NULL,
    PRIMARY KEY (l_id, user_id)
);

CREATE TABLE Matches (
    activity VARCHAR(255) NOT NULL,
    matchID INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    user1_ID INT NOT NULL,
    user2_ID INT NOT NULL,
    user1_score INT,
    user2_score INT,
    date_time TIMESTAMP NOT NULL
);

CREATE TABLE Activity (
    name VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE Rankables (
    rankable_id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    category VARCHAR NOT NULL,
    about VARCHAR NOT NULL
);
