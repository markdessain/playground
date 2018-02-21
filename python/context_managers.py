from contextlib import contextmanager



# Setup ....
# Your logic
# Tear Down ...

f = open('new_in_python.py', 'r')
print(f.readlines())
f.close()

connection = psycopg2.connect(
    ...
)
print(
    pd.read_sql(
        '''
        ...
        ...
        ...
        ''',
        connection
    )
)
connection.close()



with open('new_in_python.py', 'r') as f:
    print(f.readlines())


with redshift() as connection:
    print(
        pd.read_sql(
            '''
            ...
            ...
            ...
            ''',
            connection
        )
    )



@contextmanager
def manager():
    try:
        # Do Setup
        yield
    finally:
        # Do Tear Down



@contextmanager
def redshift():
    try:
        connection = psycopg2.connect(
            ...
        )
        yield connection
    except Exception e:
        raise e
    finally:
        connection.close()
