
def csv_cleaner():
	import pandas as pd
	import re

	df = pd.read_csv("~/store_files_airflow/raw_store_transactions.csv")

	def cleanstore_loc(data):
	    return re.sub('[^\w\s]','', data)

	def cleanmetrics(data):
		return float(data.replace("$",""))

	def cleanproductid(data):
	    return re.sub('[\D]','', data)

	df["PRODUCT_ID"] = df["PRODUCT_ID"].map(lambda x : cleanproductid(x))
	    
	df["STORE_LOCATION"] = df["STORE_LOCATION"].map(lambda x : cleanstore_loc(x))

	metriclist = ["MRP","CP","DISCOUNT","SP"]

	for column in metriclist:
	    df[column] = df[column].map(lambda x : cleanmetrics(x))

	df.to_csv("~/store_files_airflow/cleaned_store_data.csv",index = False)
