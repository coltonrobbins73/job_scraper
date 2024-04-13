from user_input import get_user_input
from file_operations import create_directory, configure_csv_file, write_headers
from web_scraping import scrape_job_data
import os
import csv

def main():
    skill, place, no_of_pages = get_user_input()
    create_directory(os.getcwd())
    file_path = configure_csv_file(skill, place)

    headers = {
        "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        write_headers(writer)
        scrape_job_data(skill, place, no_of_pages, writer, headers)

    print(f'Jobs data written to <{file_path}> successfully.')

if __name__ == "__main__":
    main()
