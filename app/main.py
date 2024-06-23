import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        if cmd := input():
            if cmd.lower() == 'exit 0':
                break
            elif 'echo' in cmd.lower():
                msg = cmd[len("echo "):]
                sys.stdout.write(f"{msg}" + "\n")
            else:
                sys.stdout.write(f"{cmd}: command not found\n")
        continue

if __name__ == "__main__":
    main()
