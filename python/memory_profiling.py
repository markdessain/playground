import time

def read_data():
    a = list(range(10000000))
    return a

def clean_data():
    pass

def fit():
    pass

def build_model():
    clean_data()
    fit()

@profile
def main():
    a = read_data()
    del a
    build_model()

if __name__ == "__main__":
    main()

# python3 -m memory_profiler memory_profiling.py
