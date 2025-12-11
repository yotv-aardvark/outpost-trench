"""Main module for the application."""

import argparse
import sys


def main() -> None:
    """Generate and print a Fibonacci sequence based on command line arguments."""

    parser = argparse.ArgumentParser(
        prog="ingest",
        description="Generate a Fibonacci sequence up to the given number of terms",
    )

    parser.add_argument("-v", "--version", action="version", version="0.0.0")
    parser.add_argument("n", type=int, help="The number of terms")
    args = parser.parse_args()

    # sequence = fibonacci_sequence(args.n)
    sys.stdout.write(args)


if __name__ == "__main__":
    main()
