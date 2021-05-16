f = open("test_cases/tac1.txt","r")
# fout = open("out.txt","w")

list_of_lines = f.readlines()
dictValues = dict()
constantFoldedList = []
print("Quadruple form after Constant Folding and Constant propogation-")
print("-------------------------------------")
for i in list_of_lines:
    i = i.strip("\n")
    op,arg1,arg2,res = i.split()
    # print("i",i)
    if(op =="not"):
        # print(i)
        if(arg1 in dictValues):
            arg1=dictValues[arg1]

        if(arg1=="True"):
            dictValues[res]="False"
            print("=","False","NULL",res)
            constantFoldedList.append(["=","False","NULL",res])
            continue
        
            

        elif(arg1=="False"):
            dictValues[res]="True"
            print("=","True","NULL",res)
            constantFoldedList.append(["=","True","NULL",res])
            continue
    # print("op",op)
    # print("dict",dictValues)
    if(op in ["+","-","*","/"]):
        # print(i)
        if(arg1.isdigit() and arg2.isdigit()):
            result = eval(arg1+op+arg2)
            dictValues[res] = str(result)
            print("=",result,"NULL",res)
            constantFoldedList.append(["=",result,"NULL",res])
        
        elif(arg1.isdigit()):
            if(arg2 in dictValues):
                result = eval(arg1+op+dictValues[arg2])
                dictValues[res] = str(result)
                print("=",result,"NULL",res)
                constantFoldedList.append(["=",result,"NULL",res])
            else:
                print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        
        elif(arg2.isdigit()):
            if(arg1 in dictValues):
                # print("HEHE",dictValues[arg1]+op+arg2)
                # try:
                result = eval(dictValues[arg1]+op+arg2)
                dictValues[res] = str(result)
                print("=",result,"NULL",res)
                constantFoldedList.append(["=",result,"NULL",res])
                # except:
                    # pass
            else:
                print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        else:
            # print("ISME")
            flag1=0
            flag2=0
            arg1Res = arg1
            if(arg1 in dictValues):
                arg1Res = str(dictValues[arg1])
                flag1 = 1
            arg2Res = arg2
            if(arg2 in dictValues):
                arg2Res = str(dictValues[arg2])
                flag2 = 1
            if(flag1==1 and flag2==1):
                result = eval(arg1Res+op+arg2Res)
                dictValues[res] = result
                print("=",result,"NULL",res) 
                constantFoldedList.append(["=",result,"NULL",res])
            else:
                print(op,arg1Res,arg2Res,res)
                constantFoldedList.append([op,arg1Res,arg2Res,res])
                
    elif(op == ">=" or op == ">" or op == "<=" or op == "<" or op == "==" ):
        # print(i,dictValues)
        a1=None 
        a2=None
        if(arg1.isdigit()):
            a1=arg1
        else:
            try:
                a1=dictValues[arg1]
            except:
                pass

        if(arg2.isdigit()):
            a2=arg2
        else:
            try:
                a2=dictValues[arg2]
            except:
                pass

        if(a1 == None or a2==None):
            if(a1!=None):
                pass
            else:
                a1=arg1

            if(a2!=None):
                pass
            else:
                a2=arg2

            print(op,a1,a2,res)
            constantFoldedList.append([op,a1,a2,res])
            continue

        # print(a1+op+a2)
        result=eval(a1+op+a2)
        dictValues[res]=str(result)
        print("=",result,"NULL",res)
        constantFoldedList.append(["=",result,"NULL",res])


            


    elif(op=="="):
        # print(dictValues)
        if(arg1.isdigit()):
            dictValues[res]=arg1
            print("=",arg1,"NULL",res)
            constantFoldedList.append(["=",arg1,"NULL",res])
        else:
            if(arg1 in dictValues):
                print("=",dictValues[arg1],"NULL",res)
                dictValues[res]=dictValues[arg1]
                constantFoldedList.append(["=",dictValues[arg1],"NULL",res])
            else:
                print("=",arg1,"NULL",res)

                constantFoldedList.append(["=",arg1,"NULL",res])

    else:
        # print("uhuhas",i)
        a1=None 
        a2=None
        if(arg1.isdigit()):
            a1=arg1
        else:
            try:
                a1=dictValues[arg1]
            except:
                pass

        if(arg2.isdigit()):
            a2=arg2
        else:
            try:
                a2=dictValues[arg2]
            except:
                pass

        if(a1 == None or a2==None):
            if(a1!=None):
                pass
            else:
                a1=arg1

            if(a2!=None):
                pass
            else:
                a2=arg2
                
            # print(op,a1,a2,res)
            # constantFoldedList.append([op,arg1,arg2,res])
            # continue

        print(op,a1,a2,res)
        constantFoldedList.append([op,a1,a2,res])
    # print(dictValues)

# print(dictValues)
print("\n")
print("Constant folded expression - ")
print("--------------------")
for i in constantFoldedList:
    if(i[0]=="="):
        print(i[3],i[0],i[1])
    elif(i[0] in ["+","-","*","/","==","<=","<",">",">="]):
        print(i[3],"=",i[1],i[0],i[2])
    elif(i[0] in ["if","goto","label","not"]):
        if(i[0]=="if"):
            print(i[0],i[1],"goto",i[3])
        if(i[0]=="goto"):
            print(i[0],i[3])
        if(i[0]=="label"):
            print(i[3],":")
        if(i[0]=="not"):
            print(i[3],"=",i[0],i[1])

print("\n")
print("After dead code elimination - ")
print("------------------------------")
for i in constantFoldedList:
    if(i[0]=="="):
        pass
    elif(i[0] in ["+","-","*","/","==","<=","<",">",">="]):
        print(i[3],"=",i[1],i[0],i[2])
    elif(i[0] in ["if","goto","label","not"]):
        if(i[0]=="if"):
            print(i[0],i[1],"goto",i[3])
        if(i[0]=="goto"):
            print(i[0],i[3])
        if(i[0]=="label"):
            print(i[3],":")
        if(i[0]=="not"):
            print(i[3],"=",i[0],i[1])
                


# print("\n")
# print("After moving loop invariate code outside - ")
# print("------------------------------")
# loopInvariate = []
# # for i in constantFoldedList:
# while(i<len(constantFoldedList)):
#     # if(i[0]=="="):
#     #     pass
#     # elif(i[0] in ["+","-","*","/","==","<=","<",">",">="]):
#         # print(i[3],"=",i[1],i[0],i[2])
#     # if(i[0] in ["if","goto","label","not"]):
#     if(constantFoldedList[i][0] == "label"):
#         l1=[]
#         l2=[]
#         while(i<i<len(constantFoldedList) and constantFoldedList[i][0]!="label"):
#             if(constantFoldedList[i][0] in ["+","-","*","/","==","<=","<",">",">="]):
#             if(i[0]=="if"):
#                 print(i[0],i[1],"goto",i[3])
#             if(i[0]=="goto"):
#                 print(i[0],i[3])
#             if(i[0]=="label"):
#                 print(i[3],":")
#             if(i[0]=="not"):
#                 print(i[3],"=",i[0],i[1])
                

        

