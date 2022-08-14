import os
Types = [
  {
    'Name' : 'Normal',
    'Weaknesses' : ['Fighting'],
    'Resistances' : [],
    'Immunities' : ['Ghost']
  },
  {
    'Name' : 'Fighting',
    'Weaknesses' : ['Flying', 'Fairy', 'Psychic'],
    'Resistances' : ['Bug', 'Dark', 'Rock'],
    'Immunities' : []
  },
  {
    'Name' : 'Flying',
    'Weaknesses' : ['Electric', 'Ice', 'Rock'],
    'Resistances' : ['Bug', 'Fighting', 'Grass'],
    'Immunities' : ['Ground']
  },
  {
    'Name' : 'Poison',
    'Weaknesses' : ['Ground', 'Psychic'],
    'Resistances' : ['Fighting', "Poison", 'Bug', 'Grass', 'Fairy'],
    'Immunities' : []
  },
  {
    'Name' : 'Ground',
    'Weaknesses' : ['Grass', 'Ice', 'Water'],
    'Resistances' : ['Poison', 'Rock'],
    'Immunities' : ['Electric']
  },
  {
    'Name' : 'Rock',
    'Weaknesses' : ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'],
    'Resistances' : ['Fire', 'Flying', 'Normal', 'Poison'],
    'Immunities' : []
  },
  {
    'Name' : 'Bug',
    'Weaknesses' : ['Fire', 'Flying', 'Rock'],
    'Resistances' : ['Fighting', 'Grass', 'Ground'],
    'Immunities' : []
  },
  {
    'Name' : 'Ghost',
    'Weaknesses' : ['Dark', 'Ghost'],
    'Resistances' : ['Bug', 'Poison'],
    'Immunities' : ['Normal', 'Fighting']
  },
  {
    'Name' : 'Steel',
    'Weaknesses' : ['Fighting', 'Fire', 'Ground'],
    'Resistances' : ['Bug', 'Dragon', 'Fairy', 'Flying', 'Grass', 'Ice', 'Normal', 'Psychic', 'Rock', 'Steel'],
    'Immunities' : ['Poison']
  },
  {
    'Name' : 'Fire',
    'Weaknesses' : ['Water', 'Rock', 'Ground'],
    'Resistances' : ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'],
    'Immunities' : []
  },
  {
    'Name' : 'Water',
    'Weaknesses' : ['Electric', 'Grass'],
    'Resistances' : ['Fire', 'Ice', 'Steel', 'Water'],
    'Immunities' : []
  },
  {
    'Name' : 'Grass',
    'Weaknesses' : ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'],
    'Resistances' : ['Electric', 'Grass', 'Ground', 'Water'],
    'Immunities' : []
  },
  {
    'Name' : 'Electric',
    'Weaknesses' : ['Ground'],
    'Resistances' : ['Electric', 'Flying', 'Steel'],
    'Immunities' : []
  },
  {
    'Name' : 'Psychic',
    'Weaknesses' : ['Bug', 'Dark', 'Ghost'],
    'Resistances' : ['Fight', 'Psychic'],
    'Immunities' : []
  },
  {
    'Name' : 'Ice',
    'Weaknesses' : ['Fighting', 'Fire', 'Rock', 'Steel'],
    'Resistances' : ['Ice'],
    'Immunities' : []
  },
  {
    'Name' : 'Dragon',
    'Weaknesses' : ['Dragon', "Fairy", "Ice"],
    'Resistances' : ['Electric', 'Fire', 'Grass', 'Water'],
    'Immunities' : []
  },
  {
    'Name' : 'Dark',
    'Weaknesses' : ['Bug', 'Fairy', 'Fighting'],
    'Resistances' : ['Dark', 'Ghost'],
    'Immunities' : ['Psychic']
  },
  {
    'Name' : 'Fairy',
    'Weaknesses' : ['Poison', 'Steel'],
    'Resistances' : ['Bug', 'Dark', 'Fighting'],
    'Immunities' : ['Dragon']
  }
]
Tests = [
#0-Any-Any
  lambda Type1, Type2 : True,
#1-Any-Immune
  lambda Type1, Type2 : (Type1['Name'] in Type2['Immunities']),
#2-Any-Neutral
  lambda Type1, Type2 : (Type1['Name'] not in Type2['Resistances']) and (Type1['Name'] not in Type2['Weaknesses']) and  (Type1['Name'] not in Type2['Immunities']),
#3-Any-Resist
  lambda Type1, Type2 : (Type1['Name'] in Type2['Resistances']),
#4-Any-Weak
  lambda Type1, Type2 : (Type1['Name'] in Type2['Weaknesses']),
#5-Immune-Immune
  lambda Type1, Type2 : (Type1['Name'] in Type2['Immunities']) and  (Type2['Name'] in Type1['Immunities']),
#6-Immune-Neutral
  lambda Type1, Type2 : (Type1['Name'] in Type2['Immunities'] ) and  ( Type2['Name'] not in Type1['Resistances'] ) and  (Type2['Name'] not in Type1['Weaknesses'] ) and  (Type2['Name'] not in Type1['Immunities']),
#7-Immune-Resist
  lambda Type1, Type2 : (Type1['Name'] in Type2['Immunities']) and  (Type2['Name'] in Type1['Resistances']),
#8-Immune-Weak
  lambda Type1, Type2 : (Type1['Name'] in Type2['Immunities'] ) and  ( Type2['Name'] in Type1['Weaknesses']),
#9-Neutral-Neutral
  lambda Type1, Type2 : (Type1['Name'] not in Type2['Resistances'] ) and  ( Type1['Name'] not in Type2['Weaknesses'] ) and  ( Type1['Name'] not in Type2['Immunities'] ) and  ( Type2['Name'] not in Type1['Resistances'] ) and  ( Type2['Name'] not in Type1['Weaknesses'] ) and  (  Type2['Name'] not in Type1['Immunities']),
#10-Neutral-Resist
  lambda Type1, Type2 : (Type1['Name'] in Type2['Resistances'] ) and  ( Type2['Name'] not in Type1['Resistances'] ) and  ( Type2['Name'] not in Type1['Weaknesses'] ) and  (  Type2['Name'] not in Type1['Immunities']),
#11-Neutral-Weak
  lambda Type1, Type2 : (Type1['Name'] in Type2['Weaknesses'] ) and  ( Type2['Name'] not in Type1['Resistances'] ) and  ( Type2['Name'] not in Type1['Weaknesses'] ) and  (  Type2['Name'] not in Type1['Immunities']),
#12-Resist-Resist
  lambda Type1, Type2 : (Type1['Name'] in Type2['Resistances'] ) and  ( Type2['Name'] in Type1['Resistances']),
#13-Resist-Weak
  lambda Type1, Type2 : (Type1['Name'] in Type2['Weaknesses'] ) and  ( Type2['Name'] in Type1['Resistances']),
#14-Weak-Weak
  lambda Type1, Type2 : (Type1['Name'] in Type2['Weaknesses'] ) and  ( Type2['Name'] in Type1['Weaknesses'])
]

