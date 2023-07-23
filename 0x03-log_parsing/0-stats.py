#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """Displays the total size and status count metrics"""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status in {200, 301, 400, 401, 403, 404, 405, 500}:
            print(f"{status}: {status_counts[status]}")


def parse_line(line):
    """Read and parse data"""
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
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
        }

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)
                print()

    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    compute_metrics()
