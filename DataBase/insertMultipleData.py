import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'INSERT INTO person(name,lastname, email) VALUES(%s, %s, %s)'
            values = (
                ('Roses', 'Back', 'Roseb@rose.com'),
                ('Danny', 'Black', 'Danyb@rose.com'),
                ('HC', 'Cryp', 'Crypb@rose.com')
            )
            pointer.executemany(sql, values)

            # save info in DB
            connect.commit()
            insertedRecords = pointer.rowcount
            print(f'Inserted Records: {insertedRecords}')
except Exception as e:
    print(e)
finally:
    connect.close()