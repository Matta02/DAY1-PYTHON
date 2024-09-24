import os

name = os.getenv("NAME", "World")

def main():
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

