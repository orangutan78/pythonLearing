dic={"a":{"psw":1,"msg":{1:"11",2:"22",3:"33"}},"b":{"psw":2,"msg":{1:"22"}}}
#print(dic["a"]["c"])
print(dic["a"].get("psw"))
print(len(dic["a"]["msg"]))
print(dic["a"]["msg"].get(1))

dic["a"].update({"psw":2})
print(dic)
