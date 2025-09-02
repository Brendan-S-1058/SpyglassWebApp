import time
import sys
import json

time.sleep (60)
print ("stalled", file=sys.stderr)
print (json.dumps('res'))