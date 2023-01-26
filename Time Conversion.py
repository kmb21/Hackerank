def timeConversion(s):
    # Write your code here
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
