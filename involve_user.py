# Write a method in python to write multiple line of text contents into a text file.

# open myfriends.txt(append)
with open("my_friends.txt", "a") as life_friends:
    # loop to keep adding next 
    while add == "yes":
        # ask for input
        friends = input("Enter a name of your friend: ")
        # write the input in the file
        life_friends.write(friends)
        # ask if there's more
