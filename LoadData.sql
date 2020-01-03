LOAD DATA INFILE '/store_files_mysql/cleaned_store_data.csv' 
INTO TABLE store_data_daily 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;