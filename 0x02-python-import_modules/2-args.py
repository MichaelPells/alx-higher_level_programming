#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    print("{:d} {}{}".format(
        len(argv) - 1,
        "argument" if len(argv) == 2 else "arguments",
        "." if len(argv) == 1 else ":"
    ))

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
