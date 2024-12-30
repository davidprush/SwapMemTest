import os
import psutil
import time

def check_swap_usage():
    swap = psutil.swap_memory()
    return swap.percent

def check_system_load(max_load=0.85):
    # Get system load averages for last 1, 5, and 15 minutes
    load1, load5, load15 = os.getloadavg()
    # Normalize to number of CPUs
    cpu_count = os.cpu_count()
    normalized_load = load1 / cpu_count
    return normalized_load > max_load

def main():
    # Get total physical memory
    total_memory = psutil.virtual_memory().total
    
    # We'll attempt to allocate 1.5 times the total memory, which should force swapping
    memory_to_allocate = int(total_memory * 1.5)
    
    # List to hold our memory chunks
    memory_chunks = []
    
    chunk_size = 1024 * 1024  # 1MB chunks
    
    print(f"Starting memory test. Total memory: {total_memory / (1024.0 ** 3):.2f} GB")
    
    # Allocate memory
    for _ in range(0, memory_to_allocate, chunk_size):
        if check_system_load():
            print("System load too high. Stopping memory allocation.")
            break
        
        try:
            memory_chunks.append(bytearray(chunk_size))
            print(f"Allocated memory: {len(memory_chunks) * chunk_size / (1024.0 ** 2):.2f} MB. Swap usage: {check_swap_usage()}%")
            time.sleep(1)  # Give some time to see the effects
        except MemoryError:
            print("Memory allocation failed, possibly hit system limits or swap space is full.")
            break
    
    # Keep the memory allocated for observation
    input("Press Enter to release memory...")
    
    # Release memory
    del memory_chunks
    
    print("Memory released.")

if __name__ == "__main__":
    main()
