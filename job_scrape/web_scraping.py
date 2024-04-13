import requests
from bs4 import BeautifulSoup

def scrape_job_data(skill, place, no_of_pages, csv_writer, headers):
    """
    Scrapes job data from Indeed based on the given skill, place, and number of pages.

    Args:
        skill (str): Skill or job title to search for.
        place (str): Location to search within.
        no_of_pages (int): Number of pages to scrape.
        csv_writer (csv.writer): A CSV writer object to write data to the file.
        headers (dict): Headers to use for the HTTP requests.
    """
    base_url = 'https://in.indeed.com/viewjob?jk='

    print('\nScraping in progress...\n')
    for page in range(no_of_pages):
        url = f"https://www.indeed.co.in/jobs?q={skill}&l={place}&start={page * 10}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        jobs = soup.find_all('a', class_='tapItem')
        for job in jobs:
            extract_and_write_job_data(job, base_url, csv_writer)

def extract_and_write_job_data(job, base_url, csv_writer):
    """
    Extracts job data from a job HTML element and writes it to a CSV file.

    Args:
        job (bs4.element.Tag): The job listing element.
        base_url (str): The base URL to construct the job's full URL.
        csv_writer (csv.writer): The CSV writer object used to write to the file.
    """
    job_id = job['id'].split('_')[-1]
    job_title = job.find('span', title=True).text.strip()
    company = job.find('span', class_='companyName').text.strip()
    location = job.find('div', class_='companyLocation').text.strip()
    posted = job.find('span', class_='date').text.strip()
    job_link = base_url + job_id
    csv_writer.writerow([job_title, company, location.title(), posted, job_link])