def clearConsole():
    """Clears the terminal"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#Methods to find trios
def FindTrio(Test):
  global OGType
  for type in Types:
    OGType += 1
    FindMatch(type, Test)
  print("Done")
def FindMatch(Count, Test):
  global layerCount
  global OGType
  layerCount += 1
  for type in range(OGType, len(Types)):
    if(Tests[Test](Types[type], Count)):
      if(layerCount == 2):
        if(Tests[Test](Types[OGType], Types[type])):
          print(Types[OGType]['Name'] + " " + Count['Name'] + " " + Types[type]['Name'])
      else:
        FindMatch(Types[type], Test)
  layerCount = layerCount - 1

while(True):
  OGType = -1
  layerCount = 0
  print("""Which test will you use?
[00]Any-Any
[01]Any-Immune
[02]Any-Neutral
[03]Any-Resist
[04]Any-Weak
[05]Immune-Immune
[06]Immune-Neutral
[07]Immune-Resist
[08]Immune-Weak
[09]Neutral-Neutral
[10]Neutral-Resist
[11]Neutral-Weak
[12]Resist-Resist
[13]Resist-Weak
[14]Weak-Weak""")
  testChoice = input()
  try:
    if(int(testChoice) in range(0, len(Tests))):
      FindTrio(int(testChoice))
    else:
      ("That is not a valid test number")
  except ValueError:
    print("That is not a valid test number")
  print("Press enter to reset")
  input()
  clearConsole()
