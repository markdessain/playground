import time

def read_data():
    time.sleep(1.5)

def clean_data():
    time.sleep(2.7)

def fit():
    time.sleep(4.2)

def build_model():
    clean_data()
    fit()

def main():
    read_data()
    build_model()

if __name__ == "__main__":
    main()

# python3 -m cProfile -o stats.prof profiling.py
# snakeviz -H 0.0.0.0 -p 8080 -s stats.prof
# gprof2dot -f pstats stats.prof | dot -Tpng -o profile.png
