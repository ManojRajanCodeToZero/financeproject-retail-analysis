import sys
from lib import DataReader, DataManipulation, utils
from pyspark.sql.functions import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the environment as an argument: LOCAL/TEST/PROD")
        sys.exit(1)

    job_run_env = sys.argv[1].upper()
    print ("Creating spark session")

    spark = utils.get_spark_session(job_run_env)
    print("Created spark session successfully")

    order_df = DataReader.read_orders(spark, job_run_env)
    orders_filtered = DataManipulation.filter_closed_orders(order_df)
    print("Filtered closed orders")
    customer_df = DataReader.read_customers(spark, job_run_env)

    joined_df = DataManipulation.join_orders_customers(orders_filtered, customer_df)
    print("Joined orders and customers dataframes") 

    aggregated_result = DataManipulation.count_orders_state(joined_df)
    print("Aggregated order counts by state")   

    aggregated_result.show()

    print("Retail analysis job completed successfully")