import sys
import os

TODO_LIST_PATH = '/home/ahanaf/.conky/ahanaf019/todo.txt'
ADD_ARG = '--add'
REMOVE_ARG = '--rm'
CLEAR_ARG = '--clear'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def help():
    print(f'''USAGE:
            add item: {ADD_ARG} "ITEM"
            remove item: {REMOVE_ARG} INDEX
            clear list: {REMOVE_ARG}''')

if __name__ == '__main__':
    args = sys.argv
    
    if len(args) == 1:
        print(f'{bcolors.BOLD}{bcolors.WARNING}Insufficient arguments.{bcolors.ENDC}')
        help()
        exit(1)
        
    
    elif args[1] == ADD_ARG:
        if len(args) != 3:
            print(f'{bcolors.BOLD}{bcolors.WARNING}Insufficient arguments.{bcolors.ENDC}')
            help()
            exit(1)
        
        with open(TODO_LIST_PATH, 'r') as f:
            lines_count = len(f.readlines())
        with open(TODO_LIST_PATH, 'a') as f:
            f.write(f'{lines_count+1}. {args[2]}\n')
            exit(0)
    
    
    elif args[1] == REMOVE_ARG:
        if len(args) != 3:
            print(f'{bcolors.BOLD}{bcolors.WARNING}Insufficient arguments.{bcolors.ENDC}')
            help()
            exit(1)
            
        with open(TODO_LIST_PATH, 'r') as f:
            lines = f.readlines()
            idx = args[2]
            try:
                idx = int(idx)
                lines.pop(idx - 1)
            except Exception as e:
                print(f'{bcolors.FAIL}Error! Index needs to be a valid integer or index out of range.{bcolors.ENDC}')
        with open(TODO_LIST_PATH, 'w') as f:
            for i, line in enumerate(lines):
                f.write(f'{i+1}. {line.split(". ")[1]}')
            exit(0)
        
        
    elif args[1] == CLEAR_ARG:
        os.remove(TODO_LIST_PATH)
        with open(TODO_LIST_PATH, 'a') as f:
            pass

    else:
        print(f'{bcolors.BOLD}{bcolors.FAIL}Invalid arguments.{bcolors.ENDC}')
        help()
        exit(1)