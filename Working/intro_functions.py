def happy():
    print("Happy Birthday to you!")


def sing(person):
    happy()
    happy()
    print("Happy Birthday dear " + person)
    happy()


sing("Fred")
print("")
sing("Lucy")
print("")
sing("Joe")

name = input("Who's birthday is it? ")
sing(name)