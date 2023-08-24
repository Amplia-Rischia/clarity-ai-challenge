# Clarity AI Data Engineer Job Application

## Introduction
Hello! I'm Mihail Pascari, and I'm excited to apply for the Data Engineer position at Clarity AI. You can learn more about my background and experiences on my [LinkedIn profile](https://www.linkedin.com/in/mpascari/).

This repository contains my solutions for the coding challenge as part of the application process. Below, you'll find instructions on how to use the code snippets for the exercises.

### Description of my approach and assumptions
- I assume that "CONNECTIONS TO" means that I have to search the target host only in the second host collumn.
- In case of invalid input provided it is ok to just throw an error and exit
- The init_datetime and end_datetime provided as command-line arguments are in the format 'YYYY-MM-DD HH:MM:SS'. For this exercise will not be considered the necesity to handle different formats, providng less flexibility to the user.
- I am assuming UTC as timezone in which the date_time is provided

## Exercise 1: [Batch monitoring]

### Dependencies or prerequisites
No external dependencies are needed for this module. It utilizes standard Python libraries for file I/O and datetime manipulation.

### Running the script
To use the script with your log file, you can run a command like this in the terminal:
```
python log_parser.py log_file_name.txt "date_time1" "date_time2" "TargetHostname"
```
For instance you can launch this command that worked for the file sent me as data sample
```
python log_parser.py .\input-file-10000.txt "2018-08-01 00:00:00" "2019-08-15 23:59:59" "Sidney"
```
Which will output something like this
```
Timestamp            From Host
========================================
2019-08-13 08:02:45  Adalhi
2019-08-13 09:17:56  Anishka
2019-08-13 09:56:01  Kya
2019-08-13 18:14:00  Alexionna
2019-08-13 19:30:54  Wadie
2019-08-13 22:29:31  Zyleah
2019-08-13 22:37:29  Dyshawn
2019-08-13 23:59:49  Trestyn
```

### Running the tests
I could not resolve a couple test failures, I may need further time to manage this issue 

In order to test the log_parser_batch script you should just execute the command below:

```
python test_log_parser_batch.py
```

## Exercise 2: [Stream monitoring]

### Dependencies or prerequisites
This script uses the functions defined in log_parser_batch.py, plus will invoke as subprocess the script mock_appending.py and additionally requires the datetime module.

### Running the script
To use the script with your log file, you can run a command like this in the terminal:
```
python .\log_parser_streaming.py
```


```
Added log entry: 1692917683357 Jahniyah Cassy
Added log entry: 1692917693358 Leib Cassy
Added log entry: 1692917703360 Jahniyah Cassy
Added log entry: 1692917713362 Naoya Cassy
Report:
+-------------------+------------------+
|     Timestamp     |  Connected Host |
+-------------------+------------------+
| 2023-08-25 00:54:43 | Jahniyah         |
| 2023-08-25 00:54:53 | Leib             |
| 2023-08-25 00:55:03 | Naoya           |
+-------------------+------------------+
Most common host: Jahniyah

```