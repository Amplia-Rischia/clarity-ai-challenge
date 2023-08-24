import time
from datetime import datetime, timedelta
from log_parser_batch import parse_line, validate_datetime, load_connections, filter_connections
import subprocess

def start_mock_append_script():
    # Modify this command to start the mock append script in your environment
    subprocess.Popen(["python", "mock_appending.py"])

def generate_reports(log_file, host_to_monitor, report_interval):
    while True:
        # Calculate the time range for the last report interval
        end_datetime = datetime.now()
        init_datetime = end_datetime - timedelta(seconds=report_interval)
        
        # Convert datetime strings to datetime objects
        init_time = datetime.strptime(init_datetime.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_datetime.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
        
        # Parse data and generate reports
        connections = load_connections(log_file)
        connected_hosts = filter_connections(connections, init_time, end_time, host_to_monitor)
        
        # Generate and print reports using ASCII art
        if connected_hosts:
            print("Report:")
            print("+-------------------+------------------+")
            print("|     Timestamp     |  Connected Host |")
            print("+-------------------+------------------+")
            for timestamp, host in connected_hosts:
                timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                print("| {:<17} | {:<16} |".format(timestamp_str, host))
            print("+-------------------+------------------+")
            most_common_host = find_most_common_host(connected_hosts)
            print("Most common host:", most_common_host)
        else:
            print("No connections recorded in the last interval.")
        
        time.sleep(report_interval)  # Wait for the specified interval

def find_most_common_host(connected_hosts):
    host_count = {}
    for _, host in connected_hosts:
        host_count[host] = host_count.get(host, 0) + 1
    
    if host_count:
        most_common_host = max(host_count, key=host_count.get)
        return most_common_host
    else:
        return None

if __name__ == "__main__":
    log_file = "./input-file-10000.txt"
    host_to_monitor = "Cassy"
    report_interval = 30  # 30 seconds
    
    start_mock_append_script()
    generate_reports(log_file, host_to_monitor, report_interval)
