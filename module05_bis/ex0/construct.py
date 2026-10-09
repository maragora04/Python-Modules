import os
import sys
import site



def in_environ() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if in_environ():
        print("\nLABORATORY STATUS: The laboratory is sealed\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.\n")

        print("Reagent installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nLABORATORY STATUS: You are working in the open\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system\n")

        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")

        print("Then run this program again")

if __name__ == "__main__":
    main()

# python3 -m venv lab_env
# source lab_env/bin/activate
# python3 ex0/construct.py