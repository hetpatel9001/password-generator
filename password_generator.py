#!/usr/bin/env python3
"""Generate a random password with the secrets module."""
import argparse
import secrets
import string


def generate(length, symbols=True):
    alphabet = string.ascii_letters + string.digits
    if symbols:
        alphabet += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--length", type=int, default=16)
    p.add_argument("--no-symbols", action="store_true")
    args = p.parse_args()
    print(generate(args.length, symbols=not args.no_symbols))


if __name__ == "__main__":
    main()
