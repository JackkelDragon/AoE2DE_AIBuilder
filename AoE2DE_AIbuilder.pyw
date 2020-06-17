try:
    from Tkinter import *
    from ttk import *
    import tkFileDialog
except ImportError:
    import tkinter as Tkinter
    from tkinter import *
    import tkinter.ttk as ttk
    from tkinter.ttk import *
    import tkinter.filedialog as tkFileDialog
import json

## Function definitions

## Create the main window

window = Tk()
window.title("AoE2 DE Campaign AI Builder v1 by Jackkel Dragon")
window.geometry('800x600')

## scrolling

canvas = Canvas(window)
canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

frame = Frame(canvas, width=800, height=2000)
canvas.create_window(0, 0, window=frame, anchor="nw")
canvas.configure(scrollregion=(0,0,800,2000))

scrolly = Scrollbar(window, command=canvas.yview)
scrolly.place(relx=1, rely=0, relheight=1, anchor='ne')
canvas.configure(yscrollcommand=scrolly.set)

## Top label

intro = Label(frame, text="This is a program for creating basic AI for custom campaigns in Age of Empires 2: Definitive Edition.\nIt is based on the Forgotten Empires AI Builder written by Jan1302.\n\nFE's web app can be found here: http://www.forgottenempires.net/aibuilder/", justify = LEFT)
intro.place(x=10,y=10)

## AI Name (for filenames)

ainame_help = Label(frame, text="AI Name:\n\nThis will be the name of the AI files.", justify = LEFT, wraplength=200)
ainame_help.place(x=10,y=100)

ainame = Entry(frame,width=40)
ainame.place(x=250, y=110)

## AI Behavior Title

aibehavior = Label(frame, text="AI Behavior\nWhen the AI activates. When not active, the AI does not do anything besides move kings/trading units/fishing ships.", width=650, anchor="center", justify=CENTER)
aibehavior.place(x=10,y=160,width=650)

## AI Behavior Types

radsel = IntVar()
radsel.set(3)
rad1 = Radiobutton(frame,text='Always Immobile', value=1, variable=radsel)
rad2 = Radiobutton(frame,text='Wait for Signal', value=2, variable=radsel)
rad3 = Radiobutton(frame,text='Always Active', value=3, variable=radsel)
#rad1.place(x=10, y=200)
rad2.place(x=10, y=200)
rad3.place(x=160, y=200)

## AI Signal for "Wait for Signal"

aisignal_help = Label(frame, text="Activation Signal:\n\nThis is the numerical signal that must be set from a trigger to activate the AI if \"Until Signal\" is selected above.", justify = LEFT, wraplength=200)
aisignal_help.place(x=10,y=240)

aisignal = Spinbox(frame, from_=0, to=255, width=3)
aisignal.place(x=250,y=260)

## Strategic Numbers Title

snlabel = Label(frame, text="Strategic Numbers", width=600, anchor="center")
snlabel.place(x=10,y=330,width=600)

sn1 = Label(frame, text="Task Ungrouped Soldiers\n\nThe AI will try to spread out its forces so no unit is adjacent to any other unit or building. (This can create a blanket of units over the map if the army is too large.)", justify = LEFT, wraplength=200)
sn1.place(x=10,y=360)

sn2 = Label(frame, text="# Military Explorers\n\nThe number of military units used to scout. (If the AI can create scout cavalry, it will train them to be these scouts.)", justify = LEFT, wraplength=200)
sn2.place(x=250,y=360)

sn3 = Label(frame, text="Builder/Gatherer Percentages\n\nThe percentage of builder villagers versus gatherer villagers.", justify = LEFT, wraplength=200)
sn3.place(x=490,y=360)

sn4 = Label(frame, text="Resource Gatherer Percentages\n( Food | Wood | Gold | Stone )", width=600, anchor="center", justify=CENTER)
sn4.place(x=10,y=480,width=600)

sn1cVal = BooleanVar(False)
sn1c = Checkbutton(frame, variable=sn1cVal)
sn1c.place(x=200,y=360,width=20)

sn2c = Spinbox(frame, from_=0, to=100, width=3)
sn2c.place(x=420,y=360)

sn3c = Spinbox(frame, from_=0, to=100, width=3)
sn3c.place(x=660,y=360)
sn4c = Spinbox(frame, from_=0, to=100, width=3)
sn4c.place(x=700,y=360)

sn5c = Spinbox(frame, from_=0, to=100, width=3)
sn5c.place(x=235,y=520)
sn6c = Spinbox(frame, from_=0, to=100, width=3)
sn6c.place(x=275,y=520)
sn7c = Spinbox(frame, from_=0, to=100, width=3)
sn7c.place(x=315,y=520)
sn8c = Spinbox(frame, from_=0, to=100, width=3)
sn8c.place(x=355,y=520)

## Economy Title

eclabel = Label(frame, text="Economy", width=600, anchor="center")
eclabel.place(x=10,y=550,width=600)

ec1 = Label(frame, text="Total Villagers", justify = LEFT)
ec1.place(x=10,y=580)
ec2 = Label(frame, text="Total Fishing Ships", justify = LEFT)
ec2.place(x=160,y=580)
ec3 = Label(frame, text="Total Trade Carts", justify = LEFT)
ec3.place(x=310,y=580)
ec4 = Label(frame, text="Total Trade Cogs", justify = LEFT)
ec4.place(x=460,y=580)

ec1c = Spinbox(frame, from_=0, to=100, width=3)
ec1c.place(x=120,y=580)
ec2c = Spinbox(frame, from_=0, to=100, width=3)
ec2c.place(x=270,y=580)
ec3c = Spinbox(frame, from_=0, to=100, width=3)
ec3c.place(x=420,y=580)
ec4c = Spinbox(frame, from_=0, to=100, width=3)
ec4c.place(x=570,y=580)

## Military Title

millabel = Label(frame, text="Military", width=600, anchor="center")
millabel.place(x=10,y=620,width=600)

