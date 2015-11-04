/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.

Given a table STATION that holds data for five fields namely ID, CITY, STATE, NORTHERN LATITUDE and WESTERN LONGITUDE.
+-------------+------------+
| Field       |   Type     |
+-------------+------------+
| ID          | INTEGER    |
| CITY        | VARCHAR(21)|
| STATE       | VARCHAR(2) |
| LAT_N       | NUMERIC    |
| LONG_W      | NUMERIC    |
+-------------+------------+
 
Let |city| be the length of the city, write a query to print two lines:
1. First line is city1 and |city1| separated by space, where |city1| is the possible minimum value.
2. Second line is city2 and |city2| separated by space, where |city2|  is the possible maximum value.
If there are more than one possible cities print the lexicographical smallest.
In other words:

Write a query to print shortest and longest cities name. If there are more than one cities print lexicographical smallest name.

Note

If cities names are: DEF, ABC, PQRS and WXYZ. Then the output is:

ABC 3
PQRS 4

*/

select top 1 city, len(city) from station
    order by len(city), city; 
select top 1 city, len(city) from station
    order by len(city) desc, city; 