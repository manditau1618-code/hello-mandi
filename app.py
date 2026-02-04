#!/usr/bin/env python3
"""Simple hello app by Mandi"""

def greet(name: str = "World") -> str:
    return f"Hello, {name}! 🦊"

def main():
    print(greet())
    print(greet("Sam"))
    print("Mandi can build apps!")

if __name__ == "__main__":
    main()
