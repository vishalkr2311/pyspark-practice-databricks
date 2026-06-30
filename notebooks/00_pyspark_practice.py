# Databricks notebook source
# DBTITLE 1,Create Sample Employee Data
from pyspark.sql import SparkSession

data = [
    (101, "John", "IT", 65000),
    (102, "Alice", "HR", 55000),
    (103, "Bob", "Finance", 70000),
    (104, "David", "IT", 80000),
    (105, "Emma", "HR", 60000),
    (106, "Chris", "Finance", 75000),
    (107, "Sophia", "IT", 90000),
    (108, "James", "Marketing", 50000)
]

columns = ["emp_id","name","department","salary"]

df = spark.createDataFrame(data, columns)

df.show()

# COMMAND ----------

# DBTITLE 1,Basic Exploration
df.printSchema()
df.columns
df.count()
df.describe().show()


# COMMAND ----------

# DBTITLE 1,Select Columns
df.select("name", "salary").show()


# COMMAND ----------

# DBTITLE 1,Filter
df.filter(df.salary > 70000).show()

from pyspark.sql.functions import col
df.filter(col("salary") > 70000).show()

# COMMAND ----------

# DBTITLE 1,Multiple Conditions
df.filter(
    (col("department")=="IT") &
    (col("salary")>70000)
).show()

# COMMAND ----------

# DBTITLE 1,Add New Column(Increase salary by 10%)
from pyspark.sql.functions import col

df_new = df.withColumn(
    "new_salary",
    col("salary")*1.10
)

df_new.show()

# COMMAND ----------

# DBTITLE 1,Rename Column
df.withColumnRenamed("department","dept").show()

# COMMAND ----------

# DBTITLE 1,Sort Data(Highest salary first)
df.orderBy(col("salary").desc()).show()

# COMMAND ----------

# DBTITLE 1,Group By  (Average salary by department)
from pyspark.sql.functions import avg

df.groupBy("department") \
    .agg(avg("salary").alias("avg_salary")) \
        .show()

# COMMAND ----------

# DBTITLE 1,Register Temp View
df.createOrReplaceTempView("employees")

# COMMAND ----------

# DBTITLE 1,Spark SQL (Show all employees, IT Employees, Department-wise Average Salary, Highest Salaries)
# MAGIC %sql
# MAGIC
# MAGIC select * 
# MAGIC from employees;
# MAGIC
# MAGIC select *
# MAGIC from employees
# MAGIC order by salary desc;
# MAGIC
# MAGIC select department,
# MAGIC avg(salary) as avy_salary
# MAGIC from employees
# MAGIC group by department;
# MAGIC
# MAGIC select *
# MAGIC from employees
# MAGIC order by salary desc
# MAGIC limit 3;

# COMMAND ----------

