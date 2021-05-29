import psycopg2

connect = psycopg2.connect(user='postgres', password='111111', host='127.0.0.1', port='5432', database="test_db")

try:
    with connect:
        with connect.cursor() as pointer:
            sql = 'SELECT * FROM person WHERE id_person IN %s'
            inputPerson = input("Write the people to search for (,): ")
            tuplePerson = tuple(inputPerson.split(','))
            keysPrimary = (tuplePerson,)
            pointer.execute(sql, keysPrimary)
            registers = pointer.fetchall()
            print(registers)
except Exception as e:
    print(e)
finally:
    connect.close()