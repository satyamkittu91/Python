Process: An instance of a program

- Takes advantage of multiple CPUs and cores
- Can run multiple threads of execution concurrently
- separate memory space -> Memory is not shared between processes
- Great for CPU-bound processing
- New process is stated independently from other processes
- Processes are interruptable/killable
- One GIL for each process -> Avoids GIL limitations

- Heavyweight -> More overhead in terms of memory and startup time
- Starting a process is slower than starting a thread
- More memory
- IPC (Inter-Process Communication) is more complex than thread communication