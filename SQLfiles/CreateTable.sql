CREATE TABLE IF NOT EXISTS store_data_daily
    (STORE_ID VARCHAR(255), 
    STORE_LOCATION VARCHAR(255),
    PRODUCT_CATEGORY VARCHAR(255), 
    PRODUCT_ID INT, 
    MRP float ,
    CP float, 
    DISCOUNT float,
    SP float, 
    DATE date);
