import os
import shutil
import subprocess
import platform
import functions



width = shutil.get_terminal_size().columns

""" PRIMARY FUNCTION ====================================================== """

""" PRINTED BLOKS ---------------------------------------"""

menu = '''|    1      | - go to a folder 
|    2      | - make a folder 
|    3      | - remove a folder
|    4      | - open file
|    exit   | - to exit '''

go_down_menu = ''' Chose an option: 
 up - to go up
 down - to go down'''

go_down_chose = ''' Chose an option:
 full - for full path
 short - for short path
 0 - to go back'''


def main():
    while True:
        functions.print_line("=")
        print(' current folder is ' + functions.wim())
        print("-" * width)
        print(' files in curent folder is: ')
        print("-" * width)
        functions.list_files()
        print("=" * width)
        print(menu)
        print("-" * width)
        option = input(' print choosen option: ').strip()

        if option == '1':
            print(go_down_menu)
            option_1 = input('Your option: ').strip()
            if option_1 == 'up':
                functions.go_up()
            elif option_1 == 'down':
                print(go_down_chose)
                option_2 = input('Your option: ').strip()

                if option_2 == 'full':
                    path = input(' Give me a path: ').strip()
                    functions.change(path)
                if option_2 == 'short':
                    path = input(' Give me a name: ').strip()
                    functions.change_short(path)
                if option_2 == '0':
                    continue
                else:
                    print('Error: invalid option')
        elif option == '2':
            functions.new_folder()
        elif option == '3':
            functions.remove_folder()
        elif option == '4':
            file_name = input('Give me a name: ')
            functions.openfile(file_name)
        elif option == 'exit':
            print(' Exiting program.')
            break
        else:
            print(' Error: invalid option')


if __name__ == "__main__":
    main()


"""
wim()

path = input("give me a path: ").strip()

change_short(path)
"""
