#!/usr/bin/env python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """Displays the total size and status count metrics"""
    print(f"File size: {total_size}")
    for status, count in sorted(status_counts.items()):
        print(f"{status}: {count}")
        
def parse_line(line):
    try:
        elem = line.strip().split()
        if len(elem) >= 7:
            status_code = int(elem[-2])
            file_size = int(elem[-1])
            return status_code, file_size
    except ValueError:
        pass
    return None, None

def compute_metrics():
    """computes total size and status counts"""
    total_size = 0
    status_counts = {}
    
    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1
                    
            if i % 10 == 0:
                print_stats(total_size, status_counts)
                print()
                
    except KeyboardInterrupt:
        pass
    
    print_stats(total_size, status_counts)
    
    
if __name__ == "__main__":
    compute_metrics()
