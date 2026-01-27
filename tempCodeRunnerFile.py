def split_and_join():
    # s=input("Enter a string: ")
    with open("PEPCLASS/input.txt", "r") as file:
        s = file.read()
    words=s.split(" ")
    print(words)
    # if there in multiple spaces then use filter
    words = list(filter(None, words))
    joinwords="-".join(words)
    print(joinwords)