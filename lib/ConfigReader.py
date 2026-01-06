import configparser
from pyspark import SparkConf


## Loading application config in python dictionary
def get_app_config(env: str) -> dict:
    config = configparser.ConfigParser()
    config.read('configs/application.conf')
    app_conf = {}
    for(key,value) in config.items(env):
        app_conf[key] = value
    return app_conf

## Loading spark config in SparkConf object
def get_pyspark_config(env: str) -> SparkConf:
    config = configparser.ConfigParser()
    config.read('configs/spark.conf')
    pyspark_config=SparkConf()
    for (key,value) in config.items(env):
        pyspark_config.set(key,value)
    return pyspark_config