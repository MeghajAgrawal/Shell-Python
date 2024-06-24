import sys
import os

def main():
    # Uncomment this block to pass the first stage
    valid_commands = ['echo', 'exit', 'type']
    PATH = os.environ.get('PATH')
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        if cmd := input():
            args = cmd.split(' ')
            if args[0] == 'exit':
                break
            elif args[0] == 'echo':
                msg = cmd[len("echo "):]
                sys.stdout.write(f"{msg}\n")
            elif args[0] == 'type':
                cmd_path = None
                paths= PATH.split(":")
                for path in paths:
                    if os.path.isfile(f"{path}/{args[1]}"):
                        cmd_path = f"{path}/{args[1]}"
                if args[1] in valid_commands:
                    sys.stdout.write(f"{args[1]} is a shell builtin\n")
                elif cmd_path:
                    sys.stdout.write(f"{args[1]} is {cmd_path}\n")
                else:
                    sys.stdout.write(f"{args[1]}: not found\n")
            else:
                sys.stdout.write(f"{cmd}: command not found\n")
        continue

if __name__ == "__main__":
    main()
