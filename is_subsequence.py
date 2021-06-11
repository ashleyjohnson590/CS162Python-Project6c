#Author: Ashley Johnson
#Date: 5/3/2021
#Description: Program takes 2 strings as a parameter and returns true if the first string is a subsequence
#of the second string. Otherwise, it returns false.

def is_subsequence(string1, string2):
    """checks if string1 is a subsequence of string2 and returns true if it is, returns false if not"""
    print("string1 = {}".format(string1))
    print("string2 = {}".format(string2))
    if len(string1)==0:
        print("found them all")
        return True
    elif len(string2) == 0:
        print("ran out of letters")
        return False
    else:
        letter = string1[0]
        index = string2.find(letter)
        if index >= 0:
            print("found {} at index {}".format(letter, index))
            return is_subsequence(string1[1:], string2[index+1:])
        else:
            print("did not find {} in {}".format(letter,string2))
            return False



def main():
    string1 = "i"
    string2 = "team"
    if is_subsequence(string1, string2):
        print("{} is a subsequence of {}".format(string1,string2))
    else:
        print("{} is not a subsequence of {}".format(string1,string2))

if __name__ == "__main__":

    main()