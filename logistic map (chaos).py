###############








def main():
    print()
    variables=handle_input("data input",0)
    result=calc(variables)
    calc_end({"arg_1":result,"arg_2":variables})


def handle_input(arg_1,arg_2):      ####handles input
    func_arg=arg_2                  ####data input if the mode that is choesen 
    if arg_1=="data input":         ####requires/has arguements , input
        a=initialization()          ####arguements as a dictionary into the seond arguement here
        return(a)                   ####eg {"arg1":{"arg":""a},"arg_2":var_2} into the second arguement (arg_2) 
    elif arg_1=="store data":
        a=0
        store_data()
        return()


def initialization():
    input_correct=False
    while input_correct==False:
        vaules_correct=False
        r_vaule=input("r?\n--->")
        initial_x=input("x0?\n--->")
        iterations=input("iterations?\n--->")
        vaules={"int,+,!=0,float,+,!=0":r_vaule,"int,+,!=0,float,+,!=0":initial_x,"int,+,!=0":iterations}
        vaules_correct=check(vaules)
        if vaules_correct==False:
            recorrect(vaules)
        else:
            print("R vaule is "+str(r_vaule))
            print("Initial x vaule (eg x0) is "+str(initial_x))
            print("Iteration amount is "+str(iterations))
            procede=input("Enter correct if above information is correct.\n--->")
            input_correct=procede
    vaules={"r_vaule":float(r_vaule),"initial_x":float(initial_x),"iterations":int(iterations)}    ####do not forget to change type
    return(vaules)



def check(arg_1):
    vaules=arg_1
    for key in vaules:
        if key=="int,+,!=0,float,+,!=0":
            try:
                a=float(vaules[key])
                if a<=0:
                    return(False)
            except:
                return(False)
        elif key=="int,+,!=0":
            try:
                a=int(vaules[key])
                if a<=0:
                    return(False)
            except:
                return(False)
    return(True)



def recorrect(arg_1):
    vaules=arg_1
    correct={}
    i=0
    vaules=arg_1
    for key in vaules:
        if key=="int,+,!=0,float,+,!=0":
            try:
                a=float(vaules[key])
                if a<=0:
                    correct[i]=False
                else:
                    correct[i]=True
            except:
                correct[i]=False
        elif key=="int,+,!=0":
            try:
                a=int(vaules[key])
                if a<=0:
                    correct[i]=False
                else:
                    correct[i]=True
            except:
                correct[i]=False
    return(True)
    for key in correct:
        if correct[key]!=True:
            if key=="1":
                print("r_vaule")
            elif key=="2":
                print("inital_x")
            elif key=="3":
                print("iterations")



def calc(arg_1):
    vaules=arg_1
    r=vaules["r_vaule"]
    x0=vaules["initial_x"]
    iterations=vaules["iterations"] ####do not forget to change type
    i=0
    x=x0
    result={"0":x0}
    while i<iterations:
        i=i+1
        x=calc_step(r,x)
        result[str(i)]=x
    return(result,i)



def calc_step(arg_1,arg_2):
    r=arg_1
    x=arg_2
    x=r*x*(1-x)
    return(x)



def calc_end(arg_1):
    result=arg_1[0]
    result=result[0]
    print("calc done")
    display=input("display?Y/N\n--->")
    while display!="Y":
        display=input("display?Y/N\n--->")
    print(str(result))
    store_data=False
    store_data=input("store data?Y/N\n--->")
    if store_data=="Y":
        handle_input("store data",0)



def store_data():
    a=a





if 1==1:
    main()















