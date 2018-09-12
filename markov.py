"""Generate Markov text from text files."""
import sys
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


def make_chains(text_string,n):
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

    # chains = {}

    # # your code goes here
    # words = text_string.split()
    # # print(words)

    # for i in range(len(words) -2):
    #     key = words[i], words[i +1]
    #     value = words[i + 2]

    #     if key not in chains:
    #         chains[key] = []
    #     chains[key].append(value)

    # return chains

    chains = {}

    words = text_string.split()

    for i in range(len(words) - n):
        key = tuple(words[i: n ])
        print(key)
        value = words[i + n]
        print(value)

        if key not in chains:
            chains[key] = []
            print(key)
            print(chains)
        chains[key].append(value)
    print(chains)
    return chains



def make_text(chains,n):
    """Return text from chains."""

    words = []
    key = choice(list(chains.keys()))
    
    words.append(key[0:n])
    # words.append(key[1])

    while True:
        new_key = tuple(words[-2:])
        if new_key not in chains:
            break
        random_word = choice(chains[new_key])

        words.append(random_word)
        
 

    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text,4)
# Produce random text
random_text = make_text(chains,4)

print(random_text)
