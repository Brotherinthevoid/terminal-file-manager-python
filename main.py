import os
import shutil
import subprocess
import platform



width = shutil.get_terminal_size().columns

""" PRIMARY FUNCTION ====================================================== """

def wim():
    cwd = os.getcwd()
    print("U are in: ", cwd)
    return cwd

def change(path_to_go):
    if os.path.isdir(path_to_go):
        print("u are go to: ", path_to_go)
        print("=" * width)
        os.chdir(path_to_go)
        wim()
    else:
        print("Error 001: Not valid directory")

def change_short(path_for_short):
    current_path = wim()
    full_path = os.path.join(current_path, path_for_short) #  обьединение путей через библиотеку

    if os.path.isdir(full_path):
        print("u are go to: ", path_for_short)
        print("=" * width)
        os.chdir(full_path)
        wim()
    else:
        print("Error 001: Not valid directory")

def go_up():
    print("go up for 1 directory ")
    print("=" * width)
    os.chdir('../')
    wim()

def list_files():
    files = os.listdir()
    if not files:
        print(' Folder is empty')
    else:
        for file in files:
            print(f"📂 {file}" if os.path.isdir(file) else f"📄 {file}")

def new_folder():
    folder_name = input('Enter new folder name: ').strip()
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder {folder_name} created ✅")
    except Exception as error:
        print_error(error)

def remove_folder():
    folder_name = input(" Enter folder name to remove: ").strip()
    if os.path.isdir(folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Folder {folder_name} has been removed 🗑️")
        except Exception as error:
            print_error(error)
    else:
        print_error(" Folder does not exist")

def openfile(file_name):
    if not os.path.isfile(file_name):
        print("❌ Error: File does not exist")
        return

    try:
        if platform.system() == "Windows":
            os.startfile(file_name)  # Открытие в стандартном приложении (Windows)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", file_name])
        else:  # Linux
            subprocess.run(["xdg-open", file_name])
        print(f"📂 Opening {file_name}...")
    except Exception as e:
        print(f"❌ Error: {e}")

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

""" SECONDARY FUNCTION ----------------------------------"""

def print_line(char):
    print(char * width)

def print_error(msg):
    print(f" 🚨 Error: {msg}")

""" ================================================= """

def main():
    while True:
        print_line("=")
        print(' current folder is ' + wim())
        print("-" * width)
        print(' files in curent folder is: ')
        print("-" * width)
        list_files()
        print("=" * width)
        print(menu)
        print("-" * width)
        option = input(' print choosen option: ').strip()

        if option == '1':
            print(go_down_menu)
            option_1 = input('Your option: ').strip()
            if option_1 == 'up':
                go_up()
            elif option_1 == 'down':
                print(go_down_chose)
                option_2 = input('Your option: ').strip()

                if option_2 == 'full':
                    path = input(' Give me a path: ').strip()
                    change(path)
                if option_2 == 'short':
                    path = input(' Give me a name: ').strip()
                    change_short(path)
                if option_2 == '0':
                    continue
                else:
                    print('Error: invalid option')
        elif option == '2':
            new_folder()
        elif option == '3':
            remove_folder()
        elif option == '4':
            file_name = input('Give me a name: ')
            openfile(file_name)
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
