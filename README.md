# Sales-Store-Project

Problem Statement: 

We have a retail store client which has stores at different locations. Company wants to analyse the profit made by each location and profit made by each individual stores. As an input, we are daily given a raw csv file where in each row of the file contains a transaction.

The columns of the file are 
  1. Store_ID - Unique identifier
  2. Store_Location - this column contains few unwanted characters like !,( + and so on and these need to be removed in the pipeline. 
  3. Product_Category 
  4. Product_ID
  5. MRP - $ sign before the price, which also needs to be removed to perform mathematical operations
  6. CP - Cost price
  7. Discount
  8. SP - Actual selling price
  9. Date - Date of the transaction
  
 
Functionalities of the Data Pipeline:

  1. Read and Clean the input files
  2. Store the cleaned files into Database
  3. Perform aggregation on the tables using SQL queries (Locationwise/Storewise)
  4. Output the result into csv files
  5. Send email notifications

We have used airflow for each of the above tasks and DAGS for basic validations and file tasks.
