# format is f1:wasd f2:wasd ... fN:wasd
# f# represents frame number and w/a/s/d represent keys pressed
# for example, 500:wd means up and right are pressed on frame 500
# --------------------------------------------------
# tas string
tas = open("polytrack.tas", "r")
# process the tas
iarray = []
for i in tas:
    data = i.split(":")
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
print(iarray)