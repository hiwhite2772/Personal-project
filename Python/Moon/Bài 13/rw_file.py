def readFile(path:str):
    data = ""
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()
    return data

def writeFile(path:str, data:str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)