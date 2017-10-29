import pyodbc

def helllo():
    database = "TEST"
    host = "localhost"
    user = "sa"
    pwd = "123"
    conn_info = 'DRIVER={SQL Server};DATABASE=%s;SERVER=%s;UID=%s;PWD=%s'%(database, host, user, pwd)
    conn = pyodbc.connect(conn_info)
    cur = conn.cursor()
    cur.execute("select * from Table_1")
    row =cur.fetchone()
    if row:
        print(row)
