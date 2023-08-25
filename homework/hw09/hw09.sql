CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs, sizes
  WHERE height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT cd.name
  FROM dogs AS cd,
       parents AS p,
       dogs AS pd
  WHERE cd.name = p.child AND pd.name = p.parent
  ORDER BY -pd.height;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT first.name AS first_dog,
         second.name AS second_dog,
         first.size AS same_size
  FROM size_of_dogs AS first,
       size_of_dogs AS second,
       parents AS fir,
       parents AS sec
  WHERE first.name < second.name
    AND fir.child = first.name
    AND sec.child = second.name
    AND fir.parent = sec.parent
    AND first.size = second.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || first_dog || ' plus ' || second_dog || ' have the same size: ' || same_size
  FROM siblings;

