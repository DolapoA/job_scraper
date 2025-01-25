#!/usr/bin/python3

import sys
import src.cli as cli
import csv
from jobspy import scrape_jobs
import pandas as pd
import re
import os

# Pull variables from user via the cli module
def main(argv=None):

    # initialise cli objects
    cli_obj = cli.cli_obj(sys.argv[1:])
    job_board = cli_obj.args.job_board
    job_title = cli_obj.args.job_title
    city = cli_obj.args.city
    nation = cli_obj.args.nation
    
    # all nations
    all_nations = [
        "argentina", "australia", "austria", "bahrain", "belgium", "brazil", "canada", "chile", "china", 
        "colombia", "costa rica", "czech republic", "czechia", "denmark", "ecuador", "egypt", "finland", 
        "france", "germany", "greece", "hong kong", "hungary", "india", "indonesia", "ireland", "israel", 
        "italy", "japan", "kuwait", "luxembourg", "malaysia", "malta", "mexico", "morocco", "netherlands", 
        "new zealand", "nigeria", "norway", "oman", "pakistan", "panama", "peru", "philippines", "poland", 
        "portugal", "qatar", "romania", "saudi arabia", "singapore", "south africa", "south korea", "spain", 
        "sweden", "switzerland", "taiwan", "thailand", "türkiye", "turkey", "ukraine", "united arab emirates", 
        "uk", "united kingdom", "usa", "us", "united states", "uruguay", "venezuela", "vietnam", "usa/ca", 
        "worldwide"
    ]

    if nation not in all_nations:
        print(f"Error: {nation} is not a valid nation. Please choose from the following list:\n{all_nations}")
        sys.exit(1)

    # Split the job board string into an array for multiple job boards    
    site_names = job_board.split(',')
    print(f"\n{site_names} \n")

    all_jobs = pd.DataFrame()

    for _ in range(5):
        # Scrape jobs
        jobs = scrape_jobs(
            site_name=site_names,
            search_term=job_title,
            google_search_term=f"{job_title} jobs in {city}, {nation} since yesterday",
            location=city,
            results_wanted=500,
            hours_old=720,
            country_indeed=nation
            #proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
            #linkedin_fetch_description=True

            
        )

        print(f"Found {len(jobs)} jobs")
        all_jobs = pd.concat([all_jobs, jobs])

    # Remove duplicates based on the 'id' column
    all_jobs.drop_duplicates(subset='id', inplace=True)

    # Filter the DataFrame to only include rows where the job title is in the 'title' column
    filtered_df = all_jobs[all_jobs['title'].str.contains(job_title, case=False, na=False)]

    # Check if jobs.csv exists and create a new file with an underscore followed by a number if it does
    base_filename = "jobs"
    extension = ".csv"
    filename = base_filename + extension
    counter = 1

    while os.path.exists(filename):
        filename = f"{base_filename}_{counter}{extension}"
        counter += 1

    # Save the filtered DataFrame to the new file
    filtered_df.to_csv(filename, quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False)
    print(f"Saved {len(filtered_df)} jobs to {filename}")

if __name__ == "__main__":
    main()
