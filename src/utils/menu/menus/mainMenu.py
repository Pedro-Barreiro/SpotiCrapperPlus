import utils.menu.functions.mainMenuFunctions as mainMenuFunctions
from main import main


def mainMenu():
    print("Welcome to SpotiScrapper+!")
    print("1. Scrape Playlist from Spotify")
    print("2. Scrape Album from Spotify")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mainMenuFunctions.choice1()

    elif choice == "2":
        mainMenuFunctions.choice2()

    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice!")
        main()
