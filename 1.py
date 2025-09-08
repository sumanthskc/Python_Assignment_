import mysql.connector as connection

def employee(batchsize=100):
    conn = connection.connect(
        host="localhost",
        user="root",
        password="Suman@_2004",
        database="employees"
    )

    my_cursor = conn.cursor()
    offset = 0
    count = 0
    while True:
        query = f"SELECT emp_no, first_name, last_name FROM employees LIMIT {batchsize} OFFSET {offset}"
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        
        if not result:
            break

        for res in result:
            yield res
            count += 1

        offset += batchsize

    print("Fetched", count)
    my_cursor.close()
    conn.close()

for res in employee():
    print(f"Emp ID: {res[0]}, First Name: {res[1]}, Last Name: {res[2]}")