mil1 = Label(frame, text="Unit 1 to Train", justify = LEFT)
mil1.place(x=10,y=650)
mil2 = Label(frame, text="Unit 2 to Train", justify = LEFT)
mil2.place(x=10,y=680)
mil3 = Label(frame, text="Unit 3 to Train", justify = LEFT)
mil3.place(x=10,y=710)
mil4 = Label(frame, text="Unit 4 to Train", justify = LEFT)
mil4.place(x=10,y=740)
mil5 = Label(frame, text="Unit 5 to Train", justify = LEFT)
mil5.place(x=10,y=770)
mil6 = Label(frame, text="Unit 6 to Train", justify = LEFT)
mil6.place(x=10,y=800)
mil7 = Label(frame, text="Unit 7 to Train", justify = LEFT)
mil7.place(x=10,y=830)

mil8 = Label(frame, text="Siege Unit 1 to Train", justify = LEFT)
mil8.place(x=350,y=650)
mil9 = Label(frame, text="Siege Unit 2 to Train", justify = LEFT)
mil9.place(x=350,y=680)
mil10 = Label(frame, text="Siege Unit 3 to Train", justify = LEFT)
mil10.place(x=350,y=710)
mil11 = Label(frame, text="Naval Unit 1 to Train", justify = LEFT)
mil11.place(x=350,y=740)
mil12 = Label(frame, text="Naval Unit 2 to Train", justify = LEFT)
mil12.place(x=350,y=770)
mil13 = Label(frame, text="Naval Unit 3 to Train", justify = LEFT)
mil13.place(x=350,y=800)

milTypesVal = []

for n in range(7):
    milTypesVal.append(StringVar())
    milTypesVal[n].set("Swordsmen")
for n in range(3):
    milTypesVal.append(StringVar())
    milTypesVal[n+7].set("Onagers")
for n in range(3):
    milTypesVal.append(StringVar())
    milTypesVal[n+10].set("Galleys")

milTypes = []

class UnitCombobox(Combobox):
	def __init__(self, master=None, **kw):
		Combobox.__init__(self, master, values=["Swordsmen","Spearmen","Scout Cavalry","Knights","Camels","Archers","Skirmishers","Cavalry Archers","Hand Cannoneers","Unique Units","Monks"], state="readonly", **kw)

for n in range(7):
    milTypes.append(UnitCombobox(frame, textvariable=milTypesVal[n]))
    milTypes[n].place(x=120,y=650+(n*30))

class SiegeCombobox(Combobox):
	def __init__(self, master=None, **kw):
		Combobox.__init__(self, master, values=["Onagers","Rams","Scorpions","Trebuchet","Cannons"], state="readonly", **kw)

for n in range(3):
    milTypes.append(SiegeCombobox(frame, textvariable=milTypesVal[n+7]))
    milTypes[n+7].place(x=490,y=650+(n*30))

class NavalCombobox(Combobox):
	def __init__(self, master=None, **kw):
		Combobox.__init__(self, master, values=["Galleys","Fire Ships","Cannon Galleons","Demolition Ships","Transport Ships"], state="readonly", **kw)

for n in range(3):
    milTypes.append(NavalCombobox(frame, textvariable=milTypesVal[n+10]))
    milTypes[n+10].place(x=490,y=740+(n*30))

milNums = []

for n in range(7):
    milNums.append(Spinbox(frame, from_=0, to=100, width=3))
    milNums[n].place(x=280,y=650+(n*30))

for n in range(6):
    milNums.append(Spinbox(frame, from_=0, to=100, width=3))
    milNums[n+7].place(x=650,y=650+(n*30))

## Building Title

bllabel = Label(frame, text="Buildings", width=600, anchor="center")
bllabel.place(x=10,y=870,width=600)

bl1 = Label(frame, text="AI Builds Houses?", justify = LEFT)
bl1.place(x=10,y=900)
bl1b = Label(frame, text="Amount of each building to build up to/maintain:", width=600, anchor="center")
bl1b.place(x=10,y=930,width=600)
bl2 = Label(frame, text="Town Centers", justify = LEFT)
bl2.place(x=10,y=960)
bl3 = Label(frame, text="Farms", justify = LEFT)
bl3.place(x=10,y=980)
bl4 = Label(frame, text="Lumber Camps", justify = LEFT)
bl4.place(x=10,y=1000)
bl5 = Label(frame, text="Mills (can become bugged if not 0 or 1)", justify = LEFT)
bl5.place(x=10,y=1020)
bl6 = Label(frame, text="Mining Camps for Gold", justify = LEFT)
bl6.place(x=10,y=1040)
bl7 = Label(frame, text="Mining Camps for Stone", justify = LEFT)
bl7.place(x=10,y=1060)
bl8 = Label(frame, text="Barracks", justify = LEFT)
bl8.place(x=10,y=1080)
bl9 = Label(frame, text="Archery Ranges", justify = LEFT)
bl9.place(x=10,y=1100)
bl10 = Label(frame, text="Stables", justify = LEFT)
bl10.place(x=10,y=1120)
bl11 = Label(frame, text="Siege Workshops", justify = LEFT)
bl11.place(x=350,y=960)
bl12 = Label(frame, text="Blacksmiths", justify = LEFT)
bl12.place(x=350,y=980)
bl13 = Label(frame, text="Markets", justify = LEFT)
bl13.place(x=350,y=1000)
bl14 = Label(frame, text="Universities", justify = LEFT)
bl14.place(x=350,y=1020)
bl15 = Label(frame, text="Monasteries", justify = LEFT)
bl15.place(x=350,y=1040)
bl16 = Label(frame, text="Docks", justify = LEFT)
bl16.place(x=350,y=1060)
bl17 = Label(frame, text="Castles", justify = LEFT)
bl17.place(x=350,y=1080)
bl18 = Label(frame, text="Towers", justify = LEFT)
bl18.place(x=350,y=1100)
bl19 = Label(frame, text="Bombard Towers", justify = LEFT)
bl19.place(x=350,y=1120)

