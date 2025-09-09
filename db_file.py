import sqlite3
import pandas as pd

conn = sqlite3.connect('STAFF.db')

table_name = 'Departments'
attribute_list = ['DEPT_ID','DEP_NAME','MANAGER_ID','LOC_ID']

file_path = '/home/project/Departments.csv'
df = pd.read_csv(file_path, names=attribute_list)

df.to_sql(table_name, conn, if_exists='replace', index=False)
print("table is ready")

# Append one row
data_dict = {
    'DEPT_ID': 9,
    'DEP_NAME': 'Quality Assurance',
    'MANAGER_ID': 30010,
    'LOC_ID': 'L0010'
}

data_append = pd.DataFrame([data_dict])
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print('Data appended successfully')

# a) View all entries
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# b) View only department names
query_statement = f"SELECT DEP_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# c) Count total entries
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()
