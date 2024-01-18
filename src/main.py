from dotenv import load_dotenv
import utils.menu.index as menu

load_dotenv()


def main():
    while True:
        menu.mainMenu()


if __name__ == "__main__":
    main()
