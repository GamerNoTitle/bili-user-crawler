import pymysql as sql
def init(address,database,username,password):
    connection=sql.connect(address,user=username,passwd=password,db=database)
    return connection

def execute(connection,command):
    cursor=connection.cursor()
    cursor.execute(command)
    cursor.close()