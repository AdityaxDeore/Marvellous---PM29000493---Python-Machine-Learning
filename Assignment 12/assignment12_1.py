def CheckVowel(Value):
    if Value in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")


def main():
    ch = input("Enter character : ")
    CheckVowel(ch)


if __name__ == "__main__":
    main()
