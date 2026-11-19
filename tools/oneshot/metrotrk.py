import re
from pathlib import Path
import shutil

mapf = open("orig/SKNE52/files/goliath.engine.wii.profile.MAP", "rt")
splitsf = open("config/SKNE52/splits.txt")
configf = open("configure.py")

splits = splitsf.read()
splitsf.close()
config = configf.read()
configf.close()

splitsf = open("config/SKNE52/splits.txt", "w")
configf = open("configure.py", "w")

reg = r"metrotrk\\(?!metrotrk\\)([^\\]\\)*\S+\.o$"
mapdata = mapf.readlines()

matches = set()

for line in mapdata:
    match = re.search(reg, line.strip())
    if match:
        matches.add(match.group())

matches = [match.split("metrotrk\\")[1].replace("\\", "/") for match in matches]

base = Path("src/MetroTRK")

for match in matches:
    files = list(Path("src/Unclassified").glob(f"{match.split('.')[0].split("/")[-1]}.*"))
    assert len(files) == 1
    file = files[0]
    target = base / match
    target = target.with_suffix(f".{file.name.split(".")[1]}")
    if not target.parent.exists():
        target.parent.mkdir()

    shutil.move(file, target)
    splits = splits.replace(f"Unclassified/{target.name}", f"MetroTRK/{match}".replace(".o", f".{file.name.split(".")[1]}"))
    config = config.replace(f'            Object(NonMatching, "Unclassified/{target.name}"),\n', "")
    print(f'Object(NonMatching, "{f"MetroTRK/{match}".replace(".o", f".{file.name.split(".")[1]}")}"),')

splitsf.write(splits)
configf.write(config)
