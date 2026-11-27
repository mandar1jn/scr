# Use objdump -W to get the required file

paths = list()

f = open("out.txt", "rt")
lines = [line.strip() for line in f.readlines()]

idx = 0

def parse_table():
    global lines
    global idx
    idx += 1

    dirs = dict()

    while True:
        line = lines[idx]
        idx += 1

        if line == "":
            break

        parts = [part.strip() for part in line.split("\t")]
        dirs[int(parts[0])] = parts[1]

    assert("The File Name Table" in lines[idx])
    idx += 1
    assert("Entry\tDir" in lines[idx])
    idx += 1

    while True:
        line = lines[idx]
        idx += 1

        if line == "":
            break

        parts = [part.strip() for part in line.split("\t")]
        if int(parts[1]) != 0:
            paths.append(dirs[int(parts[1])] + parts[-1])

while idx < len(lines):
    line = lines[idx]
    if "DW_AT_name" in line and ("/" in line or "\\" in line) and not "__sinit_\\" in line and not "(float)" in line:
        paths.append(line.split(": ")[-1])
        idx += 1
    elif "The Directory Table" in line:
        parse_table()
    else:
        idx += 1

def rep(path):
    path = path.replace("\\", "/")
    path = path.replace("Y:/goliath/SDK/", "")
    path = path.replace("Y:/SKY2015_Main/SDK/", "")
    path = path.replace("wii/cw_v1.7/", "")
    path = path.replace("Y:/sky2015-3ds-wii/goliath/SDK/", "")
    path = path.replace("Y:/SKY201~1/goliath/SDK/Wii/", "")
    path = path.replace("Y:/SKY2015_Main/", "")
    path = path.replace("C:/Jenkins/workspace/Goliath_0/SDK/wii/", "")
    path = path.replace("C:/Program Files (x86)/Freescale/CW for Wii v1.2/", "")
    path = path.replace("C:/SDK/Wii/CW for Wii v1.2/", "")
    path = path.replace("C:/Program Files (x86)/Freescale/CW for Wii v1.7/", "")
    return path

for path in sorted(list(set([rep(path) for path in paths]))):
    print(path)
