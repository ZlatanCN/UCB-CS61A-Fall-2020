.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price
  FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) AS lowest_price
  FROM inventory
  GROUP BY item;


CREATE TABLE best_deals AS
  SELECT name, MIN(MSRP / rating)
  FROM products
  GROUP BY category;


CREATE TABLE shopping_list AS
  SELECT name, store
  FROM best_deals, lowest_prices
  WHERE name = item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs)
  FROM stores AS a, shopping_list AS b
  WHERE a.store = b.store;
