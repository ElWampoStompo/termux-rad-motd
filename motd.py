#!/usr/bin/env python3
import datetime

def main():
    print("Welcome to Termux!")
    print(f"Today is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Have a great day!")

if __name__ == "__main__":
    main()