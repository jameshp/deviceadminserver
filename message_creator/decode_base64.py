import base64
import sys

for arg in sys.argv:
    print arg

infile = sys.argv[1]
outfile = sys.argv[1] + ".dat"

dat = base64.b64decode( open( infile, 'rb' ).read() )
print dat

f = open(outfile, 'wb')
f.write(dat)
f.flush()
f.close()


