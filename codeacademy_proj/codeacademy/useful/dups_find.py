__author__ = 'wrajnees'
import sys
import traceback
from collections import defaultdict
import datetime
import re
"""
Finds duplicate lines in the list of lines.
If pattern is provided, it behaves like grep with -n (show line numbers) option.
"""
def find_dups(lines, pattern):
    start_time = datetime.datetime.now()
    print "Start time: %s" %(start_time)
    lines_with_dups = {}
    lines_with_dups_line_no = defaultdict(list)
    dup_indices = []
    for index, line in enumerate(lines):
        if not pattern:
            pattern = ".*"
        match = re.search(pattern, line)
        if not dup_indices.__contains__(index) and line.strip() != '' and match:
            for j, other_line in enumerate(lines[index + 1:]):
                other_line_index = index + 1 + j
                if not dup_indices.__contains__(other_line_index) and line == other_line:
                    dup_indices.append(other_line_index)
                    if lines_with_dups.has_key(line):
                        dups_count = lines_with_dups.get(line)
                        lines_with_dups[line] = dups_count + 1
                        lines_with_dups_line_no[line].append(other_line_index + 1)
                    else:
                        lines_with_dups[line] = 1
                        lines_with_dups_line_no[line].append(index + 1)
                        lines_with_dups_line_no[line].append(other_line_index + 1)
            # print duplicates
            if lines_with_dups_line_no.has_key(line):
                print line, " --> ", lines_with_dups_line_no[line]
    end_time = datetime.datetime.now()
    print "End time: %s" %(end_time)
    print "It took %s to find duplicates." % (str(end_time - start_time))

def main(argv):
    if len(argv) < 1:
        print "Usage: ./dups_find.py <file> [<regex pattern>]"
        sys.exit(1)

    try:
        f = open(argv[0],"r")
        lines = f.readlines()
        patterns = None
        if len(argv) > 1:
            patterns = argv[1]
        find_dups(lines, patterns)
        f.close()
    except IOError:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])