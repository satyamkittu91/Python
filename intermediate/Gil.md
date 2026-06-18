GIL : Global interpreter lock
- A lock that allows only one thread at a time to execute in python.
- This means that even if you have multiple threads, only one thread can execute python code at a time.
- This can lead to performance issues in multi-threaded programs, especially if they are CPU-bound

- Needed in CPython because memory management is not thread-safe

- Avoid:
    - Use multiprocesing
    - Use a different, free threaded python implementation (Jython, IronPython)
    - use pythonas wrapper for third-party libraries (C/C++) -> numpy, scipy