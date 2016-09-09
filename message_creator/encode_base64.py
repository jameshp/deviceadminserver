import base64
import sys

infile = sys.argv[1]
outfile = sys.argv[1] + ".b64"

b64 = base64.b64encode( open( infile, 'rb' ).read() )
print b64

f = open(outfile, 'wb')
f.write(b64)
f.flush()
f.close()


