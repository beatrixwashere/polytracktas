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
# encode inputs
tas_size = len(tas)
t = bytearray(math.ceil(3.5 * tas_size))
for e in range(tas_size):
    n = int(tas[e].rstrip("\n").split(":")[0])
    t[3 * e] = n & 255
    t[3 * e + 1] = (n >> 8) & 255
    t[3 * e + 2] = (n >> 16) & 255
for e in range(0, tas_size, 2):
    n = tas[e].rstrip("\n").split(":")[1]
    i = 0
    i |= 1 if "w" in n else 0
    i |= (1 if "d" in n else 0) << 1
    i |= (1 if "s" in n else 0) << 2
    i |= (1 if "a" in n else 0) << 3
    if e + 1 < tas_size:
        t_frame = tas[e + 1].rstrip("\n").split(":")[1]
        i |= (1 if "w" in t_frame else 0) << 4
        i |= (1 if "d" in t_frame else 0) << 5
        i |= (1 if "s" in t_frame else 0) << 6
        i |= (1 if "a" in t_frame else 0) << 7
    t[3 * tas_size + math.floor(e / 2)] = i
compressed_data = zlib.compress(t, level=9)
encoded_data = base64.b64encode(compressed_data).decode('utf-8')
encoded_data = encoded_data.rstrip('=')  # remove trailing equal signs
encoded_data = encoded_data.replace('/', '_')  # replace slashes with underscores
# print ghost
print(encoded_data)
