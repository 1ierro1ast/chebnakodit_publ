import random
import json

def getIdea():
    with open("src/db.json", "r", encoding="UTF-8") as data:
        ideas = json.load(data)
        return random.choice(ideas["ideas"])

def postIdea(idea):
    with open("db.json","r", encoding="UTF-8") as db:
        database = json.load(db)
        database["ideas"].append(idea)
    with open("db.json","w", encoding="UTF-8") as db:
        json.dump(database,db,ensure_ascii=False,indent=4)

def ideasToDB():
    with open("ideas.txt", "r", encoding="UTF-8") as ideas:
        ideasList = ideas.read()
        ideasList = ideasList.split("\n")

    with open("db.json","r", encoding="UTF-8") as db:
        database = json.load(db)
        database["ideas"].extend(ideasList)
    with open("db.json","w", encoding="UTF-8") as db:
        json.dump(database,db,ensure_ascii=False,indent=4)
