import sys


def main():
    # Uncomment this block to pass the first stage
    valid_commands = ['exit 0']
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        cmd = input()
        if cmd not in valid_commands:
            sys.stdout.write(f"{cmd}: command not found\n")
            continue
        else:
            if cmd.lower() == 'exit 0':
                break


if __name__ == "__main__":
    main()
