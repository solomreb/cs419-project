import psycopg2

username = "vagrant"
password = "vagrant"
database = "cs419"

try:
    conn = psycopg2.connect(user=username, password=password, database=database)
except psycopg2.OperationalError:
    conn = -1

cursor = conn.cursor()

queries = list()

queries.append("""
    DROP TABLE IF EXISTS company;
""")

queries.append("""
    CREATE TABLE company(
       id     SERIAL PRIMARY KEY,
       name   TEXT   NOT NULL,
       age    INT    NOT NULL,
       salary REAL
    );
""")

queries.append("""
    INSERT INTO company
      (name, age, salary)
    VALUES
      ('allison', 21, 100000),
      ('becky', 21, 100000),
      ('lynda', 21, 100000),
      ('betty', 16, 18000),
      ('tom', 23, 35000),
      ('george', 24, 40000),
      ('vanessa', 31, 78000),
      ('justin', 52, 95000),
      ('adam', 43, 115000),
      ('richard', 64, 62000),
      ('alan', 47, 200000),
      ('keith', 48, 122000),
      ('rob', 47, 118000),
      ('sandra', 48, 55000),
      ('wayne', 55, 88000),
      ('john', 50, 85000),
      ('courtney', 34, 60000),
      ('roger', 28, 59000)
""")

try:
    for query in queries:
        print "\nRunning query:\n {0}".format(query)
        cursor.execute(query)
        conn.commit()
except psycopg2.Error as e:
    print e
    conn.rollback()
    pass

cursor.close()
