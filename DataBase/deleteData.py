import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'DELETE FROM person WHERE id_person=%s'
            inputPerson = input("Type the person to delete for: ")
            value = (inputPerson,)
            pointer.execute(sql, value)
            deletedRecord = pointer.rowcount
            print(f'Deleted Record: {deletedRecord}')

except Exception as e:
    print(e)
finally:
    connect.close()