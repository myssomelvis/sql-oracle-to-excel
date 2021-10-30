import cx_Oracle 
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir=r"C:\instantclient-basic-nt-21.3.0.0.0")

dsn_tns = cx_Oracle.makedsn('localhost', '2020', service_name='SID_TEST') 
conn = cx_Oracle.connect(user='root', password='root', dsn=dsn_tns) 

query = "select * from client"
dfs = []
for chunk in pd.read_sql_query(query, con=conn, chunksize=1000):
	dfs.append(chunk)
df = pd.concat(dfs)

print(f"nombre de ligne ---> {len(df)} ")
df.to_excel('my_oracle_table.xlsx',engine='xlsxwriter')
conn.close()
