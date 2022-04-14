import primes, primes_python, primes_python_compiled
import time

def main():
    n = 10_000
    print("Testing \n")
    cython_start = time.time()
    _ = primes.primes(n)
    cython_end = time.time()
    normal_compiled_start = time.time()
    _ = primes_python_compiled.primes(n)
    normal_compiled_end = time.time()
    normal_start = time.time()
    _ = primes_python.primes(n)
    normal_end = time.time()
    print(f"""Time for {n} primes: pure cython {cython_end - cython_start}, cython compiled python
          {normal_compiled_end - normal_compiled_start} and pure python {normal_end - normal_start}""")

if __name__ == "__main__":
    assert(primes_python.primes(1000) == primes.primes(1000))
    assert(primes_python_compiled.primes(1000) == primes.primes(1000))
    main()
