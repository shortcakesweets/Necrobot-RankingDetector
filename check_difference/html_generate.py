import main as DATA
from datetime import datetime

old_index_file = open("index.html", 'r')

pb_baseFormat = "<a href=\"https://warachia2.github.io/NecroRankings/pbs/"
category_baseFormat = "<a href=\"https://warachia2.github.io/NecroRankings/lbs/"

print( datetime.today().strftime('%Y-%m-%d') )
print(DATA.changed_data)
#print(DATA.new_wrs.keys())
print("\n\n\n")

run_program_trigger : bool = True
if len(DATA.changed_data) == 0:
    print(" No data has changed. No change of index.html ")
    run_program_trigger = False


lines = []

def category_refined(category):
    if category == "Aria Speed":
        return "Ariaspeedlbs.html"
    elif category == "Bard Speed":
        return "Bardspeedlbs.html"
    elif category == "Bolt Speed":
        return "Boltspeedlbs.html"
    elif category == "Cad Speed":
        return "Cadencespeedlbs.html"
    elif category == "Dia Speed":
        return "Diamondspeedlbs.html"
    elif category == "Dor Speed":
        return "Dorianspeedlbs.html"
    elif category == "Eli Speed":
        return "Elispeedlbs.html"
    elif category == "Mary Speed":
        return "Maryspeedlbs.html"
    elif category == "Mel Speed":
        return "Melodyspeedlbs.html"
    elif category == "Monk Speed":
        return "Monkspeedlbs.html"
    elif category == "Noc Speed":
        return "Nocturnaspeedlbs.html"
    elif category == "Tempo Speed":
        return "Tempospeedlbs.html"
    elif category == "Coda Speed":
        return "Codaspeedlbs.html"
    elif category == "Story Speed":
        return "Storyspeedlbs.html"
    elif category == "9char Speed":
        return "9charspeedlbs.html"
    elif category == "13char Speed":
        return "13charspeedlbs.html"

    elif category == "Aria Score":
        return "Ariascorelbs.html"
    elif category == "Bard Score":
        return "Bardscorelbs.html"
    elif category == "Bolt Score":
        return "Boltscorelbs.html"
    elif category == "Cad Score":
        return "Cadencescorelbs.html"
    elif category == "Dia Score":
        return "Diamondscorelbs.html"
    elif category == "Dor Score":
        return "Dorianscorelbs.html"
    elif category == "Eli Score":
        return "Eliscorelbs.html"
    elif category == "Mary Score":
        return "Maryscorelbs.html"
    elif category == "Mel Score":
        return "Melodyscorelbs.html"
    elif category == "Monk Score":
        return "Monkscorelbs.html"
    elif category == "Noc Score":
        return "Nocturnascorelbs.html"
    elif category == "Tempo Score":
        return "Temposcorelbs.html"
    elif category == "Coda Score":
        return "Codascorelbs.html"
    elif category == "Story Score":
        return "Storyscorelbs.html"
    elif category == "9char Score":
        return "9charscorelbs.html"
    elif category == "13char Score":
        return "13charscorelbs.html"
    else :
        print("??")
        return ""

def full_name(category):
    full_name_category = ""
    if category.startswith("Cad"):
        full_name_category = "Cadence"
    elif category.startswith("Dia"):
        full_name_category = "Diamond"
    elif category.startswith("Dor"):
        full_name_category = "Dorian"
    elif category.startswith("Mel"):
        full_name_category = "Melody"
    elif category.startswith("Noc"):
        full_name_category = "Nocturna"
    else:
        return category

    if category.endswith("Speed"):
        full_name_category += " speed"
    elif category.endswith("Score"):
        full_name_category += " score"

    return full_name_category

def st_nd_rd_th(num):
    if num == 1:
        return "st"
    elif num == 2:
        return "nd"
    elif num == 3:
        return "rd"
    else:
        return "th"

def generate_paragraph(player_name, category, data):
    new_lines = []

    new_lines.append("<p>\n")

    one_line = pb_baseFormat + player_name + ".html\"> " + player_name + "</a> :\n"
    new_lines.append(one_line)

    one_line = category_baseFormat + category_refined(category) + "\"> " + full_name(category) + "</a> "
    one_line += data[1] + " (" + str(data[3]) + st_nd_rd_th(data[3]) + ")"
    one_line += " > "
    one_line += data[0] + " (" + str(data[2]) + st_nd_rd_th(data[2]) + ")\n"
    new_lines.append(one_line)

    new_lines.append("</p>\n")
    return new_lines

insert_point : bool = False
while run_program_trigger:
    line = old_index_file.readline()
    if "<h1>" in line:
        insert_point = True

    lines.append(line)

    if insert_point:
        new_lines = []
        today = datetime.today()
        lines.append("<h3> " + datetime.today().strftime('%Y-%m-%d') + "</h3>\n")

        #print( DATA.changed_data )
        for player_name in DATA.changed_data.keys():
            bulk_data = DATA.changed_data[player_name]
            for category in bulk_data.keys():
                data = bulk_data[category]

                new_lines = generate_paragraph(player_name, category, data)

                for more_line in new_lines:
                    lines.append(more_line)

    insert_point = False
    if not line: break

old_index_file.close()

if run_program_trigger:
    new_index_file = open("index.html", 'w')
    for line in lines:
        new_index_file.write(line)

    new_index_file.close()