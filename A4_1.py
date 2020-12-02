"""A4_1 contains a function find_first_b(text, i) that takes a string
"text" that only contains the letter a and b and returns the index of the
first b.

Authour: Victor Tarnovski
Date 2020-12-2

"""

i = 0


def find_first_b(text, i):
    """Takes a string containing only a's and b's and returns the index
    of the first b"""
    length = len(text)
    if i < length:
        if text[i] == "b":
            return i        
        else:
            return (find_first_b(text, i+1))
    else:
        return None
  

if __name__ == "__main__":
    # Module Testing

    # find_first_b(text, i)

    # Case 1
    text = "aaaaaaba"
    print("The text is: ", text)
    print("The index of the first b is: ", find_first_b(text, i))
    print("\n")

    # Case 2
    text = "aaaa"
    print("The text is: ", text)
    print("The index of the first b is: ", find_first_b(text, i))
    print("\n")

    
    # Case 3
    text = "abaaaaba"
    print("The text is: ", text)
    print("The index of the first b is: ", find_first_b(text, i))
    print("\n")
