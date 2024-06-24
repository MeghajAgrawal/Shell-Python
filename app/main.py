import sys


def main():
    # Uncomment this block to pass the first stage
    valid_commands = ['echo', 'exit', 'type']
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
                if args[1] in valid_commands:
                    sys.stdout.write(f"{args[1]} is a shell builtin\n")
                else:
                    sys.stdout.write(f"{args[1]}: not found\n")
            else:
                sys.stdout.write(f"{cmd}: command not found\n")
        continue

if __name__ == "__main__":
    main()
