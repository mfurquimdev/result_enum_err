"""Main script"""

import os


def main():
    """Main function"""
    subject = os.getenv("SUBJECT", "World")
    print(f"Bye, {subject}!")


if __name__ == "__main__":
    main()
