from difflib import ndiff
from datetime import datetime

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
        print(f"Corrected form '{corrected}' is close to the submitted form '{query}'")
    else:
        print(f"Corrected form '{corrected}' is far from the submitted form '{query}'")

    # Generate HTML with colored differences
    html_content = "<html><head><style>.added { background-color: #ddffdd; } .removed { background-color: #ffdddd; }</style></head><body>"
    html_content += "<h3>Original Form:</h3><pre>"
    for x in ndiff(query, corrected):
        code = x[0]
        value = x[2:]
        if code == ' ':
            html_content += value
        elif code == '-':
            html_content += f"<span class='removed'>{value}</span>"
        elif code == '+':
            html_content += f"<span class='added'>{value}</span>"
    html_content += "</pre></br>"
    html_content += "<h3>Corrected Form:</h3><pre>"
    for x in ndiff(corrected, query):
        code = x[0]
        value = x[2:]
        if code == ' ':
            html_content += value
        elif code == '-':
            html_content += f"<span class='removed'>{value}</span>"
        elif code == '+':
            html_content += f"<span class='added'>{value}</span>"
    html_content += "</pre></body></html>"

    # Write HTML content to the output file
    #timestamp = datetime.now().strftime("%Y_%m_%d_%H:%M")
    output_file = f"test.html"

    with open(output_file, 'a') as file:
        file.write(html_content)
