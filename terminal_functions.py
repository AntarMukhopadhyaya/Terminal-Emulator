#!python
# coding: utf-8
from colorama import  Fore,Back,Style
import platform,zipfile,shutil
import subprocess
import socket
import os
import ctypes
import sys

current_working_directory = os.getcwd()




def help_screen():
    print("\n"+Fore.YELLOW+ " print    >>>>    Prints string in the Terminal \n")
    print(" clear   >>>>    Clear the Terminal Screen \n")
    print(" mkdir    >>>>  Create a directory \n")
    print(" help   >>>>     Print this help screen \n")
    print(" exit    >>>>     Exit this Terminal \n")
    print(" read    >>>>    Read the specified file\n")
    print(" getcwd   >>>>   Print the Current Working Directory\n")
    print(" version   >>>>    Prints the version of  Terminal\n")
    print("check ping >>>   Checks your Ping and Prints it to the screen\n")
    print("check internet >>>   Check internet\n")
    print("check ip >>>   Prints ipV4 and hostname\n")
    print("remove >>>   Remove specified file\n")
    print("move  >>>   Move specified file\n")

    print(Style.RESET_ALL)



def current_version():
    version = '1.0'
    print(f'Current Version: {version}')


def ping(host, no_of_packets):
    """Get The Ping"""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, no_of_packets, host]
    return subprocess.call(command) == 0


def list_directories():
    try:
        dirs = os.listdir()
        print(*dirs, sep=', ')
    except (FileNotFoundError, PermissionError) as e:
        print(Fore.RED+"Error >>> " + e)
        print(Style.RESET_ALL)


def read_file(file_name):
    file_path = os.path.join(file_name,current_working_directory,file_name)
    if os.path.isfile(file_path):
        file_content = open(file_name,'r+')
        file_size = os.path.getsize(file_path)
        file_size =  str(file_size)
        print(f"*************** File: {file_name} & Size:{file_size} Bytes ****************** \n")
        print(file_content.read())
        file_name.close()
    else:
        print(Fore.RED+"Error >>> The specified file does'nt exist.")
        print(Style.RESET_ALL)
    


def internet_connection_status(host="8.8.8.8", port=53, timeout=3):
    """Checking Internet Connectivity"""

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print(Fore.YELLOW+"Internet Connectivity Detected")
        print(Style.RESET_ALL)
    except  socket.error as e:
    
        print(" Make Sure you are connected to internet")

def run_script(file_name):
    """ Run Scripts"""
    extension = os.path.splitext(file_name)
    if '.py' in extension:
        current_working_directory = os.getcwd()
        full_path = str(current_working_directory)+ "\\\\"+file_name
        
        command = ['python', full_path]
    elif '.c' in extension:
        current_working_directory = os.getcwd()
        full_path = str(current_working_directory)+ "\\\\"+file_name
        print(file_name)
        print(full_path)
        command = ['gcc', full_path]

    return subprocess.call(command) == 0

def create_directory(directory_name):
    """ Create Directory"""
    if  os.path.isdir(directory_name):
        print(Fore.RED + "Error >>> Directory already exists.")
        print(Style.RESET_ALL)
    else:
        os.mkdir(directory_name)





def launch_vim(file_name):
    """ Launch Vim """
    command = ['vim', file_name]
    return subprocess.call(command) == 0

def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
     
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


def remove_file_or_directory(file_name):
 
    full_path = os.path.join(file_name,current_working_directory,file_name)
    
    if os.path.isfile(full_path):
        os.remove(full_path)
    elif os.path.isdir(full_path):
        os.rmdir(full_path)
    else:
        print("Error >> The specified file or directory doesn't exist.")
    
   
def show_ip():
    """ Shows Ip"""
    hostname = socket.gethostname()
    ip_v4 = socket.gethostbyname(hostname)
    print(f"PC name: {hostname}")
    print(f'IpV4 Address: {ip_v4}')


def create_file(file_name):
    file_path = os.path.join(file_name,current_working_directory,file_name)

    if os.path.isfile(file_path):
        print(" Warning:  >>>  File already exists. Write existing file ?")
    else:
        f = open(file_name, "a")
        print(f"***************** File: {file_name}  & Mode: Write *****************  \n")
        file_content = str(input(""))
        file_size = os.path.getsize(file_name)
        try:
          
            f.write(file_content)
            f.close()
        except  Exception as e:
            print("Error >>>"+ e)

def unzip_file(query):
    if "current_dir" in query:
        file_name = query.replace('current_directory', '')
        file_name = file_name.lstrip()
        print(file_name)
        file_path = os.path.join(file_name, current_working_directory,file_name)
        if os.path.isfile(file_path):
            try:
                with zipfile.ZipFile(file_name, 'r') as zip_ref:
                    zip_ref.extract(current_working_directory)
            except  Exception as e:
                print(f"Error >>> {e}")
        else:
            print("Error >>> Specified File does'nt exists.")


def move_file():
        file_name = str(input("Enter the file name you want to move: "))
        move_path = str(input("Destination Path: "))
        full_path = os.path.join(file_name,current_working_directory,file_name)
        if os.path.exists(full_path):
            try:
                shutil.move(full_path, move_path)
            except  Exception as e:
                print(f"Error >>> {e} ")
        else:
            print("Error >>> File does not exists.")

def change_directory(path_name):
    try:
        os.chdir(path_name)
    except  Exception as e:
        print(f"Error >>> {e} ")
    
     
