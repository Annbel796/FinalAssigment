import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_job_listings():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching the webpage!")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('div', class_='card')

    jobs = []
    for card in job_cards:
        try:
            title = card.find('h2', class_='title').text.strip()
        except AttributeError:
            title = "No title"

        try:
            company = card.find('h3', class_='company').text.strip()
        except AttributeError:
            company = "No company"

        try:
            location = card.find('p', class_='location').text.strip()
            if ',' in location:
                city, country = map(str.strip, location.split(',', 1))
                location = f"{city.title()}, {country.upper()}"
            else:
                location = location.title()
        except AttributeError:
            location = "No location"

        try:
            date_posted = card.find('time')['datetime']
        except (AttributeError, TypeError):
            date_posted = "Unknown date"

        job = {
            "Title": title,
            "Company": company,
            "Location": location,
            "Date Posted": date_posted,
        }

        jobs.append(job)

    return jobs

def save_to_json(data, file_path):
    if not data:
        print("No data to save!")
        return
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"Data successfully saved to {file_path}!")

def main():
    output_path = os.path.join(os.path.dirname(__file__), 'job_search_v2.json')
    jobs = scrape_job_listings()
    print(f"Found {len(jobs)} job listings.")
    save_to_json(jobs, output_path)

if __name__ == "__main__":
    main()


# INSTRUKTIONER

# Scrapa sidan - https://realpython.github.io/fake-jobs/
# Lägg in det i en lista av dictionaries, där varje dictionary skall innehålla jobtitel, företag, ort, och publiceringsdatum.
# Se till att varje ort är korrekt formaterad med första bokstaven i versal.
# Skriv ned ditt resultat till en JSON-fil kallad job_search_v2.json.