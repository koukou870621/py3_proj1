#!/usr/bin/python3
# elpy-autopep8-fix-code
def main():
    i = 0
    j = 0
    k = 0
    print("\n")
    i = 1
    while i < 5:
        j = 1
        while j < 5:
            k = 1
            while k < 5:
                if i != k and i != j and j != k:
                    print("%d,%d,%d" % (i, j, k))
                k += 1
            j += 1
        i += 1


if __name__ == "__main__":
    main()
