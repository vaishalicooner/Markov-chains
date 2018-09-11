"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    file = open(file_path)
    text_file = file.read()

    #print(text_file)

    return text_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    # print(words)

    for word in range(len(words) -2):
        key = words[word], words[word +1]
        value = words[word + 2]

        if key not in chains:
            chains[key] = []
        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    # words = []
    # chains_keys = sorted(chains.keys())
    # chains_values = sorted(chains.values())
    # # print(chains_keys)
    # # print(chains_values)

    # new_key = chains_keys[0][1]
    # print(new_key)
    # new_value = random.choice(chains_values)
    # print(new_value)
    # print(new_key)
    # chosen_word = random.choice(chains_dict)
    # print(chosen_word)


    # your code goes here

    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# Produce random text
random_text = make_text(chains)

print(random_text)
