#!/usr/bin/env python3
"""
hello.py - A multilingual greeting script with command-line options.

Features:
- Custom greetings with --name flag
- Multiple language support (en, fr, es, de, ja) with --lang flag
- Optional timestamp display with --time flag

Usage:
    python hello.py                    # Default: Hello, World!
    python hello.py --name Alice      # Hello, Alice!
    python hello.py --name Bob --lang fr  # Bonjour, Bob!
    python hello.py --name Carol --time   # Hello, Carol! [timestamp]
"""

import argparse
from datetime import datetime


# Greeting translations dictionary
GREETINGS = {
    "en": "Hello",
    "fr": "Bonjour",
    "es": "Hola",
    "de": "Hallo",
    "ja": "こんにちは"
}


def get_greeting(name: str, lang: str = "en", show_time: bool = False) -> str:
    """Generate a greeting message."""
    greeting = GREETINGS.get(lang, GREETINGS["en"])
    message = f"{greeting}, {name}!"
    
    if show_time:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message += f" [{timestamp}]"
    
    return message


def hello(name: str = "World", lang: str = "en", show_time: bool = False) -> str:
    """Main hello function."""
    return get_greeting(name, lang, show_time)


def main():
    """Parse command-line arguments and display greeting."""
    parser = argparse.ArgumentParser(
        description="A multilingual greeting script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Hello, World!
  %(prog)s --name Alice              # Hello, Alice!
  %(prog)s --name Bob --lang fr      # Bonjour, Bob!
  %(prog)s --name Carol --time       # Hello, Carol! [2024-01-15 10:30:00]
  %(prog)s --lang es --name Diana    # Hola, Diana!

Supported languages: en (English), fr (French), es (Spanish), de (German), ja (Japanese)
        """
    )
    
    parser.add_argument("-n", "--name", type=str, default="World",
                        help="Name to greet (default: World)")
    parser.add_argument("-l", "--lang", type=str, choices=["en", "fr", "es", "de", "ja"],
                        default="en", help="Language for greeting (default: en)")
    parser.add_argument("-t", "--time", action="store_true",
                        help="Show current timestamp with greeting")
    
    args = parser.parse_args()
    print(hello(name=args.name, lang=args.lang, show_time=args.time))


if __name__ == "__main__":
    main()
