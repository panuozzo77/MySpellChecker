import requests
import prompt.utils as f
import authenticate.utils as file
import evaluation.utils as evaluation

@f.check_length
def google_search(query):
    api_key, cx = file.get_credentials()
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    print(f"Here's the url you searched {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        evaluation.check_spelling(query, response.json().get('spelling', {}).get('correctedQuery', ''))
    else:
        print(f"Request failed with status code {response.status_code}")
    return response.json()


#google_search('come cucinare la pasta con il pesto')

s = "The quick brown fox jumps over the lazy dog. This classic frase is oftn used to demonstrate fonts or test keyboards due to its use of every letter in the English alphebet. It's a pangram, a sentens containing every letter of the alfabet at least ones. Pangrams are useful in typografi, design, and computer programing for testing fonts, layuts, and input methods. However, ther are meny variations of this sentence, with sum including punctuation or additional words. Regardles of the variation, the purpose remains the same: to provide a concise and comprehensive sample of text. Beyond its practicl aplicashuns, the phrase has achieved cultural signifikans and is recognized by many English speakers around the world. It's often used as a tool for memory exercises or as a playful reference in literature and media. Whil its origins are unclear, the frase has endured thru generations and continues to be a familiar and widely recognized sequens of words. The quick brown fox jumps over the lazy dog. This classic phrase is often used to demonstrate fonts or test keyboards due to its use of every letter in the English alphebet. It's a pangram, a sentens containing every letter of the alfabet at least ones. Pangrams are useful in typografi, design, and computer programing for testing fonts, layuts, and input methods. However, ther are meny variations of this sentence, with sum including punctuation or additional words. Regardles of the variation, the purpose remains the same: to provide a concise and comprehensive sample of text. Beyond its practicl aplicashuns, the frase has achieved cultural signifikans and is recognized by many English speakers around the world. It's often used as a tool for memory exercises or as a playful reference in literature and media. Whil its origins are unclear, the frase has endured thru generations and continues to be a familiar and widely recognized sequens of words. The quick brown fox jumps over the lazy dog. This classic frase is oftn used to demonstrate fonts or test keyboards due to its use of every letter in the English alphebet. It's a pangram, a sentens containing every letter of the alfabet at least ones. Pangrams are useful in typografi, design, and computer programing for testing fonts, layuts, and input methods. However, ther are meny variations of this sentence, with sum including punctuation or additional words. Regardles of the variation, the purpose remains the same: to provide a concise and comprehensive sample of text. Beyond its practicl aplicashuns, the frase has achieved cultural signifikans and is recognized by many English speakers around the world. It's often used as a tool for memory exercises or as a playful reference in literature and media. Whil its origins are unclear, the frase has endured thru generations and continues to be a familiar and widely recognized sequens of words."
google_search(s)
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
