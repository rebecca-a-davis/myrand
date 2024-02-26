#!/usr/bin/env python

import argparse
import random
import sys

def getRandInts(numInts, min=-sys.maxsize-1, max=sys.maxsize):
  # generate a given number of integers between the MIN(int) and MAX(int)
  rand_ints = [ random.randint(min, max) for n in range(numInts) ]

  return rand_ints

def prettyPrint(intList, numCols, colWidth):
  # format the numbers in columns so it's a little nicer to read
  for i in range(0, len(intList), numCols):
    for n in intList[i:i+numCols]:
      print(str(n).ljust(colWidth), end=" ")
    print()

# parse user input, generate list of integers, and print them out
def main():
  # command line args (positional for number of ints to print + some optional formatting settings)
  parser = argparse.ArgumentParser(prog="myrand",
                                   description="Generates a given number of random integers")
  parser.add_argument("num_integers", type=int, metavar="NUM", default=1, nargs="?",
                      help="Number of random integers to generate (default 1)")
  parser.add_argument("-p", "--pretty", dest="pretty_print", action="store_true",
                      help="Whether or not to format the output nicely (default is in the form of a raw list)")
  parser.add_argument("-c", "--cols", dest="num_cols", type=int, metavar="COLS", default=5,
                      help="Number of columns to print integers in (default 5); does nothing without '-p/--pretty'")
  parser.add_argument("-w", "--width", dest="col_width", type=int, metavar="COLWIDTH", default=25,
                      help="Width, in characters, of each column (default 25); does nothing without '-p/--pretty'")
  # this option is just here for help2man to generate the manpage
  parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0", help=argparse.SUPPRESS)
  args = parser.parse_args()

  # validate input values
  if args.num_integers < 1:
    parser.error("Minimum number of integers to generate is 1")
  if args.num_cols < 1:
    parser.error("Minimum number of columns is 1")
  if args.col_width < 1:
    parser.error("Minimum column width is 1")

  # generate the list of integers
  rand_ints = getRandInts(args.num_integers)

  # format the integers nicely so they're easier to read
  if args.pretty_print:
    prettyPrint(rand_ints, args.num_cols, args.col_width)
  else:
    print(rand_ints)

main()
