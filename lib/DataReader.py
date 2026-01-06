from lib import ConfigReader


##Get Customer schema
def getCustomerSchema():
    schema = "customer_id int, customer_fname string, cystomer_lname string, username string, password string, address string," \
    "city string, state string,pincode string"
    return schema

## Creating customers dataframe
def read_customers(spark, env: str):
    conf = ConfigReader.get_app_config(env)
    customer_file_path = conf['customer.file.path']
    return spark.read \
        .format("csv") \
        .option("header","true") \
        .schema(getCustomerSchema()) \
        .load(customer_file_path)

## Get Orders schema
def getOrdersSchema():
    schema = "order_id int, order_date string, customer_id int, order_status string"
    return schema

## Creating orders dataframe
def read_orders(spark,env: str):
    conf = ConfigReader.get_app_config(env)
    order_file_path = conf['order.file.path']
    return spark.read \
    .format("csv") \
    .option("header","true") \
    .schema(getOrdersSchema()) \
    .load(order_file_path)