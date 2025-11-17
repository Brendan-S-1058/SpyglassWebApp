import time
import sys
import json

print ("stalled", file=sys.stderr)
time.sleep (60)
print (json.dumps('res'))