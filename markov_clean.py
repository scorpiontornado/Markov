import random


def generate_sentence(start_token, filenames):
    tokens = {}
    # Generate a dict of tokens with tokens from every file in filenames
    for file in filenames:
        with open(file) as f:
            file = f.read()  # create a list of the lines in the file
            split = file.lower().split()  # split the line into tokens
            for j, word in enumerate(split):
                # If it is not the last token, add a bigram:
                # (current word: next word)
                if j < len(split) - 1:
                    tokens[word] = tokens.get(word, [])
                    tokens[word].append(split[j+1])

    sentence = [start_token.lower()]  # Start the sentence with the given word

    current_token = sentence[-1]  # Set the current token to the last word
    while current_token:
        if current_token != "." and current_token in tokens and len(sentence) < 200:
            # If the current token is not ".", the current token is in the
            # tokens dict, and the sentence is less than 200 tokens long,
            # append a random choice to the sentence and reassign the current token
            sentence.append(random.choice(tokens[current_token]))
            current_token = sentence[-1]
        else:
            break

    return ' '.join(sentence)


# The random number generator is initialised to zero here purely
# for your own testing so that each time you run your code during
# development, you will get the same output. Remove this to get
# different output each time you run your code with the same input.
random.seed(0)

# Run the examples in the question.
for i in range(4):
    print(generate_sentence('There', ['single.txt']))
print('=' * 80)
for i in range(4):
    print(generate_sentence('the', ['jab.txt']))
print('=' * 80)
for i in range(4):
    print(generate_sentence('It', ['dracula.txt', 'pandp.txt']))
print('=' * 80)
for i in range(10):
    print(generate_sentence(
        'Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
print('=' * 80)
for i in range(8):
    print(generate_sentence('cat', ['single.txt', 'textwraps.txt']))
#print('=' * 80)
# for i in range(10):
#  print(generate_sentence('Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
