import requests
import json
import configparser
from difflib import ndiff


def calculate_levenshtein_distance(str_1, str_2):
    distance = 0
    buffer_removed = buffer_added = 0
    for x in ndiff(str_1, str_2):
        code = x[0]
        if code == ' ':
            distance += max(buffer_removed, buffer_added)
            buffer_removed = buffer_added = 0
        elif code == '-':
            buffer_removed += 1
        elif code == '+':
            buffer_added += 1
    distance += max(buffer_removed, buffer_added)
    return distance


def check_spelling(query, corrected):
    distance = 0
    if corrected != '':
        distance = calculate_levenshtein_distance(query, corrected)
    if distance == 0:
        print(f"'{query}' is well written!")
    elif distance == 1:
        print(f"Corrected word '{corrected}' is close to the original word '{query}'")
    else:
        print(f"Corrected word '{corrected}' is far from the original word '{query}'")


def get_credentials():
    config = configparser.ConfigParser()
    config.read('credentials.conf')
    api_key = config.get('Credentials', 'api_key')
    cx = config.get('Credentials', 'cx')
    return api_key, cx


def google_search(query):
    api_key, cx = get_credentials()
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Here's the url you searched {url}")
        check_spelling(query, response.json().get('spelling', {}).get('correctedQuery', ''))
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None


google_search('come cucinare la pasta con il pesto')
'''
results = ciao
if results:
    print(json.dumps(results, indent=4))
    corrected_query = results.get('spelling', {}).get('correctedQuery', '')
    #corrected_query = parsed_json['spelling']['corrected_query']
    print(corrected_query)
'''
# if __name__ == "__main__":
# text = "ciao"
# text.json().get('spelling', {}).get('correctedQuery', '')
