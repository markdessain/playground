# In some utils.py or redshift.py file
import os
import logging
import psycopg2
from contextlib import contextmanager

log = logging.getLogger(__name__)


@contextmanager
def redshift():
    try:
        connection = psycopg2.connect(
            dbname=os.environ.get('REDSHIFT_DATABASE'),
            host=os.environ.get('REDSHIFT_HOST'),
            port=os.environ.get('REDSHIFT_PORT'),
            user=os.environ.get('REDSHIFT_USERNAME'),
            password=os.environ.get('REDSHIFT_PASSWORD')
        )
        yield connection
    finally:
        try:
            connection.close()
        except Exception:
            log.exception('Unable to close connection')


# In your code
from ... import redshift

with redshift() as connection:
    print(connection)
