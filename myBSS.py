# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:27:31 2015

@author: louiscarnec
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 22:29:47 2015

@author: louiscarnec
"""

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
            if branchType == "==" and regs[i] == regs[j]: node = left
            if branchType == ">=" and regs[i] >= regs[j]: node = left
            node = right
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


#1/x = S^(1/2)
#x_(n+1) = (x_n / 2) (3 - (S)(x^2_1))



code["1"] = ["multiply",2,2]    ; outgoing["1"] = "sqr1"
code["sqr1"] = ["copy",0,3]    ; outgoing["sqr1"] = "multS"
code["multS"] = ["multiply",3,1]    ; outgoing["multS"] = "multCop"
code["multCop"] = ["copy",0,4]    ; outgoing["multCop"] = "nowSub"
code["nowSub"] = ["subtract",11,4]    ; outgoing["nowSub"] = "copySub"
code["copySub"] = ["copy",0,5]    ; outgoing["copySub"] = "division1"
code["division1"] = ["divide",2,12]    ; outgoing["division1"] = "copyDiv"
code["copyDiv"] = ["copy",0,9]    ; outgoing["copyDiv"] = "anotherMult"
code["anotherMult"] = ["multiply",5,9]    ; outgoing["anotherMult"] = "copyMult"
code["copyMult"] = ["copy",0,6]    ; outgoing["copyMult"] = "iterate1"
code["iterate1"] = ["multiply",6,6]    ; outgoing["iterate1"] = "sqr1"

#S = 4.0
#x_1 = 1.3 
bss(code,outgoing, [0.0,0.33,0.66,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,3.0,2.0],"1")           
            