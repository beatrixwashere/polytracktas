# ================ tas_to_ghost.py =================
#         by speedysebas and beatrixwashere
# --------------------------------------------------
# converts your polytrack.tas file to a ghost encode
# ==================================================

# libraries
import math
import zlib
import base64
# open tas file and read each line
tas = open("polytrack.tas", "r").readlines()
# convert tas to input array
iarray = []
for i in tas:
    if i[0] == "#":
        continue
    data = i.split(",")
    iup = False
    ileft = False
    idown = False
    iright = False
    for j in data[1]:
        if j == "w": iup = True
        elif j == "a": ileft = True
        elif j == "s": idown = True
        elif j == "d": iright = True
    iarray.append({'frame': int(data[0]), 'controls': {'up': iup, 'left': ileft, 'down': idown, 'right': iright}})
# encode inputs
t = bytearray(math.ceil(3.5 * len(iarray)))
for e in range(len(iarray)):
    n = iarray[e]
    t[3 * e] = n['frame'] & 255
    t[3 * e + 1] = (n['frame'] >> 8) & 255
    t[3 * e + 2] = (n['frame'] >> 16) & 255
for e in range(0, len(iarray), 2):
    n = iarray[e]
    i = 0
    i |= 1 if n['controls']['up'] else 0
    i |= (1 if n['controls']['right'] else 0) << 1
    i |= (1 if n['controls']['down'] else 0) << 2
    i |= (1 if n['controls']['left'] else 0) << 3
    if e + 1 < len(iarray):
        t_frame = iarray[e + 1]
        i |= (1 if t_frame['controls']['up'] else 0) << 4
        i |= (1 if t_frame['controls']['right'] else 0) << 5
        i |= (1 if t_frame['controls']['down'] else 0) << 6
        i |= (1 if t_frame['controls']['left'] else 0) << 7
    t[3 * len(iarray) + math.floor(e / 2)] = i
compressed_data = zlib.compress(t, level=9)
encoded_data = base64.b64encode(compressed_data).decode('utf-8')
encoded_data = encoded_data.rstrip('=')  # Remove trailing equal signs
encoded_data = encoded_data.replace('/', '_')  # Replace slashes with underscores
# print ghost
print(encoded_data)
