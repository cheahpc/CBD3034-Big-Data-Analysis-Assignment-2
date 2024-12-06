1. Import the following into Databricks as new notebook
    1. output/CDB3034_A2_Task1.dbc
    2. output/CDB3034_A2_Task2.dbc

2. Import the following into Databricks as new tables
    1. data/T_Data_C1.csv
    2. data/T_Data_C2.csv
    3. data/T_Data_C3.csv

3. *Task 1 has to be manually executed until step 5.

4. Task 2 can be executed automatically via "Run All" option.

* For task 1:
1. In step 6, to successfully execute the cell, the file source of the line 3 need to change to the generated file from step 5.
    Essentially, replacing line 3 - dbutils.fs.mv source file
    to the csv file generated, shown in the result of step 5
