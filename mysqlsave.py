import pymysql as sql
def init(address,database,username,password):
    connection=sql.connect(address,user=username,passwd=password,db=database)
    return connection