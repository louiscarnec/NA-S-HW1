def bss(code, outgoing, initValues= [0.0], initNode ="1"):
    regs = initValues
    node = initNode
    counter = 0
    while outgoing.has_key(node) and counter<100:
        counter += 1
        print counter, ":", node, code[node]
        nodeType == code[node][0]
        if nodetype == "branch":
            branchType == code[node][1]
            (i,j) = code[node][2:]
            (left, right) = outgoing[node]
            if branchType == "<=" and regs[i] <= regs[j]: node = left
            if branchType == "==" and regs[i] == regs[j]: node = left
            if branchType == ">=" and regs[i] >= regs[j]: node = left
            node = right
        else:
            (i, j) = code[node][1:]
            if nodeType == "assign": regs[i] = j
            elif nodeType == "assign": regs[i] = j
            elif nodeType == "copy": regs[i] = regs[j]
            elif nodeType == "add": regs[0] = regs[1] + regs[2]
            elif nodeType == "subtract": regs[0] = regs[1] - regs[2]                
            elif nodeType == "multiply": regs[0] = regs[1] * regs[2]
            elif nodeType == "divide": regs[0] = regs[1] / regs[2]
            else: print "Unknown instruction"
            node = outgoing [node]
            
outgoing = [" "," "," "," "]            
code["copy"] = {}
code["copy"][0] = (1, 1)
 
bss(code, outgoing, 0.0, "1")
                
            