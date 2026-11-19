from pathlib import Path
import re

lib = "os.a"
base = Path("src/RVL_SDK/os")

mapf = open("orig/SKNE52/files/goliath.engine.wii.profile.MAP", "rt")
splitsf = open("config/SKNE52/splits.txt")
configf = open("configure.py")

splits = splitsf.read()
splitsf.close()
config = configf.read()
configf.close()

splitsf = open("config/SKNE52/splits.txt", "w")
configf = open("configure.py", "w")

reg = r"found in (?P<lib>.*\.a) (?P<obj>.*\.o)$"
mapdata = mapf.readlines()

matches = set()
for line in mapdata:
    match = re.search(reg, line.strip())
    if match and match.group("lib") == lib:
        matches.add(match.group("obj"))

print(matches)

splitsf.write(splits)
configf.write(config)
