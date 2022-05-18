from sqlobject.mysql import builder

MySQLConnection = builder()
conn = MySQLConnection(user="root", password="", host="localhost", db="library_mgmt")
print("Connection Info {}".format(conn.host))
