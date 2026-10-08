CREATE TABLE fact_analysis (
    id INT,
    company_id TEXT,
    sales_value FLOAT,
    profit_value FLOAT,
    stock_cagr FLOAT,
    roe_value FLOAT
);

SELECT * FROM fact_analysis;
DROP TABLE fact_analysis;