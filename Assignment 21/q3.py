# Design a Python application where multiple threads update a shared variable. Use a Lock to avoid race conditions. Each thread should increment the shared counter multiple times. Display the final value of the counter after all threads complete execution.

import threading

shared_counter = 0
counter_lock = threading.Lock()

def IncrementCounter(iterations):
    global shared_counter
    for _ in range(iterations):
        # Acquire Lock to prevent race conditions
        with counter_lock:
            shared_counter += 1

def main():
    threads = []
    num_threads = 5
    increments_per_thread = 100000
    
    print(f"Creating {num_threads} threads, each incrementing counter {increments_per_thread} times...")
    for i in range(num_threads):
        t = threading.Thread(target=IncrementCounter, args=(increments_per_thread,), name=f"Thread-{i+1}")
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print("Final value of shared counter:", shared_counter)
    expected = num_threads * increments_per_thread
    print("Expected value:", expected)

if __name__ == "__main__":
    main()
