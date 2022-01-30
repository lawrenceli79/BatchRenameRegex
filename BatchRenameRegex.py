# Rename all files in a folder by regular expression
# Arguments:
#   py BatchRenameRegex.py <pattern> <repl> <folder>
# Exmaples:
#   py BatchRenameRegex.py (.*)_EXPD.xml 10\1_IMP.xml <folder>
#   py BatchRenameRegex.py .*_EXPD.xml 10\g<0> <folder>
# Remark:
#   \1,\2 are the matched parenthesized subgroup
#   \g<0> is the entire match

import sys
import os
import re
  
if (len(sys.argv)<=3):
    print ("Usage:")
    print ("    py {} <pattern> <repl> <folder>".format(os.path.basename(__file__)))
    sys.exit()

strRegex = sys.argv[1]
strRepl = sys.argv[2]
strFolderIn = sys.argv[3]

print("strRegex=" + strRegex)
print("strRepl=" + strRepl)
print("strFolderIn=" + strFolderIn)

p = re.compile(strRegex)

count = 0
for i, filenameOld in enumerate(os.listdir(strFolderIn)):
    filenameNew = p.sub(strRepl, filenameOld)
    if(filenameOld != filenameNew):
        src = strFolderIn + '\\' + filenameOld 
        dst = strFolderIn + '\\' + filenameNew 
        os.rename(src, dst) 
        count = count + 1

print("Renamed Count={}".format(count))
