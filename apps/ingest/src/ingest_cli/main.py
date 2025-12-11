import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ingest",
        description="Ingest Server CLI",
    )

    parser.add_argument("-v", "--version", action="version", version="0.0.0")
    parser.add_argument("-m", "--mode", type=str, help="Mode to run (server| migrate| script)", default="server",
                        required=False)
    args = parser.parse_args()

    sys.stdout.write(f"ingest [running] mode {args.mode}\n")


if __name__ == "__main__":
    main()
