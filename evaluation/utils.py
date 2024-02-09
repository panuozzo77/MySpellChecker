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
        print(f"Corrected form '{corrected}' is close to the original form '{query}'")
    else:
        print(f"Corrected form '{corrected}' is far from the original form '{query}'")
