-- Write all sql commands here, write comments for all of them too

CREATE DATABASE maximumdb;
USE maximumdb;

create table maximum(
    Date text,
    Temperature double,
    Station varchar(100)
)

create table minimum(
    Date text,
    Temperature double,
    Station varchar(100)
)

-- i used table data import wizard to import the data from the csv file


-- the below command gives the top 5 maximum temperatures
SELECT Date, Temperature , Station
FROM maximum 
ORDER BY Temperature DESC 
LIMIT 5;

-- the below command gives the top 5 minimum temperatures
SELECT Date, Temperature , Station
FROM minimum
ORDER BY Temperature ASC
LIMIT 5;

-- the below gives average temperature for each station
SELECT Station, AVG(Temperature) AS Avg_Temperature
FROM (
    SELECT Station, Temperature FROM maximum
    UNION ALL
    SELECT Station, Temperature FROM minimum
) AS combined_data
GROUP BY Station
ORDER BY Avg_Temperature DESC;

-- the below gives the maximum temperature for each station
SELECT t1.Station, t1.Date, t1.Temperature
FROM maximum t1
WHERE t1.Temperature = (
    SELECT MAX(t2.Temperature) FROM maximum t2 
    WHERE t2.Station = t1.Station
);

-- the below gives the minimum temperature for each station
SELECT t1.Station, t1.Date, t1.Temperature
FROM minimum t1
WHERE t1.Temperature = (
    SELECT MIN(t2.Temperature) FROM minimum t2 
    WHERE t2.Station = t1.Station
);
