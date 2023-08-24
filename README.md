# Clarity AI Data Engineer Job Application

## Introduction
Hello! I'm Mihail Pascari, and I'm excited to apply for the Data Engineer position at Clarity AI. You can learn more about my background and experiences on my [LinkedIn profile](https://www.linkedin.com/in/mpascari/).

This repository contains my solutions for the coding challenge as part of the application process. Below, you'll find instructions on how to use the code snippets for the exercises.

## Exercise 1: [Batch monitoring]

### Description of my approach and assumptions
[]

### Dependencies or prerequisites
Python installed on your OS

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
2022-08-01 01:00:00  host1               
2022-08-01 01:20:00  host2               
2022-08-01 01:40:00  host3
```

## Exercise 2: [Stream monitoring]

### Description of my approach and assumptions
[Description of the exercise and what the code snippet accomplishes.]

### Usage
1. [Step-by-step instructions on how to set up and run the code snippet.]
2. [Any dependencies or prerequisites needed before running the code.]