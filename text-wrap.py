def wrap(string, max_width):
    string_container = []
    output = ''
    for i in range(len(string)):
        if i%max_width !=0:
            continue
        else:
            try:string_container.append(string[i:i+max_width])
            except:...
        
    for j, i in enumerate(string_container):
        if j == len(string_container)-1:
            output+= i 
        else:
            output+= i + "\n"
    return output
