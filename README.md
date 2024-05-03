assignment repo:
======================
   data - Input data
   output - Transformed Output
   src - pyspark code

# Step 1: Set Up Development Environment
Clone the Repo https://github.com/AKPAKUR/assignment
`cd assignment`
`chmod 755 ./setup.sh`
`./setup.sh` 
This will create the pyspark virtual env

# Step 2: Run ETL
steps:
    Read csv from data directory
    Transformation
    save data in output directory

`python '/home/abhi/projects/assignment/src/etl.py`


# Step 3: Create Dockerfile
Create a Dockerfile to package your PySpark script and its dependencies:
`
FROM pyspark/pyspark:latest
COPY src/etl.py /etl.py
CMD ["spark-submit", "/etl.py"]

`

# Step 4: Build Docker Image
`docker build -t etl_pipeline .`

# Step 5: Run ETL Process in Docker Container
`docker run --rm -v $(pwd):/data etl_pipeline`

# Step 6: Verify Data in Delta Table is correct
There should be 5 lines of data in the output Parquet file
