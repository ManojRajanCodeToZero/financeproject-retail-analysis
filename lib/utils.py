from pyspark.sql import SparkSession
from lib.ConfigReader import get_app_config, get_pyspark_config

def get_spark_session(env: str) -> SparkSession:
    if env == "LOCAL":
        return SparkSession.builder \
        .config(conf=get_pyspark_config(env)) \
        .master("local[*]") \
        .getOrCreate()
    else:
        return SparkSession.builder \
        .config(conf=get_pyspark_config(env)) \
        .enableHiveSupport() \
        .getOrCreate()