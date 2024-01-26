#!/usr/bin/env python3
"""
a script that reads stdin line by line and computes metrics: ...
"""

import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 7 and parts[5].isdigit() and parts[6].isdigit():
            status_code = int(parts[5])

            total_size += int(parts[6])
            status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_counts.keys()):
                    print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    pass

finally:
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")