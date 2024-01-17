import utils.menu.functions.spotifyPostActionMenuFunctions as spotifyPostActionMenuFunctions
import main

def spotifyPostActionMenu(scrapedItem):
    print("Choose an action to do with the scrapped album/playlist:")
    print("1. Import to Youtube playlist")
    print("2. Create JSON file")
    print("3. Back to main menu")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if scrapedItem['type'] == "playlist":
            spotifyPostActionMenuFunctions.choice1Playlist(scrapedItem)
        elif scrapedItem['type'] == "album":
            spotifyPostActionMenuFunctions.choice1Album(scrapedItem)
            
    elif choice == "2":
        if scrapedItem['type'] == "playlist":
            spotifyPostActionMenuFunctions.choice2Playlist(scrapedItem)
        elif scrapedItem['type'] == "album":
            spotifyPostActionMenuFunctions.choice2Album(scrapedItem)
    elif choice == "3":
        main()
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice!")
        main()
