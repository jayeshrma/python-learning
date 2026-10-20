# Using zip()
teams=["MI", "RCB", "SRH", "GT"]
trophies=[5,2,0,1]

for team, trophy in zip(teams,trophies):
    print(f"{team}:{trophies}")