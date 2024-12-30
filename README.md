# Memory Swap Test Script for Linux

This script tests how memory swapping works between RAM and swap space on a Linux system. It attempts to allocate memory beyond the system's physical RAM, forcing the use of swap space. Here's how it works:

## Features

- **Memory Allocation**: The script allocates memory in chunks, increasing until it either fills up available memory or hits system limits.
- **System Load Check**: To prevent system lockup or excessive slowdown, the script checks the system load before allocating more memory. If the load is too high, it stops allocating.

## How It Works

1. **Check Total Memory**: It first determines the total physical RAM available.
2. **Allocate Memory**: It then tries to allocate 1.5 times the total memory in small chunks, printing updates on memory and swap usage.
3. **System Load Monitoring**: If the system load exceeds a predefined threshold (85% of CPU capacity by default), memory allocation stops to avoid overwhelming the system.

## Running the Script

### Prerequisites

- **Python 3** installed on your system.
- **psutil** library. Install with:

  ```bash
  pip install psutil# swap-test
Python program to test swap memory
