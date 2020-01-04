import mysql.connector
import sys

def fetch_table_data(DataBase_Name,table_name):
    # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    cnx = mysql.connector.connect(
        host='localhost',
        database=DataBase_Name,
        user='root',
        password=''
    )

    cursor = cnx.cursor()
    cursor.execute('select * from ' + table_name)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    # Closing connection
    cnx.close()

    return header, rows


def export(DataBase_Name,table_name):
    header, rows = fetch_table_data(DataBase_Name,table_name)

    # Create csv file
    f = open(table_name + '.csv', 'w')

    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)

# Tables to be exported
DataBase_Name = sys.argv[1]
Table_Name = sys.argv[2]

export(DataBase_Name,Table_Name)
