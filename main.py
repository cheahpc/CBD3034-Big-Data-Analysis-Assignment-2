# Task 1: Data Loading and Data Cleaning
# 1.1 Renaming the files
dbutils.fs.mv("/FileStore/tables/T_Data_Cl.csv", "/FileStore/tables/BDA_T_data_Cl.csv")
dbutils.fs.mv("/FileStore/tables/T_Data_C2.csv", "/FileStore/tables/BDA_T_data_C2.csv")
dbutils.fs.mv("/FileStore/tables/T_Data_C3.csv", "/FileStore/tables/BDA_T_data_C3.csv")

# 1.2 cleaning each file
df_c1 = spark.read.csv("dbfs:/FileStore/tables/BDA_T_data_C1.csv", header=True, inferSchema=True)
df_c2 = spark.read.csv("dbfs:/FileStore/tables/BDA_T_data_C2.csv", header=True, inferSchema=True)
df_c3 = spark.read.csv("dbfs:/FileStore/tables/BDA_T_data_C3.csv", header=True, inferSchema=True)
# 1.2.1 Cleaning the first file
# Rename columns


# 1.2.2 Cleaning the second file
# partner yes 0 to partner yes no
# dependents yes 0 to dependents yes no
# phone service yes 0 to phone service yes no
# multiple lines yes 0 0nophoneservice to multiple lines yes no no phone service
# InternetService DSL Fiberoptic 0 to InternetService DSL Fiberoptic No

# 1.2.3 Cleaning the third file
# InternetService DSL Fiberoptic No no to InternetService DSL Fiberoptic No

