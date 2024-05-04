#!/usr/bin/python3
import sys

def print_stats(file_sizes, status_codes):
    print("File size: {}".format(sum(file_sizes)))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line):
    parts = line.strip().split()
    if len(parts) < 9 or parts[5] != '"GET' or parts[7] != 'HTTP/1.1"':
        return None
    try:
        status_code = int(parts[8])
        file_size = int(parts[9])
        return status_code, file_size
    except ValueError:
        return None

def main():
    file_sizes = []
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parsed = parse_line(line)
            if parsed:
                status_code, file_size = parsed
                file_sizes.append(file_size)
                if status_code in status_codes:
                    status_codes[status_code] += 1

                line_count += 1
                if line_count == 10:
                    print_stats(file_sizes, status_codes)
                    line_count = 0
                    file_sizes = []
                    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

