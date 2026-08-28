import sys


def system_args() -> None:
    i = 1
    arg_len = len(sys.argv) - 1
    print("Program name: ", sys.argv[0])
    if (arg_len == 0):
        print("No arguments provided!")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        while (i <= arg_len):
            print(f"Argument {i}: {str(sys.argv[i])}")
            i += 1


if __name__ == "__main__":
    print("=== Command Quest ===")
    system_args()
