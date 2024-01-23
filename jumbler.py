"""
jumbler:  List dictionary words that match an anagram.
2022-06-25 by Steven

Credits: 
A. Nother Student, And Another:  Sketched pseudocode together
Our Friend:  Helped debug
"""

dict_file = open('dict.txt', 'r')
DICT = 'shortdict.txt'  # short version or testing and debugging
# DICT = "dict.txt"     #ull directory word list
anagram = input("Anagram to find>")

dict_file = open(DICT, "r")
for line in dict_file:
    word = line.strip()
    print(word)


def find(anagram: str):
    """print words in DICT that match anagram.

    >>>find("gamma")
        gamma

    >>>find ("nosuchword")
    """
    dict_file = open(DICT, "r")
    for line in dict_file:
        word = line.strip()
        if line == anagram:
            print(word)
        if __name__ == "__main__":
            import doctest
            doctest.testmod()
            print("Doctests Complete")


"""
Print words in DICT that match anagram
    >>>find("gamma")
        gamma
    >>>find("nosuchword")
    
    >>>find("MAGAM")
        gamma
    >>>find("KAWEA")
        awake
"""


def normalize(word: str) -> list[str]:
    """
    Returns a lsit of characters that is canonical for anagrams.

    >>>normalize("gamma") == normalize("magam")
        True
    >>>normalize("MAGAM") == normalize("gamma")
        True
    >>>normalize("KAWEA") == normalize("awake")
        True
    >>>normalize("KAWEA") == normalize("gamma")
        False

    """


def main():
    anagram == input("Anagram to find>")
    find(anagram)
    if __name__ == "__main__":
        main()

        # import doctest
        # doctest.testmod()
        # print ("Doctests Complete")


main()
