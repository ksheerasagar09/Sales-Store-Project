select date, store_location, round(sum(SP) - sum(CP)) as location_profit 
from store_data_daily
group by date, store_location
order by location_profit desc
into outfile "/store_files_mysql/loc_wise_profit_agg.csv"
fields terminated by ","
lines terminated by "\n";


select date, store_id, round(sum(SP) - sum(CP)) as store_profit 
from store_data_daily
group by date, store_id
order by store_profit desc
into outfile "/store_files_mysql/store_wise_profit_agg.csv"
fields terminated by ","
lines terminated by "\n";