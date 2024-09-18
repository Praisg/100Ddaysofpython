travel_log = [ #this is a list with a dictionary nested
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name,times,place):
    newdic = {}
    newdic["country"]= name
    newdic["visits"]= times
    newdic["cities"]=place
    travel_log.append(newdic)#remember append adds mulist

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



