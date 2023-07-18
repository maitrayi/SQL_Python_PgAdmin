import psycopg2
import psycopg2.extras
hostname = 'localhost'
database = 'Python_1'
username = 'postgres'
pwd = 'hello'
port_id = 5432
conn=None
cur=None
try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
            )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #this will tell to return data in dictionary form 
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                id      int PRIMARY kEY ,
                                name    varchar(40) NOT NULL, 
                                salary  int, 
                                dept_id varchar(30))'''
    cur.execute(create_script)
    insert_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s,%s)'
    insert_value = [(1, 'James', 1200, 'D1'),(2, 'Robin', 1500, 'D1'), (3, 'Xavier', 2000, 'D1') ]
    for record in insert_value:
        cur.execute(insert_script,record)


    #upading data in sql database 
    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5 )'
    cur.execute(update_script)

    #deleting a data
    delete_script =' DELETE FROM employee WHERE name = %s'
    delete_record = ('James',)  # comma is applied 
    cur.execute(delete_script,delete_record)


    #to see all the data
    cur.execute('SELECT * FROM employee')
    for record in cur.fetchall():
        #print(record[1], record[2])
        print(record['name'], record['salary'])
    conn.commit()

    


except Exception as error:
    print(error)



finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()