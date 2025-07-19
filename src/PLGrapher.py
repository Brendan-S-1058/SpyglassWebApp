import sys
import json
import pandas as pd
import matplotlib.pyplot as plt
import os

inputR = sys.stdin.read()
inputL = json.loads(inputR)

print ('inputL: ' + str(inputL), file = sys.stderr)