from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("PySparkBasics").getOrCreate()
df = spark.read.csv("sales.csv", header=True, inferSchema=True)
df.show()
# Add new column 'tax' as 10% of amount
df_with_tax = df.withColumn("tax", col("amount") * 0.1)
df_with_tax.show()
df.show()
print(df.columns)
df.orderBy(col("region").asc(), col("amount").desc()).show()
df.filter(col("amount")> 1000).show()
df.filter((col('region') == 'South')).show()
df.filter((col("region")=='North')).show()
df.show()
df.select("name","amount").show()
# Rename a column
df_renamed = df.withColumnRenamed("amount","amounts")
df_renamed.show()
# # Drop a column
# df_dropped =df.drop("region")
# df_dropped.show()
df_with_category = df.withColumn(
    "category",
    when(col("amount") > 1000, "High").otherwise("Low")
)
df_with_category.show()

print("Row count:", df.count())
print("Distinct regions:", df.select("region").distinct().count())

df_with_category.filter(col("category") == "High") \
    .write.csv("output_high_sales", header=True)

    df_with_category.groupBy("region", "category").sum("amount").show()
