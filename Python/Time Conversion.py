def timeConversion(s):
    #Version 1 beginner
    components = s.split(":")
    if "AM" in components[2]:
        components[2] = components[2].replace("AM", '')
        if components[0] == "12":
            return "00:%s:%s"%(components[1], components[2])
        else:
            return "%s:%s:%s"%(components[0], components[1], components[2])
    else:
        components[2] = components[2].replace("PM", '')
        if int(components[0]) == 12:
            return "%s:%s:%s"%(components[0], components[1], components[2])
        else:
            new = int(components[0]) + 12
            components[0] = str(new)
            return "%s:%s:%s"%(components[0], components[1], components[2]) 
        
        
def timeConversion(s):
   #Version 2 after I have grown
    t = s.split(":")
    if "PM" in t[2]:
        if int(t[0]) == 12:
            return "%s:%s:%s"%(t[0],t[1],t[2][:2])
        else:
            t[0] = str(int(t[0]) + 12)
            return "%s:%s:%s"%(t[0],t[1],t[2][:2])
    elif "AM" in t[2] and int(t[0]) == 12:
        return "00:%s:%s"%(t[1], t[2][:2])
    else:
        return "%s:%s:%s"%(t[0],t[1],t[2][:2])