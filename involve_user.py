# Write a method in python to write multiple line of text contents into a text file.

# open myfriends.txt(append)
with open("my_friends.txt", "a") as life_friends:
    add = "yes"
    # loop to keep adding next 
    while add.lower() == "yes":
        # ask for input
        friends = input("Enter a name of your friend: ")
        # write the input in the file
        life_friends.write(friends + "\n")
        # ask if there's more
        add = input("Are there more lines? ")
