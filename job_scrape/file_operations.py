import os
import csv

def create_directory(path):
    """
    Create a directory at the specified path if it does not already exist.

    Args:
        path (str): The file system path where the directory should be created.
    """
    if not os.path.exists(path):
        os.mkdir(path)
        print('Base Directory Created Successfully.')

def configure_csv_file(skill, place):
    """
    Generates the file path for a CSV file named according to the skill and place provided.

    Args:
        skill (str): The user's skill.
        place (str): The location associated with the job search.

    Returns:
        str: The full file path for the CSV file.
    """
    file_name = f"{skill.title()}_{place.title()}_Jobs.csv"
    file_path = os.path.join(os.getcwd(), r'data/', file_name)
    return file_path

def write_headers(csv_writer):
    """
    Writes the headers to the CSV file.

    Args:
        csv_writer (csv.writer): A CSV writer object.
    """
    csv_writer.writerow(['JOB_NAME', 'COMPANY', 'LOCATION', 'POSTED', 'APPLY_LINK'])
