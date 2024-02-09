def check_length(func):
    def wrapper(query):
        if len(query) > 2048:
            print("Warning: Query length exceeds 2048 characters. I'll split it into smaller pieces.")
            proceed = input("Do you want to proceed with splitting the query into smaller pieces? (yes/no): ")
            if proceed.lower() == 'yes':
                queries = split_text(query)
                proceed = input(f"Do you want to analyze {len(queries)} queries? (yes/no):")
                if proceed.lower() == 'yes':
                    for q in queries:
                        func(q)
                else:
                    print("Execution Aborted")
            else:
                print("Execution Aborted")
        else:
            func(query)

    def split_text(text):
        sentences = []
        if '.' in text:
            # Split by '.' if present
            sentences = text.split('.')
        else:
            # If '.' is not present, split by spaces
            words = text.split(' ')
            current_sentence = ''
            for word in words:
                if len(current_sentence) + len(word) < 1024:
                    current_sentence += word + ' '
                else:
                    sentences.append(current_sentence.strip())
                    current_sentence = word + ' '
            if current_sentence:
                sentences.append(current_sentence.strip())
        return sentences

    return wrapper
