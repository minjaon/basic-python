import random

while True:
    comp=random.choice(["가위","주먹","보"])
    me=input("안내면 진거 ")
    if comp=="가위":
        if me=="가위": print("비김")
        elif me=="주먹": print("승리")
        elif me=="보": print("패배")
        else: print("Invalid input.")
    if comp=="주먹":
        if me=="가위": print("패배")
        elif me=="주먹": print("비김")
        elif me=="보": print("승리")
        else: print("Invalid input.")
    if comp=="보":
        if me=="가위": print("승리")
        elif me=="주먹": print("패배")
        elif me=="보": print("비김")
        else: print("Invalid input.")
    if me in ["가위","주먹","보"]:
        print("컴퓨터: {0}".format(comp))
