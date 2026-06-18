Threads: An entitity within a process that can be scheduled. (Also known as Lightweight process)
A process can spawn multiple threads, and all threads within a process share the same memory space. This allows for efficient communication and data sharing between threads, but it also means that threads can interfere with each other if they are not properly synchronized.

- All threads within a process share the same memory space
- Lightweight
- Starting a thread is faster than starting a process
- Great for I/O-bound tasks


- Threading is limited by GIL (Global Interpreter Lock) in Python, which means that only one thread can execute Python bytecode at a time. This can limit the performance of CPU-bound tasks when using threads.
- No effect for CPU-bound tasks due to GIL
- Not interruptable/killable
- Careful with race conditions and deadlocks