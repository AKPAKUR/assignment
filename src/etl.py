from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

# Read data from CSV
df = spark.read.csv(r"./data/data.csv", header=True, inferSchema=True)

# Apply transformation: calculate total order amount by each customer
df_transformed = df.groupBy("customer_id").agg(sum("order_amount").alias("customer_total_order_amt"))

# Path to the output Parquet file
output_path = r"./output/output_data.parquet"

# Write transformed data to Delta Table
#df_transformed.write.format("delta").save("/home/abhi/projects/assignment/output")

# Write DataFrame to Parquet using to_parquet method
df_transformed.write.format("parquet").mode("overwrite").save(output_path)

# Define Delta table schema
schema = "customer_id INT, customer_total_order_amt INT"

# Create table name
table_name = "Delta_table"

# Spark SQL
spark.sql(f"CREATE TABLE {table_name} ({schema}) USING parquet LOCATION '/home/abhi/projects/assignment/output/output_data.parquet' ")


# Stop SparkSession
spark.stop()
