import sys, os, glob, platform, webbrowser,logging, datetime,zipfile
from termcolor import  colored
from colorama import  Fore, Back,Style
from terminal_functions import  *
current_working_directory = os.getcwd()
current_working_directory = colored(current_working_directory, 'yellow', 'on_grey')
import shutil

LOG_FILENAME = 'errors.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)



if __name__ == "__main__":
    print(Fore.YELLOW+"PyTEmulator  >>> Python Terminal Emulator")
    current_version()
    print(str(datetime.datetime.now()))
    print(Style.RESET_ALL)
    
    while True:


        query = input(os.getcwd() + '@user>')
        if isinstance(query, str):
            if 'print' in query:
                query = query.replace('print', '')
                TEXT = query
                print(Fore.YELLOW+TEXT)
                print(Style.RESET_ALL)
            elif 'exit' in query:

                print(Fore.RED + "Exiting Now ...")
                print(Style.RESET_ALL)
                sys.exit()
            elif 'open ' in query:
                query = query.replace('open', '')
                if 'notepad' in query:

                    if platform.system() == 'Windows':

                        os.startfile("C:\\Windows\\System32\\notepad.exe")
                    else:
                        print("Make Sure you are Windows Platform")
                        
                if  'site' in query:
                    site = query.replace('site', '')
                    webbrowser.open(site)

                else:
                    print(Fore.RED + "Something Went Wrong...")
            elif 'check' in query:
                query = query.replace('check', '')
                if 'ping' in query:
                    host = input('Enter Host: ')
                    NO_OF_PACKETS = 10
                    ping(host, str(NO_OF_PACKETS))
                if 'internet' in query:
                    internet_connection_status()
                elif 'ip' in query:
                    show_ip()


            elif 'read' in query or 'cat' in query:
                query = query.replace('read', " ")
                file_name = query.lstrip()
                read_file(file_name)
                 
           
                 

            elif  'getcwd' in query:
                print(Fore.YELLOW+current_working_directory)
                print(Style.RESET_ALL)
            elif 'cd' in query:
                query = query.replace("cd", ' ')
                path = query.lstrip()
                full_path = os.path.join(path,current_working_directory,path)
                if os.path.exists(path):
                    change_directory(path)
                elif os.path.exists(full_path):
                    change_directory(full_path)
                else:
                    print(Fore.RED + "Error >>> The specified path does not exist.")
                    print(Style.RESET_ALL)

            elif 'help' in query:
                help_screen()

            elif 'clear' in query or 'cls' in query:
                os.system('cls' if os.name == 'nt' else 'clear')

            elif 'dirs' in query or 'ls' in query:
               list_directories()
            elif 'run' in query:
                file_name = query.replace('run', '')
                file_name = file_name.lstrip()
                run_script(file_name)
            elif 'mkdir' in query or 'folder' in query:
                    directory_name = query.replace('mkdir', ' ')
                    directory_name = directory_name.lstrip()
                    create_directory(directory_name)
            elif 'create' in query:
                file_name = query.replace('create',' ')
                file_name = file_name.lstrip()
                create_file(file_name)
                     
      
            
            elif  'remove' in query:
                
                query = query.replace('remove', ' ')
                file_name = query.lstrip()
            
                remove_file_or_directory(file_name)
            elif 'unzip' in query:
                query = query.replace('unzip', ' ')
                query = query.lstrip()
                unzip_file(query)
            elif  'move' in query:
                move_file()
             

            




            elif 'admin'  in query:
                run_as_admin()
            elif query == "":
                print("") 
            else:
                print(Fore.RED + "Error >>> No Such Command Found")
                print(Style.RESET_ALL)

