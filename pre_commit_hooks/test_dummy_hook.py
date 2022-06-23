import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--message")
    parser.add_argument("filesnames", nargs="*")
    args = parser.parse_args(sys.argv[1:])
    retval = 0

    message = args.message

    if message == "yes":
        print(f"Hook passed.")
        return retval

    retval = 1
    print("Hook failed.")
    return retval


if __name__ == '__main__':
    raise SystemExit(main())
