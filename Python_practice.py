print("Hello World")

n=18

if n>25:
    print("Davai")
elif n>20:
    print("Vamos")
else:
    print("Komm Jetz")

cats=["Barsik","Lucie","Froshka","Lynx"]
print(cats[3])

cats.append("Misha")
print(cats)

name="Freddie"
age=33
height="173 cm"
print("Hello, my name is "+name)
print(f"I am {height} tall")
print(f"I am {age} years old.")
print("My name is "+name)
print("Hello "+ str(age) + "."+ str(height))
cats[3]="Froska"
print(cats)
cats.append("Tavarish")
print(cats)
People_sighted={"Fred":6,"Toto":4,"Romeo":7}
print(People_sighted)
print(People_sighted["Fred"])

print(5+2*3)
print(3**3%5)
print(5+9*3/2-4)
print(16-3/2+7-1)

counties=["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[2])
counties.append("El Paso")
print(counties)
counties.insert(0,"Toronto")
print(counties)
counties.remove("Toronto")
print(counties)
counties.append("Toronto")
print(counties)
counties.pop(4)
print(counties)
counties.pop(3)
print(counties)
counties.insert(1,"El Paso")
print(counties)
counties.pop(0)
print(counties)
counties.insert(1,"Jefferson")
counties.pop(3)
print(counties)
counties.append("Arapahoe")
print(counties)

counties_tuple=("Arapahoe","Denver","Jefferson")
print(counties_tuple)

counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print(len(counties))
print(counties_dict)
x=counties_dict.keys()
print(x)
y=counties_dict.values()
print(y)
z=counties_dict.items()
print(z)
print(counties_dict.get("Denver"))
print(counties_dict.keys())
print(counties_dict["Arapahoe"])

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
print(voting_data)

voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
print(voting_data)
voting_data.pop(0)
print(voting_data)
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.pop(1)
print(voting_data)
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print(voting_data)


counties=["Arapahoe","Denver","Jefferson"]
if counties[1]=="Denver":
    print(counties[1])
if str("Arapahoe") in counties and str("El Paso") in counties:
    print("Arapahoe and El Paso in the list of counties")
else:
    print("Arapahoe or El Paso not in the list of counties.")

x=5
y=5
if x==5 and y==5:
    print("True")
else:
    print("False")


x=0
while x<=5:
    print(x)
    x=x+1
for county in counties:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))
for county, voters in counties_dict.items():
    print(county, voters)

for county_dict in voting_data:
    print(county_dict)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

