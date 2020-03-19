#!/usr/bin/env python3

import sys
with open(sys.argv[1]) as f:
    apps_data = f.read()

with open(sys.argv[2]) as f:
    adv_data = f.read()

# Find all the data
# the application whent us to cross-check
# They are on for the form advisor__{name} {value}

d_aps = {}
import re
for m in re.finditer(r"advisor__(.*?)\s+(.*)", apps_data):
    name = m.groups()[0]
    value = float(m.groups()[1])
    d_aps[name] = value

# Will print the data for all the opencl gpu call.
# We should ask for a kernel name.
# For now, I'm lazy, I will take the last one and hope for the best
d_adv = {}
for m in re.finditer(rf"({'|'.join(d_aps)}).*?\s+(.*)", adv_data):
   a = m.groups()
   name = m.groups()[0]
   value = float(m.groups()[1])
   d_adv[name] = value

import math
working  = True
print ("Name, Application, Advisor, is in 10 %")
# Now just need to compare number
for k in set(d_aps) | set(d_adv):
    aps = d_aps[k]
    adv = d_adv[k]
    print (k, aps, adv, math.isclose(aps,adv,rel_tol=0.1) )
    if not ( math.isclose(aps,adv,rel_tol=0.1)):
        working = False

if not working:
    sys.exit("Advisor don't math application hand count")
