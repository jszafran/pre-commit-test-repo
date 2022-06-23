import argparse
import pathlib
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message")
    args = parser.parse_args(sys.argv[1:])
    retval = 0

    path = pathlib.Path(args.filepath)
    path.touch(exist_ok=True)
    message = args.message

    if message == "yes":
        print(f"Hook passed.")
        return retval

    retval = 1
    print("Hook failed.")
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
