def func_opps(arg):
    some_list=[1,2,3]
    #some_dict={}
    return print(some_list[arg])
    #return some_dict["a"]
def func_opps2(arg):
    try:
        func_opps(arg)
    except IndexError:
        return print("Error list index out of range")




#func_opps(23)
func_opps2(23)