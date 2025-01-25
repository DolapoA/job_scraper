# job scraper

Modifying Author(s): Dolapo Ajayi

### Tool Description
A CLI tool that fetches jobs from LinkedIn and other job boards

---
### Features
1. Fetches job positions from roughly the past 30 days and collates them in a csv file

---
### Requirements
1. Python version >= 3.10 required

2. pip install -U python-jobspy

---
### Usage
  python3 run_job_scraper.py [-h] -b <JOB_BOARD> -j <JOB_TITLE> -c <CITY> -n <NATION>

options:
  -h, --help            
                        show this help message and exit

  -b JOB_BOARD, --job_board <JOB_BOARD>
                        Provide a job board (indeed/linkedin/zip_recruiter/glassdoor/google). You can also provide a comma separated list of job boards e.g. "indeed,linkedin".

  -j JOB_TITLE, --job_title <JOB_TITLE>
                        Provide a Job title e.g. "bioinformatician".

  -c CITY, --city <CITY>  Enter the city of the job e.g. "Barcelona"

  -n NATION, --nation <NATION>
                        Enter the nation of the job e.g. "Spain"

---                     
### Limitations
- Currently only working with LinkedIn