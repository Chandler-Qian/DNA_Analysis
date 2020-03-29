# Name: Yucheng Qian
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0
# Number of A, T, G, C nucleotides
a_count = t_count = g_count = c_count = 0
# Number of all nucleotides count
atgc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        # if the bp is a C
        if bp == 'C':
        	c_count += 1
        # if the bp is a G
        else:
        	g_count += 1
    # if the bp is an A or a T
    if bp == 'A' or bp == 'T':
    	# increment the count of at
    	at_count += 1
    	# if the bp is an A
        if bp == 'A':
        	a_count += 1
        # if the bp is a T
        else:
        	t_count += 1

# count the sum of A, T, G, C
atgc_count = a_count + t_count + g_count + c_count
# divide the gc_count by the total_count
gc_content = float(gc_count) / atgc_count
# divide the at_count by the total_count
at_content = float(at_count) / atgc_count
# Value of at / gc ratio
at_gc_ratio = float(at_count) / gc_count
# Compute the GC category:
if gc_content > 0.6:
	gc_class = 'high GC content'
elif gc_content < 0.4:
	gc_class = 'low GC content'
else:
	gc_class = 'moderate GC content'

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G count:', g_count
print 'C count:', c_count
print 'A count:', a_count
print 'T count:', t_count
print 'Sum count:', atgc_count
print 'Total count:', total_count
print 'seq length:', len(seq)
print 'AT/GC Ratio:', at_gc_ratio
print 'GC Classification:', gc_class