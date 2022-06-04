# Define pattern_search
def pattern_search(text, pattern):
    print(text)
    print(pattern)
    for index in range(len(text)):
        print(f'Text Index: {index}')
        for char in range(len(pattern)):
            print(f'Pattern Index: {char}')
            if pattern[char] == text[char + index]:
                print('Matching index found')
            else:
                break


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"

# Invoke pattern_search
pattern_search(text, pattern)