bl1cVal = BooleanVar(False)
bl1c = Checkbutton(frame, variable=bl1cVal)
bl1c.place(x=200,y=900,width=20)

blNums = []

for n in range(9):
    blNums.append(Spinbox(frame, from_=0, to=100, width=3))
    blNums[n].place(x=300,y=960+(n*20))

for n in range(9):
    blNums.append(Spinbox(frame, from_=0, to=100, width=3))
    blNums[n+9].place(x=600,y=960+(n*20))

## Attacks Title

atklabel = Label(frame, text="Attacks", width=600, anchor="center")
atklabel.place(x=10,y=1180,width=600)

atk1 = Label(frame, text="Will the AI target walls?", justify = LEFT)
atk1.place(x=10,y=1220)
atk2 = Label(frame, text="Seconds from becoming active before attacking:", justify = LEFT)
atk2.place(x=10,y=1250)
atk3 = Label(frame, text="Seconds between attack waves:", justify = LEFT)
atk3.place(x=10,y=1280)
atk4 = Label(frame, text="Amount of land-based attack groups:", justify = LEFT)
atk4.place(x=10,y=1310)
atk5 = Label(frame, text="Amount of units in land-based attack groups:", justify = LEFT)
atk5.place(x=10,y=1340)
atk6 = Label(frame, text="Amount of water-based attack groups:", justify = LEFT)
atk6.place(x=10,y=1370)
atk7 = Label(frame, text="Amount of units in water-based attack groups:", justify = LEFT)
atk7.place(x=10,y=1400)

atk1cVal = BooleanVar(False)
atk1c = Checkbutton(frame, variable=atk1cVal)
atk1c.place(x=200,y=1220,width=20)

atkNums = []

for n in range(2):
    atkNums.append(Spinbox(frame, from_=0, to=7200, width=8))
    atkNums[n].place(x=300,y=1250+(n*30))

for n in range(4):
    atkNums.append(Spinbox(frame, from_=0, to=200, width=4))
    atkNums[n+2].place(x=300,y=1310+(n*30))

## Upgrades Title

uplabel = Label(frame, text="Upgrades", width=600, anchor="center")
uplabel.place(x=10,y=1450,width=600)

up1 = Label(frame, text="Percentages of collected resources to hold on to for upgrades", justify = LEFT)
up1.place(x=10,y=1475)

up1 = Label(frame, text="Food Escrow", justify = LEFT)
up1.place(x=10,y=1500)
up1 = Label(frame, text="Wood Escrow", justify = LEFT)
up1.place(x=10,y=1520)
up1 = Label(frame, text="Gold Escrow", justify = LEFT)
up1.place(x=10,y=1540)
up1 = Label(frame, text="Stone Escrow", justify = LEFT)
up1.place(x=10,y=1560)

up1 = Label(frame, text="Types of Upgrades to Research", justify = LEFT)
up1.place(x=10,y=1590)

up1 = Label(frame, text="Military", justify = LEFT)
up1.place(x=10,y=1620)
up1 = Label(frame, text="Blacksmith", justify = LEFT)
up1.place(x=10,y=1640)
up1 = Label(frame, text="Economic", justify = LEFT)
up1.place(x=10,y=1660)
up1 = Label(frame, text="University", justify = LEFT)
up1.place(x=10,y=1680)
up1 = Label(frame, text="Monastery", justify = LEFT)
up1.place(x=10,y=1700)
up1 = Label(frame, text="Dock", justify = LEFT)
up1.place(x=10,y=1720)

upNums = []

for n in range(4):
    upNums.append(Spinbox(frame, from_=0, to=100, width=4))
    upNums[n].place(x=200,y=1500+(n*20))

##upNums[0].delete(0) ## debug stuff here
##upNums[0].insert(0,1) ##

upChecks = []
upChecksVar = []

for n in range(6):
    upChecksVar.append(BooleanVar(False))
    upChecks.append(Checkbutton(frame, variable=upChecksVar[n]))
    upChecks[n].place(x=200,y=1620+(n*20),width=20)

## Misc Title

misclabel = Label(frame, text="Miscellanous", width=600, anchor="center")
misclabel.place(x=10,y=1780,width=600)

misc1 = Label(frame, text="Use Market", justify = LEFT)
misc1.place(x=10,y=1820)
misc1 = Label(frame, text="Default Resign Behavior", justify = LEFT)
misc1.place(x=10,y=1840)
misc1 = Label(frame, text="Advance Ages?", justify = LEFT)
misc1.place(x=10,y=1860)
misc1 = Label(frame, text="Final Age (for above)", justify = LEFT)
misc1.place(x=10,y=1880)

miscChecks = []
miscChecksVar = []

for n in range(3):
    miscChecksVar.append(BooleanVar(False))
    miscChecks.append(Checkbutton(frame, variable=miscChecksVar[n]))
    miscChecks[n].place(x=200,y=1820+(n*20),width=20)

finAgeVal = StringVar()
finAgeVal.set("Dark Age")

finAge = Combobox(frame, values=["Dark Age","Feudal Age","Castle Age","Imperial Age"], state="readonly", textvariable=finAgeVal)
finAge.place(x=200, y=1880)

## Output Title

