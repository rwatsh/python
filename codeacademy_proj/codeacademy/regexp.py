__author__ = 'rushil'
import re

logLines = []
logLines.append("[31mError executing action `run` on resource 'bash[run_rcu]'ss")

for line in logLines:
    match = re.search("bash\[(\w+)\]", line)
    print match.group()
    if match:
        print match.group(1)