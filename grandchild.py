# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is grandchild program


def main():
    # this function asks the user to enter her/his age
    
    # input
    age = input("Enter your age: ")
    print("")
    
    # process
    try:
        age = int(age)
        if age > 25 and age < 40:
            print("you can date her grandchild")
        else:
            print("you can not date her grandchild")
    except:
        print("This was not an integer")


if __name__ == "__main__":
    main()
