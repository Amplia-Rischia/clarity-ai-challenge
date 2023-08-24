import sys
from datetime import datetime, timedelta

def parse_line(line):
    timestamp, source, destination = line.strip().split()
    return int(timestamp), source, destination

def filter_connections(log_file, init_datetime, end_datetime, target_hostname):
    try:
        init_time = datetime.strptime(init_datetime, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        print("Invalid datetime format. Please use 'YYYY-MM-DD HH:MM:SS'")
        return []

    connections = []

    with open(log_file, 'r') as file:
        for line in file:
            timestamp, source, destination = parse_line(line)
            connection_time = datetime.fromtimestamp(timestamp / 1000)

            if init_time <= connection_time <= end_time and destination == target_hostname:
                connections.append((connection_time, source))

    return connections

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python log_parser.py <log_file> <init_datetime> <end_datetime> <hostname>")
        sys.exit(1)

    log_file = sys.argv[1]
    init_datetime = sys.argv[2]
    end_datetime = sys.argv[3]
    target_hostname = sys.argv[4]

    connections = filter_connections(log_file, init_datetime, end_datetime, target_hostname)

    if connections:
        print("{:<20} {:<20}".format("Timestamp", "From Host"))
        print("="*40)
        for timestamp, hostname in connections:
            print("{:<20} {:<20}".format(timestamp.strftime('%Y-%m-%d %H:%M:%S'), hostname))
    else:
        print("No connections found for", target_hostname, "during the specified period.")
