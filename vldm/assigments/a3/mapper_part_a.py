#! /usr/bin/python

# import system functions
import sys

# utility function to split up input file
def read_data_input(file, separator = '\t'):
    for line in file:
        yield line.split(separator)

# define main mapping function        
def main(separator = '\t'):
    data = read_data_input(sys.stdin, separator)
    for words in data:
        print '%s%s%d' % (words[2].lower(), separator, 1)
            
# ensure THIS function runs and not something else
if __name__ == '__main__':
    main()