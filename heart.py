import time
import sys

def print_heart():
    message = "I Love You  Boishakhi"
    print("\n" * 3)
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")
        time.sleep(0.2)

    time.sleep(1)
    sys.stdout.write("\n" * 2 + message.center(20, " ") + "\n")
    sys.stdout.write("❤️ " * 7 + "\n")

if __name__ == "__main__":
    print_heart()
