import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'DELETE FROM person WHERE id_person IN %s'
            inputPerson = input("Type the people to delete for: ")
            values = (tuple(inputPerson.split(',')),)
            pointer.execute(sql, values)
            deletedRecords = pointer.rowcount
            print(f'Deleted Records: {deletedRecords}')

except Exception as e:
    print(e)
finally:
    connect.close()