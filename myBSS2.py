def bss(code, outgoing,initValues=[0.0],initNode="1"):
    regs = initValues
    node = initNode
    counter = 0
    while outgoing.has_key(node) and counter < 50 :
        counter += 1
        print counter, ":", node, code[node]
        nodeType = code[node][0]
        if nodeType == "branch":
            branchType = code[node][1]
            (i, j) = code[node][2:]
            (left, right) = outgoing[node]
            if branchType == "<=" and regs[i] <= regs[j]: node = left
            elif branchType == "==" and regs[i] == regs[j]: node = left
            elif branchType == ">=" and regs[i] >= regs[j]: node = left
            else: node = right
        else:
            (i , j) = code [node][1:]
            if nodeType == "assign": regs[i] = j
            elif nodeType == "copy": regs[j] = regs[i]
            elif nodeType == "add": regs[0] = regs[i] + regs[j]
            elif nodeType == "subtract": regs[0] = regs[i] - regs[j]
            elif nodeType == "multiply": regs[0] = regs[i] * regs[j]
            elif nodeType == "divide": regs[0] = regs[i] / regs[j]
            else: print " unknown"
            node = outgoing [node]    
        print regs   
            
code = {}
outgoing={}
#x_(n+1) = (1 / 2) (x_n + S / x_n)

code["1"] = ["divide",2,1]    ; outgoing["1"] = "copDiv"
code["copDiv"] = ["copy",0,9]    ; outgoing["copDiv"] = "add1"
code["add1"] = ["add",1,9]    ; outgoing["add1"] = "copAdd1"
code["copAdd1"] = ["copy",0,8]    ; outgoing["copAdd1"] = "divBy2"
code["divBy2"] = ["divide",8,11]    ; outgoing["divBy2"] = "cop4Crit"
code["divBy2"] = ["divide",8,11]    ; outgoing["divBy2"] = "cop4Crit"

code["cop4Crit"] = ["copy",0,7]    ; outgoing["cop4Crit"] = "crit2Stop1"
code["crit2Stop1"] = ["subtract",7,1]    ; outgoing["crit2Stop1"] = "sqrDiff"
code["sqrDiff"] = ["multiply",0,0]    ; outgoing["sqrDiff"] = "copIt"
code["copIt"] = ["copy",0,6]    ; outgoing["copIt"] = "test"
code["test"] = ["branch","<=",6,12]    ; outgoing["test"] = "halt","2"
code["2"] = ["divide",7,1]    ; outgoing["2"] = "copDiv"
code["halt"] = []

#S = 3.0
#x_1 = 2.0 
bss(code,outgoing, [0.0,1.4,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,2.0,0.0004],"1")           
            