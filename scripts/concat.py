from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FlightsDataFast") \
    .getOrCreate()

df = spark.read.csv(
    "/teamspace/studios/this_studio/Project/data/csv_flight/report_201*_*.csv",
    header=True,
    inferSchema=True
)

df.coalesce(1).write \
    .option("header", True) \
    .mode("overwrite") \
    .csv("/teamspace/studios/this_studio/Project/data/report_2017_2018")