from sys import argv
import argparse

parser = argparse.ArgumentParser(
    description = "This is a sum calculator"
)
parser.add_argument(nargs = 5, required = True)
c = 0
for arg in argv:
 print(arg)
 c += 1
print(f"Number of args is {c}")