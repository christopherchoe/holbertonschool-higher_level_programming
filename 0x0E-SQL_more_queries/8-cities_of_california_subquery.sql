-- lists all cities of california in hbtn_0d_usa
USE hbtn_0d_usa;

SELECT cities.id AS id, cities.name
FROM states, cities
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
