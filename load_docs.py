import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

vision = load_json("vision.json")
brd = load_json("BRD.json")
nfr = load_json("NFR.json")

print("Vision:", vision["project_name"])
print("BRD requirements:", len(brd["business_requirements"]))
print("NFR security:", nfr["security"])
