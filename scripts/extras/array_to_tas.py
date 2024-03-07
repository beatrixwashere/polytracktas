# input array
iarray = [{'frame': 0, 'controls': {'up': True, 'left': False, 'down': False, 'right': False}}, {'frame': 500, 'controls': {'up': True, 'left': False, 'down': False, 'right': True}}, {'frame': 600, 'controls': {'up': True, 'left': False, 'down': False, 'right': False}}, {'frame': 1200, 'controls': {'up': False, 'left': True, 'down': True, 'right': False}}, {'frame': 1500, 'controls': {'up': True, 'left': False, 'down': False, 'right': False}}]
# process the array
tas = ""
for i in iarray:
    tas += str(i['frame']) + ","
    if i['controls']['up']: tas += "w"
    if i['controls']['left']: tas += "a"
    if i['controls']['down']: tas += "s"
    if i['controls']['right']: tas += "d"
    tas += "\n"
outputfile = open("output.tas", "w")
outputfile.write(tas)
print(tas)
