

import pyodbc 
sql_conn = pyodbc.connect("Driver={SQL Server};Server=serverName;UID=UserName;PWD=Password;Database=sql_db;")
df_sql = pd.read_sql_query('type your sql query here', sql_conn)
df_sql.head()
