import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'SELECT * FROM person WHERE id_person=%s'
            id_person = input("Type the key to search for: ")
            keyPrimary = (id_person,)
            pointer.execute(sql, keyPrimary)
            registers = pointer.fetchone()
            print(registers)
except Exception as e:
    print(e)
finally:
    connect.close()