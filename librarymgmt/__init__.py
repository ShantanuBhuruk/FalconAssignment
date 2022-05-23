from sqlobject.mysql import builder

MySQLConnection = builder()
conn = MySQLConnection(user="root", password="", host="127.0.0.1", db="library_mgmt")
print("Connection Info {}".format(conn.host))
