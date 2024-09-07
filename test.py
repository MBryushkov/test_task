import psycopg2
import json
from datetime import datetime
from decimal import Decimal
from ftplib import FTP_TLS

conn = psycopg2.connect(dbname="test1", user="postgres", password="1711", host="localhost", port="5432")
cursor = conn.cursor()

cursor.execute("SELECT * FROM maternity_hospital")
ans=cursor.fetchall()

cursor.close()
conn.close()

all_data=[]
data = {}
 
for a in ans:
    data=({'id': a[0], 'date': a[1].isoformat(), 'name': a[2], 'weight': str(a[3])})
    all_data.append(data)
    print(a)
    
with open('test.json', 'w') as file:
    json.dump(all_data, file, indent=4)
    
ftp_server = '127.0.0.1'
ftp_user = 'admin'
ftp_password = '1711'

ftps = FTP_TLS(ftp_server)
ftps.login(ftp_user, ftp_password)

# Принудительное включение защищенного соединения
ftps.prot_p()

ftps.cwd('/uploads/')
with open('test.json', 'rb') as file:
    ftps.storbinary('STOR test.json', file)

ftps.quit()