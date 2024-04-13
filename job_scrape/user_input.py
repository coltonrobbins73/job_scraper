"""
This module gets user input
"""

def get_user_input():
    """
    Prompt the user to input their skill, location, and the number of pages they want to scrape.

    Returns:
        tuple: A tuple containing the skill (str), location (str), and number of pages (int).
    """
    skill = input('Enter your Skill: ').strip()
    place = input('Enter the location: ').strip()
    no_of_pages = int(input('Enter the #pages to scrape: '))
    return skill, place, no_of_pages
