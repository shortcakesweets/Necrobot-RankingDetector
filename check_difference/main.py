
import pandas as pd

new_data_lb = pd.read_csv("https://warachia2.github.io/NecroRankings/data/main5000.csv")
new_data_lbplace = pd.read_csv("https://warachia2.github.io/NecroRankings/data/all5000place.csv")
new_wrs = pd.read_csv("https://warachia2.github.io/NecroRankings/data/mainwrs.csv", header=None, index_col=0, squeeze=True).to_dict()

old_data_lb = pd.read_csv("all5000.csv")
old_data_lbplace = pd.read_csv("all5000place.csv")
old_wrs = pd.read_csv("mainwrs.csv", header=None, index_col=0, squeeze=True).to_dict()

#print(new_wrs)

def ratio_to_time(wr, ratio):
    if ratio == 20:
        return "---"
    msec = wr * ratio
    t = divmod(msec, 60000)
    t2 = divmod(t[1], 1000)
    t3 = divmod(t2[1], 10)
    middle = str(int(t2[0]))
    last = str(int(t3[0]))
    if int(t2[0]) < 10:
        middle = "0" + middle
    if int(t3[0]) < 10:
        last = "0" + last

    return str(int(t[0])) + ":" + middle + ":" + last

#print(new_data_lb)

index = 0
changed_data = {}
# Usage
# changed_data["Shortcake"] = { "Diamond Speed" : [ new_pb, old_pb, new_lbplace, old_lbplace ] , ... }

def append_to_changed_data(name, category, data):
    if name in changed_data:
        changed_data[name][category] = data
    else:
        new_data = {}
        new_data[category] = data
        changed_data[name] = new_data


for index in range(5000):
    new_player_data = new_data_lb.iloc[index]
    old_player_data = old_data_lb.iloc[index]

    #print(new_player_data)
    #print(old_player_data)

    player_name = new_player_data["Name"]
    print(index, ":", player_name)

    count = 0
    for category in new_wrs.keys():
        new_wr = new_wrs[category] * 10
        old_wr = old_wrs[category] * 10

        if category.endswith("Speed"):
            new_time = ratio_to_time(new_wr, new_player_data[category])
            old_time = ratio_to_time(old_wr, old_player_data[category])

            if new_time != old_time:
                new_lbplace = new_data_lbplace.iloc[index][category]
                old_lbplace = old_data_lbplace.iloc[index][category]
                print(category, new_time, old_time, new_lbplace, old_lbplace)

                new_changed_data = [new_time, old_time, new_lbplace, old_lbplace]
                append_to_changed_data(player_name, category, new_changed_data)
                count += 1

        elif category.endswith("Score"):
            new_score = new_player_data[category]
            old_score = old_player_data[category]

            if new_score != old_score:
                new_lbplace = new_data_lbplace.iloc[index][category]
                old_lbplace = old_data_lbplace.iloc[index][category]
                print(category, new_score, old_score, new_lbplace, old_lbplace)

                new_changed_data = [new_score, old_score, new_lbplace, old_lbplace]
                append_to_changed_data(player_name, category, new_changed_data)
                count += 1

        else: # Deathless
            print(category)

    if count != 0: # Some pbs are changed
        print(" Total changed PBs : ", count)
    else:
        print(" No change ")

print("\n")

#print(changed_data)