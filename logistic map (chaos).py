###############

import ast






def main():
    variables=handle_input("start",0)
    result=calc(variables)
    calc_end({"arg_1":result,"arg_2":variables})


def handle_input(arg_1,arg_2):      ####handles input
    func_arg=arg_2                  ####data input if the mode that is chosen requires/has arguement
    if arg_1=="start":              ####eg {"arg1":{"arg":""a},"arg_2":var_2} into the second arguement (arg_2)
        a=start()
        return(a)
    elif arg_1=="data input":
        a=initialization()
        return(a)
    elif arg_1=="load data":
        a=load_data()
        return(a)
    elif arg_1=="store data":
        store_data(func_arg)
        return()
    elif arg_1=="file name get load":
        a=get_gile_name_load()      ####handles getting a file name to load
        return(a)
    elif arg_1=="file name get dump":
        a=get_file_name_dump()      ####handles getting the file name to output results
        return(a)
    
    
    
def start():                        ####allows for either file loading or direct data input
    ready=False
    while ready==False:
        load_file=input("Do you want to load a file?Y/N\n---->")
        if load_file=="Y":
            file_name=get_file_name_load()
            file=open(file_name,"r")
            a=file.read()
            a=ast.literal_eval(a)
            a=a["input"]
            print("File initial parameters loaded.")
            ready=True
        else:
            a=initialization()
            ready=True
            print("Inputs loaded.")
    procede=False
    while procede!="Y":
        procede=input("Start caculation?Y/N\n---->")
    print("----------------------------")
    return(a)




def get_file_name_load():               ####gets a file name and tests contents for validity
    sucess=False
    print("")
    while sucess==False:
        file_name=input("Name of file to load?\n---->")
        file_name=str(file_name)+".txt"
        try:
            with open(file_name,"r") as file:
                print("File "+file_name+" found.")
                try:                    ####input may be malformed
                    a=file.read()
                    a=ast.literal_eval(a)
                    try:                ####input could be another data type (not a dictionary)
                        a=a["input"]
                        r_vaule=a["r_vaule"]
                        initial_x=a["initial_x"]
                        iterations=a["iterations"]
                        a={"1":r_vaule,"2":initial_x,"3":iterations}
                        valid=check(a)
                        if valid==True:
                            sucess=True
                            print("File parameters are as follows:")
                            print("R vaule is "+str(r_vaule))
                            print("Initial x vaule (eg x0) is "+str(initial_x))
                            print("Iteration amount is "+str(iterations))
                        else:
                            print("Failed to import file.\nFile may be corrupted or not correct.")
                    except:
                        print("Failed to import file.\nFile may be corrupted or not correct.")
                except:
                    print("Failed to import file.\nFile may be corrupted or not correct.")
        except FileNotFoundError:
            print("File "+file_name+" not found.")
    return(file_name)




def initialization():               ####handles initialization
    input_correct=False             ####output: {"r_vaule":float(r_vaule),"initial_x":float(initial_x),"iterations":int(iterations)}
    while input_correct==False:
        vaules_correct=False
        r_vaule=input("r?\n--->")
        initial_x=input("x0?\n--->")
        iterations=input("iterations?\n--->")
        vaules={"1":r_vaule,"2":initial_x,"3":iterations}
        vaules_correct=check(vaules)
        if vaules_correct==False:
            recorrect(vaules)
        else:
            print("R vaule is "+str(r_vaule))
            print("Initial x vaule (eg x0) is "+str(initial_x))
            print("Iteration amount is "+str(iterations))
            procede=input("Enter correct if above information is correct.\n--->")
            input_correct=procede
    vaules={"r_vaule":float(r_vaule),"initial_x":float(initial_x),"iterations":int(iterations)}
    return(vaules)



def check(arg_1):                   ####checks for the type and ranges correctness of input
    vaules=arg_1
    try:
        a=vaules["1"]
        b=vaules["2"]
        c=vaules["3"]
        a=float(a)
        if a<=0:
            return(False)
        b=float(b)
        if b<=0:
            return(False)
        c=int(c)
        if c<=0:
            return(False)
    except:
        return(False)
    return(True)



def recorrect(arg_1):                   ####if check()==False this function will output needed corrections to console
    vaules=arg_1
    correct={}
    a=vaules["1"]
    b=vaules["2"]
    c=vaules["3"]
    try:
        a=float(a)
        if a<=0:
            print("R vaule must not be negative or zero.")
    except:
        print("R vaule must be a nonegative, non zero float/int.")
    try:
        b=float(b)
        if b<=0:
            print("Initial x vaule must not be negative or zero.")
    except:
        print("Initial x vaule must be a nonegative, non zero float/int.")
    try:
        c=int(c)
        if c<=0:
            print("Iterations must not be negative or zero.")
    except:
        print("Iterations must be a nonegative non zero int.")




def calc(arg_1):                        ####handles iterating x
    print("Calculations started.")
    vaules=arg_1
    r=vaules["r_vaule"]
    x0=vaules["initial_x"]
    iterations=vaules["iterations"] ####do not forget to change type
    i=0
    x=x0
    result={"0":x0}
    while i<iterations:
        i=i+1
        print("Iteration "+str(i))
        x=calc_step(r,x)
        print("X="+str(x))
        result[str(i)]=x
    return(result)



def calc_step(arg_1,arg_2):             ####single step /iteration 
    r=arg_1
    x=arg_2
    x=r*x*(1-x)
    return(x)



def calc_end(arg_1):                    ####output
    result=arg_1["arg_1"]
    print("calc done")
    display=input("display?Y/N\n--->")
    while display!="Y":
        display=input("display?Y/N\n--->")
    print(str(result))
    store_data=False
    store_data=input("store data?Y/N\n--->")
    if store_data=="Y":
        handle_input("store data",arg_1)



def store_data(arg_1):                  ####if one wants to dump results
    results=arg_1["arg_1"]
    variables=arg_1["arg_2"]
    print("results "+str(results))
    print("variables "+str(variables))
    data={"input":variables,"results":results}
    file_name=handle_input("file name get dump",0)
    file=open(file_name,"w")
    file.write(str(data))
    file.close()
    print("Data stored at "+file_name+".")
    
    


def get_file_name_dump():           ####get file name
    sucess=False
    print("---Warinig---\nThis program will wipe any data in a provided file name.")
    i=0
    while sucess==False:
        i+1
        if i==3:
            print("---Warinig---\nThis program will wipe any data in a provided file name.")
            i=1
        new_file=input("Do you wnat to create a new file?Y/N\n---->")
        if new_file=="Y":
            file_name=input("New file name?\n---->")
            file_name=str(file_name)+".txt"
            try:
                file=open(file_name,"x")
                print("File "+file_name+" created sucessfully")
                file.close()
                sucess=True
            except FileExistsError:
                print("File"+file_name+" already exists.")
        else:
            file_name=input("File name?\n---->")
            file_name=str(file_name)+".txt"
            try:
                file=open(file_name)
                print("File "+file_name+" found.")
                file.close()
                sucess=True
            except FileNotFoundError:
                print("File "+file_name+" not found.")
    return(file_name)



if 1==1:
    main()