def collect_data():
    data = {}

    ## filename
    data["AIName"] = ainame.get()

    ## activation type
    data["AIActivation"] = radsel.get()

    ## activation signal
    data["AISignalID"] = aisignal.get()

    ## task ungrouped
    data["TaskUngrouped"] = sn1cVal.get()

    ## num military explorers
    data["MilitaryExplorerCount"] = sn2c.get()

    ## builder/gatherer percentages
    data["BuilderPercent"] = sn3c.get()
    data["GathererPercent"] = sn4c.get()

    ## resource gathering percentages
    data["FoodGatherPercent"] = sn5c.get()
    data["WoodGatherPercent"] = sn6c.get()
    data["GoldGatherPercent"] = sn7c.get()
    data["StoneGatherPercent"] = sn8c.get()

    ## total villagers/fishing ships/trade carts/trade cogs
    data["VillagerCount"] = ec1c.get()
    data["FishShipCount"] = ec2c.get()
    data["TradeCartCount"] = ec3c.get()
    data["TradeCogCount"] = ec4c.get()

    ## military unit types and numbers
    for n in range(13):
        data["UnitType"+str(n+1)] = milTypes[n].get()
        data["UnitCount"+str(n+1)] = milNums[n].get()

    ## build houses?
    data["BuildHouses"] = bl1cVal.get()

    ## building amounts
    for n in range(18):
        data["BuildingCount"+str(n+1)] = blNums[n].get()

    ## target walls?
    data["TargetWalls"] = atk1cVal.get()

    ## attack wave timers
    for n in range(2):
        data["AttackTimerValues"+str(n+1)] = atkNums[n].get()

    ## attack group numbers
    for n in range(4):
        data["AttackGroupValues"+str(n+1)] = atkNums[n+2].get()

    ## upgrade escrows
    for n in range(4):
        data["UpgradeEscrow"+str(n+1)] = upNums[n].get()

    ## upgrade types
    for n in range(6):
        data["UpgradeType"+str(n+1)] = upChecksVar[n].get()

    ## misc data
    data["UseMarket"] = miscChecksVar[0].get()
    data["DefaultResign"] = miscChecksVar[1].get()
    data["AdvanceAge"] = miscChecksVar[2].get()
    data["FinalAge"] = finAgeVal.get()

    #print(data) ## for debugging
        
    return data
        
def save_json():
    data = collect_data()
    
    window.file = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("JSON","*.json"),("All Files","*.*")), defaultextension=".json")
    
    if window.file != "":
        f = open(window.file,'w')
        f.write(json.dumps(data))
        f.close()
        
def load_json():
    window.file = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("JSON","*.json"),("All Files","*.*")))
    
    f = open(window.file)
    rawtext = f.read()
    data = json.loads(rawtext)
    
    #print(data) ## debug
    
    ## Restore the data
    
    ## filename
    ainame.delete(0,END)
    ainame.insert(0,data["AIName"])
        
    ## activation type
    radsel.set(int(data["AIActivation"]))

    ## activation signal
    aisignal.delete(0,END)
    aisignal.insert(0,data["AISignalID"])
    
    ## task ungrouped
    sn1cVal.set(data["TaskUngrouped"])
    
    ## num military explorers
    sn2c.delete(0,END)
    sn2c.insert(0,data["MilitaryExplorerCount"])
    
    ## builder/gatherer percentages
    sn3c.delete(0,END)
    sn3c.insert(0,data["BuilderPercent"])
    sn4c.delete(0,END)
    sn4c.insert(0,data["GathererPercent"])
    
    ## resource gathering percentages
    sn5c.delete(0,END)
    sn5c.insert(0,data["FoodGatherPercent"])
    sn6c.delete(0,END)
    sn6c.insert(0,data["WoodGatherPercent"])
    sn7c.delete(0,END)
    sn7c.insert(0,data["GoldGatherPercent"])
    sn8c.delete(0,END)
    sn8c.insert(0,data["StoneGatherPercent"])
    
    ## total villagers/fishing ships/trade carts/trade cogs
    ec1c.delete(0,END)
    ec1c.insert(0,data["VillagerCount"])
    ec2c.delete(0,END)
    ec2c.insert(0,data["FishShipCount"])
    ec3c.delete(0,END)
    ec3c.insert(0,data["TradeCartCount"])
    ec4c.delete(0,END)
    ec4c.insert(0,data["TradeCogCount"])
    
    ## military unit types and numbers
    for n in range(13):
        milTypes[n].set(data["UnitType"+str(n+1)])
        milNums[n].delete(0,END)
        milNums[n].insert(0,data["UnitCount"+str(n+1)])
    
    ## build houses?
    bl1cVal.set(data["BuildHouses"])
    
    ## building amounts
    for n in range(18):
        blNums[n].delete(0,END)
        blNums[n].insert(0,data["BuildingCount"+str(n+1)])
    
    ## target walls?
    atk1cVal.set(data["TargetWalls"])
    
    ## attack wave timers
    for n in range(2):
        atkNums[n].delete(0,END)
        atkNums[n].insert(0,data["AttackTimerValues"+str(n+1)])
    
    ## attack group numbers
    for n in range(4):
        atkNums[n+2].delete(0,END)
        atkNums[n+2].insert(0,data["AttackGroupValues"+str(n+1)])
    
    ## upgrade escrows
    for n in range(4):
        upNums[n].delete(0,END)
        upNums[n].insert(0,data["UpgradeEscrow"+str(n+1)])
        
    ## upgrade types
    for n in range(6):
        upChecksVar[n].set(data["UpgradeType"+str(n+1)])
    
    ## misc data
    miscChecksVar[0].set(data["UseMarket"])
    miscChecksVar[1].set(data["DefaultResign"])
    miscChecksVar[2].set(data["AdvanceAge"])
    finAgeVal.set(data["FinalAge"])
    
def boolToYesNo(bool):

    if (bool):
        return "yes"
    else:
        return "no"
        
