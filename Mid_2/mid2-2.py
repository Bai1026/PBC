import re

def process_strings(string_list):
    direction_words = {'east': 'E', 'north': 'N', 'south': 'S', 'west': 'W'}
    pattern = r'\b(east|north|south|west)\b'
    replacement_count = 0
    processed_strings = []

    for string in string_list:
        # Strip leading and trailing spaces
        stripped_string = string.strip()
        
        # Find and replace directional words
        def replace_func(match):
            word = match.group(0)
            if word in direction_words:
                nonlocal replacement_count
                replacement_count += 1
                return direction_words[word]
            return word
        
        replaced_string = re.sub(pattern, replace_func, stripped_string)
        
        # Replace multiple spaces with a single space
        final_string = re.sub(r'\s+', ' ', replaced_string)
        
        # Add processed string to the list
        processed_strings.append(final_string)
    
    return processed_strings, replacement_count

# # Example usage:
# input_strings = [
#     "this is a  western book",
#     "  i am moving toward   the   east",
#     "east east eastnorth beast"
# ]

n = int(input())
input_strings = []
for _ in range(n):
    input_strings.append(input())
# print(input_strings)

processed_output, total_replacements = process_strings(input_strings)

processed_output.append(str(total_replacements))
# print(processed_output)

for item in processed_output:
    print(item, end='\n')