import sys
import re
import os.path
from datetime import datetime

def parse_line(line):
    timestamp, source, destination = line.strip().split()
    return int(timestamp), source, destination

def validate_datetime(datetime_str):
    datetime_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    if not datetime_pattern.match(datetime_str):
        raise ValueError("Invalid datetime format: Please use 'YYYY-MM-DD HH:MM:SS'")

def load_connections(log_file):
    connections = []
    with open(log_file, 'r') as file:
        for line in file:
            timestamp, source, destination = parse_line(line)
            connections.append((timestamp, source, destination))
    return connections

def filter_connections(connections, init_time, end_time, target_hostname):
    filtered_connections = []
    for timestamp, source, destination in connections:
        connection_time = datetime.fromtimestamp(timestamp / 1000)
        if init_time <= connection_time <= end_time and destination == target_hostname:
            filtered_connections.append((connection_time, source))
    return filtered_connections

def print_connections(connections):
    if connections:
        print("{:<20} {:<20}".format("Timestamp", "From Host"))
        print("="*40)
        for timestamp, hostname in connections:
            print("{:<20} {:<20}".format(timestamp.strftime('%Y-%m-%d %H:%M:%S'), hostname))
    else:
        print("No connections found for the specified criteria.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python log_parser.py <log_file> <init_datetime> <end_datetime> <hostname>")
        sys.exit(1)

    log_file = os.path.abspath(sys.argv[1])
    init_datetime = sys.argv[2]
    end_datetime = sys.argv[3]
    target_hostname = sys.argv[4]

    validate_datetime(init_datetime)
    validate_datetime(end_datetime)

    if not os.path.exists(log_file):
        print("Error: Log file does not exist.")
        sys.exit(1)

    try:
        init_time = datetime.strptime(init_datetime, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')

        connections = load_connections(log_file)
        filtered_connections = filter_connections(connections, init_time, end_time, target_hostname)
        print_connections(filtered_connections)
        
    except ValueError as e:
        print(e)
        sys.exit(1)
