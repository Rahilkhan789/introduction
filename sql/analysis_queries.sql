-- Entry-level SQL questions for the retail sales project

-- 1) Total revenue
SELECT ROUND(SUM(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS total_revenue
FROM sales_data;

-- 2) Average order value
SELECT ROUND(AVG(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS average_order_value
FROM sales_data;

-- 3) Revenue by category
SELECT
  category,
  ROUND(SUM(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS revenue
FROM sales_data
GROUP BY category
ORDER BY revenue DESC;

-- 4) Revenue by city
SELECT
  city,
  ROUND(SUM(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS revenue
FROM sales_data
GROUP BY city
ORDER BY revenue DESC;

-- 5) Channel performance
SELECT
  channel,
  ROUND(SUM(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS revenue,
  COUNT(*) AS order_count
FROM sales_data
GROUP BY channel
ORDER BY revenue DESC;

-- 6) Top 5 products by revenue
SELECT
  product,
  ROUND(SUM(units_sold * unit_price * (1 - discount_pct / 100.0)), 2) AS revenue
FROM sales_data
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;
