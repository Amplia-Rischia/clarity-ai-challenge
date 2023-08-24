import time
import random

log_file_path = "./input-file-10000.txt"
source_hostnames = [
    "Leib", "Bray", "Debbra", "Shaquane", "Naoya",
    "Kairi", "Sukayna", "Teddi", "Eman", "Reshae",
    "Maronda", "Jahniyah", "Loreto"
]
destination_hostnames = [
    "Cassy"
]

def append_to_log_file(line):
    with open(log_file_path, "a") as log_file:
        log_file.write(line + "\n")

def generate_random_log_entry():
    timestamp = int(time.time() * 1000)
    source = random.choice(source_hostnames)
    destination = random.choice(destination_hostnames)
    return f"{timestamp} {source} {destination}"

if __name__ == "__main__":
    while True:
        log_entry = generate_random_log_entry()
        append_to_log_file(log_entry)
        print(f"Added log entry: {log_entry}")
        time.sleep(10)  # Wait for 10 seconds
