import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'UPDATE person SET name=%s, lastname=%s, email=%s WHERE id_person=%s'
            values = (('Andreas', 'Examples', 'exs@exa.com', 1),
                      ('Andre', 'Exampl', 'exaa@exaa.com', 2))
            pointer.executemany(sql, values)
            updatedRecords = pointer.rowcount
            print(f'Updated Records: {updatedRecords}')

except Exception as e:
    print(e)
finally:
    connect.close()