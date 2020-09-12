from time import sleep
from packaging import version
import webbrowser

__author__ = "PWRScript"
__version__ = "1.0.0"

try:
    import crafatar
except ModuleNotFoundError:
    print("[CRITICAL ERROR] Can´t import module crafatar because they isn´t installed!")
    print("[CRITICAL ERROR] Try running pip install -U crafatar.py before running this script")
    print("[CRITICAL ERROR] Quitting script in 5 seconds with -130 error (dependency crafatar.py not satisfied)")
    sleep(5)
    quit(-130)
else:
    if version.parse(crafatar.__version__) < version.parse(__version__):
        print("[CRITICAL ERROR] Can´t import module crafatar because they are on a outdated version")
        print("[CRITICAL ERROR] Try running pip install -U crafatar.py before running this script")
        print("[CRITICAL ERROR] Quitting script in 5 seconds with -131 error (dependency crafatar.py has outdated version)")
        sleep(5)
        quit(-131)


run_method = "cli"

cli_board_length = 50
cli_board_characters = "*"

if __name__ == '__main__':
    crafatar_api = crafatar.CrafatarAPIWrapper()

    stop_program = False

    if run_method == "cli":
        while not stop_program:
            selected_option = None
            print(cli_board_characters * cli_board_length)
            print(cli_board_characters + "crafatar.py Tutorial Script (CLI Interface)".center(cli_board_length - 2) + cli_board_characters)
            print(cli_board_characters + f"Library: {crafatar.__version__} | Script: {__version__}".center(cli_board_length - 2) + cli_board_characters)
            print(cli_board_characters + f"Developers/Contributors: {__author__}".center(cli_board_length - 2) + cli_board_characters)
            print(cli_board_characters * cli_board_length)
            print(cli_board_characters + f"What option you want to use?".center(cli_board_length - 2) + cli_board_characters)
            print(cli_board_characters * cli_board_length)
            print(cli_board_characters + "  [1]" + f"Module Structure and Explanation".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [2]" + f"Creating a Basic Script using crafatar.py".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [3]" + f"Use Our Builtin Script".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [4]" + f"What´s New [{crafatar.__version__}]?".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [5]" + f"Github Repository".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [6]" + f"Issue Tracker".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [7]" + f"Documentation".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters + "  [8]" + f"Exit".center(cli_board_length - 7) + cli_board_characters)
            print(cli_board_characters * cli_board_length)
            while selected_option == None:
                try:
                    selected_option = int(input("> "))
                except ValueError:
                    selected_option = None
                    print("[WARNING] Your option must be a number between 1 and 8")
                else:
                    if selected_option < 1 or selected_option > 8:
                        print("[WARNING] Your option must be a number between 1 and 8")
                    else:
                        if selected_option == 1:
                            # TODO Implement Module Structure and Explanation
                            pass
                        elif selected_option == 2:
                            # TODO Implement Creating a Basic Script using crafatar.py
                            pass
                        elif selected_option == 3:
                            # TODO Implement Use Our Builtin Script
                            pass
                        elif selected_option == 4:
                            # TODO Implement What's New
                            pass
                        elif selected_option == 5:
                            webbrowser.open("https://github.com/PWRScript/crafatar.py")
                        elif selected_option == 6:
                            webbrowser.open("https://github.com/PWRScript/crafatar.py/issues")
                        elif selected_option == 7:
                            # TODO Implement documentation link
                            pass
                        elif selected_option == 8:
                            stop_program = True

    if stop_program:
        print("Exiting script with status 0 (ordered by user)")
        quit(0)