def create_final_per_file():
    finaltext = ""
    data = collect_data()
    
    finaltext += ";------\n;"+data["AIName"]+"\n;------\n;Generated by AoE2DE AI Builder\n\n"
    
    finaltext += ";***Set Constants***\n;---GENERAL---\n(defconst yes 1)\n(defconst no 0)\n(defconst aisignal " + str(data["AISignalID"]) + ")\n\n"
    
    finaltext += ";---GOALS---\n"
    
    for n in range(7):
        if (data["UnitCount"+str(n+1)] != 0):
            dataname = data["UnitType"+str(n+1)]
            finalname = ""
            
            if (dataname == "Swordsmen"):
                finalname = "militiaman-line"
            elif (dataname == "Spearmen"):
                finalname = "spearman-line"
            elif (dataname == "Scout Cavalry"):
                finalname = "scout-cavalry-line"
            elif (dataname == "Knights"):
                finalname = "knight-line"
            elif (dataname == "Camels"):
                finalname = "camel-line"
            elif (dataname == "Archers"):
                finalname = "archer-line"
            elif (dataname == "Skirmishers"):
                finalname = "skirmisher-line"
            elif (dataname == "Cavalry Archers"):
                finalname = "cavalry-archer-line"
            elif (dataname == "Hand Cannoneers"):
                finalname = "hand-cannoneer"
            elif (dataname == "Unique Units"):
                finalname = "my-unique-unit-line"
            elif (dataname == "Monks"):
                finalname = "monk"
            
            finaltext += "(defconst unit"+str(n+1)+" "+finalname+")\n"
            
    for n in range(3):
        if (data["UnitCount"+str(n+8)] != 0):
            dataname = data["UnitType"+str(n+8)]
            finalname = ""
            
            if (dataname == "Onagers"):
                finalname = "mangonel-line"
            elif (dataname == "Rams"):
                finalname = "battering-ram-line"
            elif (dataname == "Scorpions"):
                finalname = "scorpion-line"
            elif (dataname == "Trebuchet"):
                finalname = "trebuchet"
            elif (dataname == "Cannons"):
                finalname = "bombard-cannon"
            
            finaltext += "(defconst siege"+str(n+1)+" "+finalname+")\n"
            
    for n in range(3):
        if (data["UnitCount"+str(n+11)] != 0):
            dataname = data["UnitType"+str(n+11)]
            finalname = ""
            
            if (dataname == "Galleys"):
                finalname = "galley-line"
            elif (dataname == "Fire Ships"):
                finalname = "fire-ship-line"
            elif (dataname == "Cannon Galleons"):
                finalname = "cannon-galleon-line"
            elif (dataname == "Demolition Ships"):
                finalname = "demolition-ship-line"
            elif (dataname == "Transport Ships"):
                finalname = "transport-ship"
            
            finaltext += "(defconst naval"+str(n+1)+" "+finalname+")\n"
    
    finaltext += "(defconst blacksmith-techs 5)\n(defconst military-techs 6)\n(defconst economic-techs 7)\n(defconst university-techs 8)\n(defconst monastery-techs 9)\n(defconst dock-techs 10)\n(defconst build-houses 11)\n(defconst end-age 12)\n(defconst use-market 14)\n(defconst default-resign 15)\n(defconst allow-advancing 16)\n(defconst allow-signal 17)\n(defconst active-at-start 18)\n(defconst activate 19)\n(defconst combi 20)\n\n"

    finaltext += ";---ATTACKS---\n(defconst attack-timer 2)\n(defconst interval-timer 3)\n(defconst standby 0)\n(defconst offence 1)\n(defconst reset-attack 2)\n(defconst attack-goal 3)\n\n"

    finaltext += ";---UPGRADES---\n"
    
    finaltext += "(defconst food-escrow "+data["UpgradeEscrow1"]+")\n(defconst wood-escrow "+data["UpgradeEscrow2"]+")\n(defconst gold-escrow "+data["UpgradeEscrow3"]+")\n(defconst stone-escrow "+data["UpgradeEscrow4"]+")\n\n"

    finaltext += ";---OTHERS---\n(defconst percentage-builders "+data["BuilderPercent"]+")\n(defconst percentage-gatherers "+data["GathererPercent"]+")\n(defconst percentage-explorers "+data["MilitaryExplorerCount"]+")\n(defconst food-gatherers "+data["FoodGatherPercent"]+")\n(defconst wood-gatherers "+data["WoodGatherPercent"]+")\n(defconst gold-gatherers "+data["GoldGatherPercent"]+")\n(defconst stone-gatherers "+data["StoneGatherPercent"]+")\n(defconst end-dark 0)\n(defconst end-feudal 1)\n(defconst end-castle 2)\n(defconst end-imperial 3)\n"
    
    finaltext += "(defconst task-soldiers "+boolToYesNo(data["TaskUngrouped"])+")\n\n"

    finaltext += ";***Set Goals***\n;---Upgrades---\n\n(defrule\n	(true)\n=>\n	(set-goal economic-techs "+boolToYesNo(data["UpgradeType3"])+")\n	(set-goal military-techs "+boolToYesNo(data["UpgradeType1"])+")\n	(set-goal blacksmith-techs "+boolToYesNo(data["UpgradeType2"])+")\n	(set-goal university-techs "+boolToYesNo(data["UpgradeType4"])+")\n	(set-goal monastery-techs "+boolToYesNo(data["UpgradeType5"])+")\n	(set-goal dock-techs "+boolToYesNo(data["UpgradeType6"])+")\n	(disable-self)\n)\n\n"

    ## need to set end age properly
    rawfinalage = data["FinalAge"]
    truefinalage = "end-dark"
    
    if (rawfinalage == "Feudal Age"):
        truefinalage = "end-feudal"
    elif (rawfinalage == "Castle Age"):
        truefinalage = "end-castle"
    elif (rawfinalage == "Imperial Age"):
        truefinalage = "end-imperial"

    finaltext += ";---General---\n\n(defrule\n	(true)\n=>\n	(set-goal allow-advancing "+boolToYesNo(data["AdvanceAge"])+")\n	(set-goal build-houses "+boolToYesNo(data["BuildHouses"])+")\n	(set-goal end-age "+truefinalage+")\n	(set-goal use-market "+boolToYesNo(data["UseMarket"])+")\n	(set-goal default-resign "+boolToYesNo(data["DefaultResign"])+")\n	"
    
    ## signal and active at start
    ##finaltext += "(set-goal allow-signal 0)\n	(set-goal active-at-start 1)\n	(disable-self)\n)\n\n"
    
    if (data["AIActivation"] == 3):
        finaltext += "(set-goal allow-signal 0)\n	(set-goal active-at-start 1)\n	(disable-self)\n)\n\n"
    else:
        finaltext += "(set-goal allow-signal 1)\n	(set-goal active-at-start 0)\n	(disable-self)\n)\n\n"

    finaltext += ";---Activation---\n;when a signal is sent or the AI is allowed to be active at start it will tell the AI to enable the activate goal. This goal will make the AI active. (Combi is for backwards compability)\n\n(defrule\n	(or\n		(and\n		(event-detected trigger aisignal)\n		(goal allow-signal yes)\n		)\n	(goal active-at-start yes)\n	)\n=>\n	(set-goal activate yes)\n	(set-goal combi yes)\n	(disable-self)\n)\n\n"
     
    finaltext += ";***Setup***\n;---Load Externals---\n;load extra files. These files are generic and take care of the resigning of the AI, its upgrades and the active use of the market.\n\n(load \"builder resign\")\n(load \"builder upgrades\")\n(load \"builder market\")\n\n"
    
    finaltext += ";---Immobile Behaviour---\n;default behaviour is set to immobile\n(defrule\n	(goal active-at-start no)\n=>\n	(set-strategic-number sn-maximum-food-drop-distance 0)\n	(set-strategic-number sn-maximum-wood-drop-distance 0)\n	(set-strategic-number sn-maximum-gold-drop-distance 0)\n	(set-strategic-number sn-maximum-hunt-drop-distance 0)\n	(set-strategic-number sn-maximum-stone-drop-distance 0)\n	(set-strategic-number sn-food-gatherer-percentage 0)\n	(set-strategic-number sn-wood-gatherer-percentage 0)\n	(set-strategic-number sn-gold-gatherer-percentage 0)\n	(set-strategic-number sn-stone-gatherer-percentage 0)\n	(set-strategic-number sn-cap-civilian-explorers 0)\n	(set-strategic-number sn-percent-civilian-explorers 0) \n	(disable-self)\n)\n(defrule	\n	(goal active-at-start no)\n=>\n	(set-strategic-number sn-defense-distance 20)\n	(set-strategic-number sn-sentry-distance 20)\n	(set-strategic-number sn-percent-enemy-sighted-response 100)\n	(set-strategic-number sn-number-explore-groups 0)\n	(set-strategic-number sn-percent-attack-soldiers 0)\n	(set-strategic-number sn-task-ungrouped-soldiers 0)\n	(set-strategic-number sn-number-attack-groups 0)\n	(set-strategic-number sn-enemy-sighted-response-distance 10)\n	(set-strategic-number sn-total-number-explorers 0)\n	(set-strategic-number sn-minimum-town-size 0)\n	(set-strategic-number sn-maximum-town-size 0)\n	(disable-self)\n)\n"
    
    finaltext += ";---Active Behaviour---\n;when activated the AI will begin to play\n(defrule\n	(goal activate yes)\n=>\n	(set-strategic-number sn-percent-civilian-builders percentage-builders)\n	(set-strategic-number sn-percent-civilian-gatherers percentage-gatherers)\n	(set-strategic-number sn-percent-civilian-explorers 0)\n	(set-strategic-number sn-number-explore-groups 1)\n 	(set-strategic-number sn-total-number-explorers percentage-explorers)\n	(set-strategic-number sn-food-gatherer-percentage food-gatherers)\n	(set-strategic-number sn-wood-gatherer-percentage wood-gatherers)\n	(set-strategic-number sn-gold-gatherer-percentage gold-gatherers)\n	(set-strategic-number sn-stone-gatherer-percentage stone-gatherers)\n	(disable-self)\n)\n(defrule\n	(goal activate yes)\n=>\n	(set-strategic-number sn-maximum-hunt-drop-distance 30)\n	(set-strategic-number sn-mill-max-distance 30)\n	(set-strategic-number sn-maximum-gold-drop-distance 20)\n	(set-strategic-number sn-maximum-stone-drop-distance 20)\n	(set-strategic-number sn-maximum-food-drop-distance 10) \n	(set-strategic-number sn-maximum-wood-drop-distance 20)\n	(set-strategic-number sn-task-ungrouped-soldiers task-soldiers)\n	(disable-self)\n)\n;"
    
    finaltext += "***AI Behaviour***\n;-----Dodging rules-----\n;ability of the AI to dodge enemy missiles shot at them and maintaining distance when engaging with enemies. The lower the number how better they are at it.\n(defrule\n	(difficulty == easiest)\n=>\n	(set-difficulty-parameter ability-to-maintain-distance 90)\n	(set-difficulty-parameter ability-to-dodge-missiles 90)\n	(disable-self)\n)\n(defrule\n	(difficulty == easy)\n=>\n	(set-difficulty-parameter ability-to-maintain-distance 70)\n	(set-difficulty-parameter ability-to-dodge-missiles 70)\n	(disable-self)\n)\n(defrule\n	(difficulty == moderate)\n=>\n	(set-difficulty-parameter ability-to-maintain-distance 50) \n	(set-difficulty-parameter ability-to-dodge-missiles 50)\n	(disable-self)\n)\n(defrule\n	(difficulty == hard)\n=>\n	(set-difficulty-parameter ability-to-maintain-distance 30) \n	(set-difficulty-parameter ability-to-dodge-missiles 30)\n	(disable-self)\n)\n(defrule\n	(difficulty == hardest)\n=>\n	(set-difficulty-parameter ability-to-maintain-distance 0) \n	(set-difficulty-parameter ability-to-dodge-missiles 0)\n	(disable-self)\n)\n;"
    
    finaltext += "***Production***\n;---Homebase Stats---\n(defrule\n	(goal activate yes)\n=>\n	(set-strategic-number sn-maximum-town-size 15)\n    (set-strategic-number sn-camp-max-distance 20)\n   	(set-strategic-number sn-mill-max-distance 30)\n	(set-strategic-number sn-percent-enemy-sighted-response 50)\n	(set-strategic-number sn-enemy-sighted-response-distance 15)\n	(set-strategic-number sn-blot-exploration-map 0)\n	(set-strategic-number sn-sentry-distance 20)\n	(disable-self)\n)\n"
    
    finaltext += ";---Farming and Civilians---\n(defrule\n	(goal activate yes)\n	(building-type-count-total farm less-than "+data["BuildingCount2"]+")\n	(or\n	(building-type-count-total mill > 0)\n	(building-type-count-total town-center > 0)\n	)\n	(idle-farm-count <= 1)\n	(can-build farm)\n=>\n	(build farm)\n)\n(defrule\n	(goal activate yes)\n	(unit-type-count-total villager < "+data["VillagerCount"]+")\n	(can-train villager)\n=>\n	(train villager)\n) \n(defrule\n	(goal activate yes)\n	(unit-type-count-total trade-cart < "+data["TradeCartCount"]+")\n	(can-train trade-cart)\n=>\n	(train trade-cart)\n) \n(defrule\n	(goal activate yes)\n	(unit-type-count-total trade-cog < "+data["TradeCogCount"]+")\n	(can-train trade-cog)\n=>\n	(train trade-cog)\n) \n(defrule\n	(goal activate yes)\n	(unit-type-count-total fishing-ship < "+data["FishShipCount"]+")\n	(dropsite-min-distance food < 20)\n	(can-train fishing-ship)\n=>\n	(train fishing-ship)\n) \n"
    
    finaltext += ";---Economic Buildings---\n(defrule\n	(goal activate yes)\n	(building-type-count-total town-center < "+data["BuildingCount1"]+")\n	(can-build town-center)\n=>\n	(build town-center)\n) \n(defrule\n	(goal activate yes)\n	(housing-headroom less-than 4)\n	(population-headroom greater-than 0)\n	(can-build house)\n	(goal build-houses 1)\n=>\n	(build house)\n)\n(defrule\n	(goal activate yes)\n	(resource-found wood)\n	(dropsite-min-distance wood > 4)\n	(building-type-count-total lumber-camp < "+data["BuildingCount3"]+")\n	(can-build lumber-camp)\n=>\n	(build lumber-camp)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total mill < "+data["BuildingCount4"]+")\n	(dropsite-min-distance food > 5)\n	(can-build mill)\n=>\n	(build mill)\n) \n(defrule\n	(goal activate yes)\n	(resource-found gold)\n	(building-type-count-total mining-camp < "+data["BuildingCount5"]+")\n	(dropsite-min-distance gold > 5)\n	(can-build mining-camp)\n=>\n	(build mining-camp)\n) \n(defrule\n	(goal activate yes)\n	(resource-found stone)\n	(building-type-count-total mining-camp < "+data["BuildingCount6"]+")\n	(dropsite-min-distance stone > 5)\n	(can-build mining-camp)\n=>\n	(build mining-camp)\n) \n"
    
    finaltext += ";---Military and Research Buildings---\n(defrule\n	(goal activate yes)\n	(building-type-count-total barracks < "+data["BuildingCount7"]+")\n	(can-build barracks)\n=>\n	(build barracks)\n) \n(defrule\n	(goal activate yes)	\n	(building-type-count-total archery-range < "+data["BuildingCount8"]+")\n	(can-build archery-range)\n=>\n	(build archery-range)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total stable < "+data["BuildingCount9"]+")\n	(can-build stable)\n=>\n	(build stable)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total siege-workshop < "+data["BuildingCount10"]+")\n	(can-build siege-workshop)\n=>\n	(build siege-workshop)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total dock < "+data["BuildingCount15"]+")\n	(can-build dock)\n=>\n	(build dock)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total university < "+data["BuildingCount13"]+")\n	(can-build university)\n=>\n	(build university)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total blacksmith < "+data["BuildingCount11"]+")\n	(can-build blacksmith)\n=>\n	(build blacksmith)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total market < "+data["BuildingCount12"]+")\n	(can-build market)\n=>\n	(build market)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total monastery < "+data["BuildingCount14"]+")\n	(can-build monastery)\n=>\n	(build monastery)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total castle < "+data["BuildingCount16"]+")\n	(can-build castle)\n=>\n	(build castle)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total watch-tower-line < "+data["BuildingCount17"]+")\n	(can-build watch-tower-line)\n=>\n	(build watch-tower-line)\n) \n(defrule\n	(goal activate yes)\n	(building-type-count-total bombard-tower < "+data["BuildingCount18"]+")\n	(can-build bombard-tower)\n=>\n	(build bombard-tower)\n) \n"
    
    finaltext += ";***Assault rules***\n;---Assault stats---\n(defrule\n	(goal activate yes)\n=>\n	(set-strategic-number sn-do-not-scale-for-difficulty-level no)\n	(set-strategic-number sn-wall-targeting-mode "+boolToYesNo(data["TargetWalls"])+")\n	(disable-self)\n)\n"
    
    finaltext += ";-----Offence-----\n;activate the first attack\n(defrule\n	(goal activate yes)\n=>\n	(enable-timer attack-timer "+str(data["AttackTimerValues1"])+")\n	(set-goal attack-goal standby)\n	(disable-self)\n)\n;first attack is activated and a new timer is enabled to already activate the next attack later on\n(defrule \n	(timer-triggered attack-timer)\n	(goal attack-goal standby)\n	(military-population >= 10)\n	(defend-soldier-count >= 10)\n	(not (town-under-attack))\n=>\n	(set-strategic-number sn-percent-enemy-sighted-response 60)\n	(set-strategic-number sn-enemy-sighted-response-distance 40) \n	(set-goal attack-goal offence) \n	(disable-timer attack-timer) \n	(enable-timer attack-timer "+str(data["AttackTimerValues2"])+");Interval between attacks\n)\n;the ai stops his attacks and resets everything until the next wave\n(defrule \n	;(goal attack-goal reset-attack) \n	(timer-triggered interval-timer)\n=> \n	(disable-timer interval-timer) \n	(set-goal attack-goal standby)\n) \n;the ai will keep his units at his base when on standby\n(defrule \n	(goal attack-goal standby)\n=> \n	(set-strategic-number sn-group-form-distance 25)\n	(set-strategic-number sn-maximum-attack-group-size 0) \n	(set-strategic-number sn-minimum-attack-group-size 0) \n	(set-strategic-number sn-number-attack-groups 0)\n	(set-strategic-number sn-number-boat-attack-groups 0)\n	(set-strategic-number sn-minimum-boat-attack-group-size 0)\n	(set-strategic-number sn-maximum-boat-attack-group-size 0)\n	(disable-timer interval-timer) \n	(enable-timer interval-timer 10)\n	;(set-goal attack-goal reset-attack)\n)\n;the ai gathers his troops and attacks the enemy with the amount stated below\n(defrule \n	(goal attack-goal offence) "
    
    finaltext += ";Attacking - Groups\n=> \n	(set-strategic-number sn-group-form-distance 30)\n	(set-strategic-number sn-number-attack-groups "+str(data["AttackGroupValues1"])+")\n	(set-strategic-number sn-maximum-attack-group-size "+str(data["AttackGroupValues2"])+") \n	(set-strategic-number sn-minimum-attack-group-size "+str(data["AttackGroupValues2"])+") \n	(set-strategic-number sn-number-boat-attack-groups "+str(data["AttackGroupValues3"])+")\n	(set-strategic-number sn-minimum-boat-attack-group-size "+str(data["AttackGroupValues4"])+")\n	(set-strategic-number sn-maximum-boat-attack-group-size "+str(data["AttackGroupValues4"])+")\n	(set-goal attack-goal reset-attack)\n)\n"
    
    finaltext += ";***Production2***\n;---Military---\n"
    
    for n in range(7):
        if (data["UnitCount"+str(n+1)] != 0):
            finaltext += "(defrule\n	(goal activate yes)\n	(unit-type-count-total unit"+str(n+1)+" < "+str(data["UnitCount"+str(n+1)])+")\n	(can-train unit"+str(n+1)+")\n=>\n	(train unit"+str(n+1)+")\n)\n"
            
    for n in range(3):
        if (data["UnitCount"+str(n+1)] != 0):
            finaltext += "(defrule\n	(goal activate yes)\n	(unit-type-count-total siege"+str(n+1)+" < "+str(data["UnitCount"+str(n+8)])+")\n	(can-train siege"+str(n+1)+")\n=>\n	(train siege"+str(n+1)+")\n)\n"
            
    for n in range(3):
        if (data["UnitCount"+str(n+1)] != 0):
            finaltext += "(defrule\n	(goal activate yes)\n	(unit-type-count-total naval"+str(n+1)+" < "+str(data["UnitCount"+str(n+11)])+")\n	(can-train naval"+str(n+1)+")\n=>\n	(train naval"+str(n+1)+")\n)\n"
    
    finaltext += ";***Market sales***\n(defrule\n	(goal activate yes)\n	(gold-amount >= 1500)\n	(wood-amount <= 200)\n	(commodity-buying-price wood <= 150)\n	(can-buy-commodity wood)\n	(goal use-market 1)\n=>\n	(buy-commodity wood)\n)\n(defrule\n	(goal activate yes)\n	(gold-amount >= 1500)\n	(food-amount <= 200)\n	(commodity-buying-price food <= 150)\n	(can-buy-commodity food)\n	(goal use-market 1)\n=>\n	(buy-commodity food)\n)\n(defrule\n	(goal activate yes)\n	(gold-amount >= 500)\n	(food-amount <= 100)\n	(can-buy-commodity food)\n	(goal use-market 1)\n=>\n	(buy-commodity food)\n)\n(defrule\n	(goal activate yes)\n	(gold-amount >= 2000)\n	(stone-amount <= 500)\n	(commodity-buying-price stone <= 100)\n	(can-buy-commodity stone)\n	(goal use-market 1)\n=>\n	(buy-commodity stone)\n)\n(defrule\n	(goal activate yes)\n	(gold-amount >= 1500)\n	(stone-amount <= 200)\n	(commodity-buying-price stone <= 200)\n	(can-buy-commodity stone)\n	(goal use-market 1)\n=>\n	(buy-commodity stone)\n)\n(defrule\n	(goal activate yes)\n	(wood-amount >= 2000)\n	(or\n		(gold-amount < 200)\n		(food-amount < 200)\n	)\n	(can-sell-commodity wood)\n	(goal use-market 1)\n=>\n	(sell-commodity wood)\n)\n(defrule\n	(goal activate yes)\n	(food-amount >= 2000)\n	(or\n		(gold-amount < 200)\n		(wood-amount < 200)\n	)\n	(can-sell-commodity food)\n	(goal use-market 1)\n=>\n	(sell-commodity food)\n)\n(defrule\n	(goal activate yes)\n	(stone-amount >= 1500)\n	(or\n		(or\n			(gold-amount < 200)\n			(wood-amount < 200)\n		)\n		(food-amount < 200)\n	)\n	(commodity-selling-price stone >= 70)\n	(can-sell-commodity stone)\n	(goal use-market 1)\n=>\n	(sell-commodity stone)\n)"
    
    ##print(finaltext) ## debug
    return finaltext
    
def save_final_files():

    saveloc = tkFileDialog.askdirectory()
    filename = collect_data()["AIName"]
    
    if (filename == ""):
        filename = "myAI"
    
    if saveloc != "":
        f = open(saveloc+"/"+filename+".per",'w')
        f.write(create_final_per_file())
        f.close()
        f2 = open(saveloc+"/"+filename+".ai",'w')
        f2.write(" ")
        f2.close()
        
    print(saveloc+"/"+filename+".per") ## debug
    
def to_top():
    canvas.yview_moveto(0)

outlabel = Label(frame, text="Build AI", width=600, anchor="center")
outlabel.place(x=10,y=1920,width=600)

out1 = Button(frame, text="Save AI data for later", width=20, command=save_json)
out1.place(x=600,y=50)

out2 = Button(frame, text="Load AI data", width=20, command=load_json)
out2.place(x=600,y=100)

out3 = Button(frame, text="Export final AI files", width=20, command=save_final_files)
out3.place(x=250,y=1950)

out4 = Button(frame, text="Return to Top", width=20, command=to_top)
out4.place(x=600,y=1950)

## Main Loop
window.mainloop()