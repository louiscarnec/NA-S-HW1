def turing(code, tape, initPos = 0, initState = "initial"):
  position = initPos
  state = initState
  while state != "halt":
    print state, ": position", position, "in", tape
    symbol = tape[position]
    (symbol, direction, state) = code[state][symbol]
    if symbol != "noWrite": tape[position] = symbol
    position += direction

#This code marks the start of both unary numbers using A and B for arguments
#1 and 2 respectively.
code = {}

code["initial"] = {}
code["initial"][" "] = (" ", 1, "goRightA")

code["goRightA"] = {}
code["goRightA"]["1"] = ("A", 1, "goRighttimes")

code["goRighttimes"] = {}
code["goRighttimes"]["1"] = ("1", 1, "goRighttimes")
code["goRighttimes"][" "] = ("*", 1, "arg2")

code["arg2"] = {}
code["arg2"]["1"] = ("B", 1, "goRight2")

code["goRight2"] = {}
code["goRight2"]["1"] = ("1", 1, "goRight2")
code["goRight2"][" "] = ("E", 1, "newArg")

#A new arg is created by writing 1 following the blank after the second arg,
#where the answer to the unary multiplication will be printed.
code["newArg"] = {}
code["newArg"][" "] = ("1", 1, "printed1")

code["printed1"] = {}
code["printed1"][" "] = (" ", -1, "toStart")

#We then return to the start.
code["toStart"] = {}
code["toStart"]["1"] = ("1", -1, "toStart")
code["toStart"]["X"] = ("X", -1, "toStart")
code["toStart"]["*"] = ("*", -1, "toStart")
code["toStart"]["B"] = ("B", -1, "toStart")
code["toStart"]["E"] = ("E", -1, "toStart")
code["toStart"]["Y"] = ("Y", 1, "pass1") 
code["toStart"]["A"] = ("A", 1, "pass1")
code["toStart"][" "] = (" ", 1, "testArg1")

#print X to iterate over arg 1
code["pass1"] = {}
code["pass1"][" "] = (" ", 1, "finish")
code["pass1"]["A"] = ("X", 1, "toArg2")
code["pass1"]["X"] = ("X", 1, "pass1")
code["pass1"]["1"] = ("X", 1, "toArg2")

#skip to arg 2
code["toArg2"] = {}
code["toArg2"]["1"] = ("1", 1, "toArg2")
code["toArg2"]["*"] = ("*", 1, "markArg2")

#mark argument 1
code["markArg2"] = {}
code["markArg2"]["B"] = ("Y", 1, "gotoPrint")
code["markArg2"]["Y"] = ("Y", 1, "markArg2")
code["markArg2"]["1"] = ("Y", 1, "gotoPrint")

#after marking arg 2 we print 1 in the new arg and back up.
code["gotoPrint"] = {}
code["gotoPrint"]["1"] = ("1", 1, "gotoPrint")
code["gotoPrint"]["E"] = ("E", 1, "gotoPrint")
code["gotoPrint"][" "] = ("1", -1, "backingUp")

#backing up over arg 2.
code["backingUp"] = {}
code["backingUp"]["1"] = ("1", -1, "backingUp")
code["backingUp"]["E"] = ("E", -1, "backingUp")
code["backingUp"]["Y"] = ("Y", -1, "backingup")
code["backingUp"]["*"] = ("*", 1, "testArg2")

#testing to see if arg 2 has been fully marked. if not go back to marking.
code["testArg2"] = {}
code["testArg2"]["Y"] = ("Y", 1, "testArg2")
code["testArg2"]["1"] = ("Y", 1, "gotoPrint")
code["testArg2"]["E"] = ("E", -1, "eraseMarks2")

#erase the Ys.
code["eraseMarks2"] = {}
code["eraseMarks2"]["Y"] = ("1", -1, "eraseMarks2")
code["eraseMarks2"]["*"] = ("*", -1, "toStart")

#testing to see if arg 1 is fully market. if not go back to marking.
code["testArg1"] = {}
code["testArg1"][" "] = (" ", 1, "testArg1")
code["testArg1"]["X"] = ("X", 1, "testArg1")
code["testArg1"]["1"] = ("X", 1, "toArg2")
code["testArg1"]["*"] = ("*", -1, "eraseMark1")

#erase marks from arg 1
code["eraseMark1"] = {}
code["eraseMark1"]["X"] = ("1", -1, "eraseMark1")
code["eraseMark1"]["1"] = ("1", -1, "eraseMark1")
code["eraseMark1"][" "] = (" ", 1, "finishingUp")

#finishing up by getting rid of symbols
code["finishingUp"] = {}
code["finishingUp"][" "] = (" ", 1, "finishingUp")
code["finishingUp"]["1"] = ("1", 1, "finishingUp")
code["finishingUp"]["*"] = (" ", 1, "finishingUp")
code["finishingUp"]["E"] = (" ", -1, "finished")

code["finished"] = {}
code["finished"]["1"] = ("1", -1, "finished")
code["finished"][" "] = (" ", -1, "done")

code["done"] = {}
code["done"]["1"] = ("1", -1, "done")
code["done"][" "] = ("1", 0, "halt")

#added blank spaces because list is finite.
turing(code, [" ", "1", "1", "1", " ", "1", "1", "1", "1", " ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "], 0, "initial")