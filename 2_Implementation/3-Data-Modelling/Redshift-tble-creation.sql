CREATE TABLE transaction_facts (
    user_id VARCHAR(50),
    total_page_views INT,
    total_transaction_amount FLOAT,
    PRIMARY KEY (user_id)
);

CREATE TABLE user_dim (
    user_id VARCHAR(50) PRIMARY KEY,
    user_name VARCHAR(100),
    user_email VARCHAR(100)
);

CREATE TABLE product_dim (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name VARCHAR(100),
    product_price FLOAT
);

CREATE TABLE date_dim (
    date_id DATE PRIMARY KEY,
    day INT,
    month INT,
    year INT
);

CREATE TABLE campaign_dim (
    campaign_id VARCHAR(50) PRIMARY KEY,
    campaign_name VARCHAR(100),
    campaign_type VARCHAR(50)
);
