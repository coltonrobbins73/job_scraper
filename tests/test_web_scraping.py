import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import csv

# Assuming your functions are in web_scraping.py
from web_scraping import scrape_job_data, extract_and_write_job_data

class TestWebScraping(unittest.TestCase):
    def setUp(self):
        # This will be run before each test
        self.skill = "python"
        self.place = "new york"
        self.no_of_pages = 1
        self.base_url = "https://in.indeed.com/viewjob?jk="
        self.headers = {
            "User-agent": "Mozilla/5.0"
        }

    @patch('web_scraping.requests.get')
    def test_scrape_job_data(self, mock_get):
        # Mocking the requests.get response
        mock_response = MagicMock()
        mock_response.text = '<html></html>'  # Simple HTML for example
        mock_get.return_value = mock_response

        # Mocking csv.writer to check what would be written
        with patch('csv.writer') as mock_writer:
            writer = MagicMock()
            mock_writer.return_value = writer
            scrape_job_data(self.skill, self.place, self.no_of_pages, writer, self.headers)
            mock_get.assert_called_with('https://www.indeed.co.in/jobs?q=python&l=new york&start=0', headers=self.headers)
            # Here you can add more assertions to check how your function handles the empty html

    def test_extract_and_write_job_data(self):
        # Preparing a mock job element and writer
        job = MagicMock()
        job.configure_mock(**{
            'find.return_value.text.strip.side_effect': ['Job Title', 'Company Name', 'New York', 'Today'],
            'get.return_value': '12345'
        })
        file = StringIO()
        writer = csv.writer(file)

        extract_and_write_job_data(job, self.base_url, writer)

        file.seek(0)
        result = file.readlines()
        expected = 'Job Title,Company Name,New York,Today,https://in.indeed.com/viewjob?jk=12345\n'
        self.assertEqual(result[0], expected)

if __name__ == '__main__':
    unittest.main()
