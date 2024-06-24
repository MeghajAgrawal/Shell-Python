import sys
import os
import subprocess

def main():
    # Uncomment this block to pass the first stage
    valid_commands = ['echo', 'exit', 'type', 'pwd', 'cd']
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
            elif args[0] == 'pwd':
                sys.stdout.write(f"{os.getcwd()}\n")
            elif args[0] == 'cd':
                try:
                    os.chdir(" ".join(args[1:]))
                except FileNotFoundError:
                    sys.stdout.write(f"{args[0]}: {" ".join(args[1:])}: No such file or directory\n")
            else:
                process_path = None
                paths = PATH.split(":")
                for path in paths:
                    file_path = os.path.join(path,args[0])
                    if os.path.isfile(file_path) and os.access(file_path,os.X_OK):
                        process_path = file_path
                if process_path:
                    try:
                        subprocess.run(args)
                    except subprocess.CalledProcessError as e:
                        sys.stderr.write(f"{cmd}: {e}\n")
                else:
                    sys.stdout.write(f"{cmd}: command not found\n")
        continue

if __name__ == "__main__":
    main()
