from sys import argv

script, input_file = argv

# defining the print_a_line function with arguments of line_count and f
def print_a_line(line_count, f):
    # now it's saying to print the first argument, line_count, and read one line from f
    print line_count, f.readline()

# creating a variable (current_file) which opens the file you named in the command line
current_file = open(input_file)

print "Let's print three lines:"

# This gets confusing, I think, because current_line hasn't been defined until now
current_line = 1
# using current_line as the argument in line_count's place
# second argument, f, is being replaced by current_file which opens the whole input file
print_a_line(current_line, current_file)

current_line = current_line + 1
# now we're using the line we're currently on, but adding 1 so current_line is equal to the next code line
# so now it will print what's on the current line (the second line of code) from the input file
print_a_line(current_line, current_file)

current_line = current_line + 1
# and just like last time, we're adding 1 to the current line so we can print the next line
# now we're printing line 3
print_a_line(current_line, current_file)
