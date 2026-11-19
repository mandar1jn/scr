from pathlib import Path
import re
import shutil

lib = "AkMusicEngine.a"
srcpath = "AkMusicEngine/"

base = Path("src") / srcpath

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
    # if match:
    #     print(match.group("lib"))
    if match and match.group("lib") == lib:
        matches.add(match.group("obj"))

# print(matches)

for match in matches:
    # print(match)
    files = list(Path("src/Unclassified").glob(f"{'.'.join(match.split('.')[:-1]).split("/")[-1]}.*"))
    assert len(files) == 1, match
    file = files[0]
    target = base / match
    target = target.with_suffix(f".{file.name.split(".")[-1]}")
    # print(target)
    if not target.parent.exists():
        target.parent.mkdir()

    shutil.move(file, target)
    splits = splits.replace(f"Unclassified/{target.name}", f"{srcpath}{match}".replace(".o", f".{file.name.split(".")[-1]}"))
    config = config.replace(f'            Object(NonMatching, "Unclassified/{target.name}"),\n', "")
    print(f'Object(NonMatching, "{f"{srcpath}{match}".replace(".o", f".{file.name.split(".")[-1]}")}"),')

splitsf.write(splits)
configf.write(config)
