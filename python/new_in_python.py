# Formatted strings
# ================================================

first_name = 'Mark'
last_name = 'Dessain'

print('Hello %s %s' % (first_name, last_name))
print('Hello {first_name} {last_name}'.format(first_name=first_name, last_name=last_name))

# New
print(f'Hello {first_name} {last_name}')



# Matrix Multiplication
# ================================================

import numpy as np

x = np.ones(3)
m = np.eye(3)

print(np.dot(x, m))

# New
print(x @ m)


# Math
# ==================================================

import math
a = 5.0
b = 4.99998
math.isclose(a, b, rel_tol=1e-5)


# Async
# ===============================================

import asyncio

async def ticker(delay, to, name):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        print(name, i)
        await asyncio.sleep(delay)

ioloop = asyncio.get_event_loop()

tasks = [
    ioloop.create_task(ticker(delay=1, to=10, name='Mark')),
    ioloop.create_task(ticker(delay=2, to=10, name='Marisa')),
    ioloop.create_task(ticker(delay=3, to=10, name='Javier'))
]

ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()


# Documentation Type Hinting
# ================================================

def greeting(name: str) -> str:
    return 'Hello ' + name
