# Define pattern_search
def pattern_search(text, pattern):
    print(text)
    print(pattern)
    for index in range(len(text)):
        print(f'Text Index: {index}')
        match_count = 0
        for char in range(len(pattern)):
            print(f'Pattern Index: {char}')
            if pattern[char] == text[char + index]:
                print('Matching index found')
                print(f'Match Count: {match_count}')
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(f'{pattern} found at index {index}')


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"

# Invoke pattern_search
pattern_search(text, pattern)
