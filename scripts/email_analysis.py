from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc, regexp_extract

# Step 1: Initialize Spark Session
spark = SparkSession.builder \
    .appName("Enron Email Analysis - Multiline Support") \
    .getOrCreate()

# Step 2: Load the dataset (read as plain text instead of CSV)
data_path = "gs://river-inquiry-440619-n8/emails.csv"
emails_df = spark.read.text(data_path)

# Step 3: Extract 'From' and 'To' using updated regex patterns
emails_df = emails_df.withColumn(
    'From', regexp_extract('value', r'(?i)(From:\s*.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}))', 2)
)
emails_df = emails_df.withColumn(
    'To', regexp_extract('value', r'(?i)(To:\s*.*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}))', 2)
)

# Step 4: Filter out rows with NULL or empty From and To values
emails_df = emails_df.filter((col("From").isNotNull()) & (col("To").isNotNull()))
emails_df = emails_df.filter((col("From") != "") & (col("To") != ""))

# Step 5: Count total number of emails
total_emails = emails_df.count()
print(f"Total number of valid emails: {total_emails}")

# Step 6: Get top 10 senders
top_senders = emails_df.groupBy("From").count().orderBy(desc("count"))
top_senders.show(10)

# Step 7: Count email communication frequencies between senders and recipients
communication_frequency = emails_df.groupBy("From", "To").count().orderBy(desc("count"))
communication_frequency.show(10)

# Step 8: Save the output results to GCS
output_path = "gs://river-inquiry-440619-n8/output/email_analysis_results"
communication_frequency.write.csv(output_path, mode="overwrite")

# Step 9: Stop the Spark session
spark.stop()
