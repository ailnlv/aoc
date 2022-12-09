 import sys
 import re

 root = dict(files=0, children=dict())
 curr = root
 for line in sys.stdin.readlines():
     line = line.strip()
     if line == "$ cd /":
         curr = root
     elif line.startswith("$ cd"):
         curr = curr['children'][line.split(' ')[-1]]
     elif line.startswith("dir"):
         curr['children'][line.split(" ")[-1]] = {'files': 0, 'children': {'..': curr}}
     elif re.match("^\d+", line):
         curr['files'] += int(line.split(" ")[0])
     elif line.startswith("$ ls"): continue
     else:
         print(line)
         break
          
 sum_filtered = 0
 def recurse(node):
     global sum_filtered
     size = node['files'] + sum(recurse(child) for k, child in node['children'].items() if k != "..")
     if size <= 100000: sum_filtered += size
     return size


 print(recurse(root))
 print(sum_filtered)
 
