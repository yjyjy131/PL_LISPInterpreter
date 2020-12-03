import parse


    #eval function get value by parse_tree from parser.
    #this function will traverse parse_tree by child to root order and sequentially get value.


def eval(var_dict,tree_root,ident_calc=False):

    if(type(tree_root)!=parse.TreeNode):return "Error"
    #print(tree_root.postorder())
    #print(tree_root.depth())

    if tree_root.data[0] =='literal':
        result=function_literal(var_dict,tree_root)
        return result

    elif tree_root.data[0] =='string':
        result=function_literal(var_dict,tree_root)
        return result

    elif tree_root.data[0] =='literal_list':
        result=function_literal(var_dict,tree_root)
        return result

    elif tree_root.data[0] =='variable':
        result=function_variable(var_dict,tree_root)
        return result

    elif tree_root.data[0] =='false':
        result=function_false(var_dict,tree_root)
        return result

    elif tree_root.data[0] =='true':
        result=function_true(var_dict,tree_root)
        return result


    elif tree_root.data[0]=='ident':
        result=function_ident(var_dict,tree_root,ident_calc)
        return result

    # if it is parse_tree of arithmetic function
    elif tree_root.data[0] in ['/','*','+','-']:
        result = function_calculus(var_dict,tree_root)
        return result

    # if it is parse_tree of SETQ function

    elif tree_root.data[0] == 'setq':
        result = function_setq(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'list':
        result=function_list(var_dict,tree_root)
        return result

    elif tree_root.data[0]=='car':
        result=function_car(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'cdr':
        result=function_cdr(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'nth':
        result=function_nth(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'length':
        result=function_length(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'assoc':
        result=function_assoc(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'cons':
        result=function_cons(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'reverse':
        result=function_reverse(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'append':
        result=function_append(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'member':
        result=function_member(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'remove':
        result=function_remove(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'subst':
        result=function_subst(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'cond':
        result=function_cond(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'if':
        result=function_if(var_dict,tree_root)
        return result

    elif tree_root.data[0] == 'print':
        result=function_print(var_dict,tree_root)
        return result
    # TODO eval data0?
    elif tree_root.data[0] == 'atom':
        result = func_atom(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'null':
        result = func_null(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'numberp':
        result = func_numberp(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'zerop':
        result = func_zerop(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'minusp':
        result = func_minusp(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'equal':
        result = func_eqaul(var_dict, tree_root)
        return result

    elif tree_root.data[0] == '=':
        result = func_eqaul(var_dict, tree_root)
        return result

    elif tree_root.data[0] == '<':
        result = func_less_than(var_dict, tree_root)
        return result

    elif tree_root.data[0] == '>':
        result = func_greater_than(var_dict, tree_root)
        return result

    elif tree_root.data[0] == '>=':
        result = func_greater_equal(var_dict, tree_root)
        return result
    
    elif tree_root.data[0] == '<=':
        result = func_less_equal(var_dict, tree_root)
        return result

    elif tree_root.data[0] == 'stringp':
            result = func_stringp(var_dict, tree_root)
            return result

    elif tree_root.data[0] == 'print':
        result = func_print(var_dict, tree_root)
        return result
    """
    elif(tree_root.data[1]==다른함수):
        다른 함수에 대한 eval 함#tn
    """
#################################TypeCheck method###################################
def type_check(var_dict,target):

    if(target[0]=="ident"):
        if(target[1] in var_dict):
            return var_dict[target[1]][0]
        else:
            print("Value Error : there is no "+"'"+target[1]+"'")
            raise NotImplementedError
    else: return target[0]
#################################TypeCheck method###################################


################################# literal method###################################
def function_literal(var_dict,tree_root):
    return tree_root.data
################################# literal method###################################


################################# literal_list method###################################
def function_literal_list(var_dict,tree_root):
    return tree_root.data
################################# literal_list method###################################


################################# string method###################################
def function_string(var_dict,tree_root):
    return tree_root.data
################################# string method###################################

################################# true method###################################
def function_true(var_dict,tree_root):
    return tree_root.data
################################# true method###################################


################################# false method###################################
def function_false(var_dict,tree_root):
    return tree_root.data
################################# false method###################################



################################# ident method###################################
def function_ident(var_dict,tree_root,ident_calc):
    if ident_calc==False:
        return tree_root.data
    if ident_calc==True:
        if(tree_root.data[0]=="ident"):
            if(tree_root.data[1] in var_dict):
                return var_dict[tree_root.data[1]]
            else:
                print("Value Error : there is no "+"'"+tree_root.data[1]+"'")
                raise NotImplementedError

################################# ident method###################################

################################# variable method###################################
def function_variable(var_dict,tree_root):
    return ('ident',tree_root.data[1])
################################# variable method###################################


################################# calculus method###################################
#입력한 문자열을 숫자로 변환해줌(실수/정수 반영)
def float_or_int(string):
    if '.' in string:
        index=string.index('.')
        temp=string[index+1:]
        for i in temp:
            if i!='0':
                return float(string)

        return int(float(string))
    else:
        return int(string)

def function_calculus(var_dict,tree_root):
    result=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,result)!="literal"):
        print(tree_root.data[1]+"Type Error")
        raise NotImplementedError
    result=float_or_int(result[1])
    if tree_root.data[0]=='+':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("+ Type Error")
                raise NotImplementedError
            result = result + float_or_int(check[1])
    if tree_root.data[0]=='-':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("- Type Error")
                raise NotImplementedError
            result = result - float_or_int(check[1])
    if tree_root.data[0]=='*':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("* Type Error")
                raise NotImplementedError
            result = result * float_or_int(check[1])
    if tree_root.data[0]=='/':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("/ Type Error")
                raise NotImplementedError
            result = result / float_or_int(check[1])

    return ('literal',str(result))
############################################calculus method##############################################


#########################################list method###################################################
def is_literal_list(treenode):
    if treenode.data[0]=='literal_list':
        return True
    else:
        return False

def function_list(var_dict,tree_root):
    result = str()
    for index, child in enumerate(tree_root.children):
        if index==0:
            result=eval(var_dict,child,True)[1]

        else:
            result = result + " "+eval(var_dict,child,True)[1]

    return ('literal_list','('+result+')')
#########################################list method###################################################


#########################################setq method###################################################
def function_setq(var_dict,tree_root):
    return_list=list()
    if len(tree_root.children)%2!=0:
        return "Error : setq parameter number is odd"
    for index, child in enumerate(tree_root.children):
        if (index%2)==0:
            variable=eval(var_dict,child,False)
            if variable[0]!='ident':
                print("setq function even variable is not ident")
                raise NotImplementedError

        elif (index%2)!=0:
            value=eval(var_dict,child,True)
            var_dict[variable[1]]=value
            return_list.append(value)
    return return_list[len(return_list)-1]

#########################################setq method###################################################


#########################################car method###################################################
#string 형태로 저장된 literal_list 의 lexeme을 파이썬 list형태로 반환
#원소는 다 string 으로 저장됨
def literal_list_to_list(string_literal_list):
    result=list()
    temp=string_literal_list[1:-1]
    temp=temp.strip()
    while(1):
        try:
            index_start=temp.index('(')
            if index_start!=0:
                result.extend(temp[:index_start].split())

            index_end=temp.index(')')

            while(1):
                if index_end+1<len(temp):
                    if temp[index_end+1]==')':
                        index_end = index_end+1
                    else:
                        break
                else:
                    break

            temp_literal_list=temp[index_start:index_end+1]
            result.append(temp_literal_list)
            temp=temp[index_end+2:]
        except:
            result.extend(temp.split())
            break

    return result

#리스트내 원소가 어떤 token값을 가지는지 출력해줌
def detect_token(string):
    first_char=string[0]
    if first_char=='"':
        return 'string'
    elif first_char=='(':
        return 'literal_list'
    elif first_char.isalpha():
        return 'ident'
    else:
        return 'literal'

def function_car(var_dict,tree_root):
    literal_list=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,literal_list)!="literal_list"):
        print("CAR Type Error")
        raise NotImplementedError
    list_py = literal_list_to_list(literal_list[1])
    if(len(list_py)==0):return ("false", "nil")
    first_element=list_py[0]
    token=detect_token(first_element)
    return (token, first_element)
 # (car '()) << should fix error

#########################################car method###################################################


#########################################cdr method###################################################
def function_cdr(var_dict,tree_root):

    literal_list=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,literal_list)!="literal_list"):
        print("CDR Type Error")
        raise NotImplementedError
    list_py = literal_list_to_list(literal_list[1])
    new_literal_list_py=list_py[1:]
    new_literal_list='('+" ".join(new_literal_list_py)+')'
    return ('literal_list',new_literal_list )

#########################################cdr method###################################################

#########################################nth method###################################################
def function_nth(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,result1)!="literal"):
        print("NTH Type Error : First argument should be Natural Number")
        raise NotImplementedError

    number=float_or_int(result1[1])
    #print(number)
    if(type(number)!=int or number<0):
        print("NTH Type Error : First argument should be Natural Number")
        raise NotImplementedError

    result2=eval(var_dict,tree_root.children[1],True) #애매
    if(type_check(var_dict,result2)!="literal_list"):
        print("NTH Type Error : Second argument should be List")
        raise NotImplementedError

    list_py = literal_list_to_list(result2[1])
    #print(len(list_py))

    if(len(list_py)-1<number):return ("false","nil")
    else:return (detect_token(list_py[number]),list_py[number])

#########################################nth method###################################################


#########################################cons method#################################################
def function_cons(var_dict,tree_root):
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    token = type_check(var_dict,right_result)
    if token!='literal_list':
        print("right parameter of function cons is not literal_list")
        raise NotImplementedError

    py_new_list = literal_list_to_list(right_result[1])
    py_new_list.insert(0,left_result[1])
    new_literal_list='('+" ".join(py_new_list)+')'
    return ('literal_list',new_literal_list)
#########################################cons method#################################################


#########################################reverse method#################################################
def function_reverse(var_dict,tree_root):
    result=eval(var_dict,tree_root.children[0],True)
    token = type_check(var_dict,result)

    if token!='literal_list':
        print("parameter of function reverse is not literal_list")
        raise NotImplementedError

    py_new_list = literal_list_to_list(result[1])
    py_new_list=py_new_list[::-1]
    new_literal_list='('+" ".join(py_new_list)+')'
    return ('literal_list',new_literal_list)
#########################################reverse method#################################################


#########################################append method#################################################
def function_append(var_dict,tree_root):
    list_element=list()
    for child in tree_root.children:
        result=eval(var_dict,child,True)
        token = type_check(var_dict,result)
        if token!='literal_list':
            print("parameter of function append is not literal_list")
            raise NotImplementedError
        else:
            list_element.extend(literal_list_to_list(result[1]))

    new_literal_list='('+" ".join(list_element)+')'
    return ('literal_list',new_literal_list)
#########################################append method#################################################


#########################################member method#################################################
def function_member(var_dict,tree_root):
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    token = type_check(var_dict,right_result)
    if token!='literal_list':
        print("right parameter of function member is not literal_list")
        raise NotImplementedError
    target_element=left_result[1]
    py_new_list = literal_list_to_list(right_result[1])
    #print(py_new_list)
    try:
        index=py_new_list.index(target_element)
        py_new_list=py_new_list[index:]
        new_literal_list='('+" ".join(py_new_list)+')'
        return ('literal_list',new_literal_list)
    except:
        return ('false','nil')
#########################################member method#################################################


#########################################remove method#################################################
def function_remove(var_dict,tree_root):
    result=list()
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    token = type_check(var_dict,right_result)
    if token!='literal_list':
        print("right parameter of function member is not literal_list")
        raise NotImplementedError
    target_element=left_result[1]
    py_new_list = literal_list_to_list(right_result[1])

    for i in py_new_list:
        if i!=target_element:
            result.append(i)

    new_literal_list='('+" ".join(result)+')'
    return ('literal_list',new_literal_list)
#########################################remove method#################################################

#########################################length method###################################################
def function_length(var_dict,tree_root):


    result=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,result)!="literal_list"):
        print("LENGTH Type Error : argument should be List")
        raise NotImplementedError

    list_py = literal_list_to_list(result[1])

    out=str(len(list_py))


    return ("literal",out)

#########################################length method###################################################

#########################################ASSOC method###################################################
def function_assoc(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)

    result2=eval(var_dict,tree_root.children[1],True)
    if(type_check(var_dict,result2)!="literal_list"):
        print("ASSOC Type Error : Second argument should be List")
        raise NotImplementedError

    list_py = literal_list_to_list(result2[1])

    #print(list_py)
    for i in list_py:
        if(detect_token(i)!="literal_list"):
            print("ASSOC Type Error : List's argument should be List")
            raise NotImplementedError

    for i in list_py:
        temp=literal_list_to_list(i)
        if(result1==(detect_token(temp[0]),temp[0])):
            save=i
            check=True
            break

    if(check):return ("literal_list",save)
    else:return ("false","nil")

#########################################ASSOC method###################################################

#########################################SUBST method###################################################
def function_subst(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)

    result2=eval(var_dict,tree_root.children[1],True)

    result3=eval(var_dict,tree_root.children[2],True)
    if(type_check(var_dict,result3)!="literal_list"):
        print("SUBST Type Error : Third argument should be List")
        raise NotImplementedError

    list_py = literal_list_to_list(result3[1])

    str="("
    if(result2==(detect_token(list_py[0]),list_py[0])):
        str=str+result1[1]
    else:
        str=str+list_py[0]

    for i in list_py[1:]:
        if(result2==(detect_token(i),i)):
            str=str+" "+result1[1]
        else:
            str=str+" "+i
    str=str+")"
    #print(str)

    return ("literal_list",str)

#########################################ASSOC method###################################################



#########################################atom method###################################################
# literal, string, variable
# ident ( ident , literal, string, variable )

def func_atom (var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]
 
    if(typeValue == 'variable' or typeValue == 'literal' or typeValue == 'string'):
        return ("true", "true")

    elif(typeValue == 'ident'):
        value = var_dict.get(tree_root.children[0].data[1])
        if value is not None:
            print(value)
            if(value[0] == 'variable' or value[0] == 'literal' or value[0] == 'string'):
                return ("true", "true")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            return ("error", "error")
    else:
        return ("false", "nil")



#########################################null method###################################################
def  func_null (var_dict, tree_root):
    value = var_dict.get(tree_root.children[0].data[1])
    if value is not None:
        if(value[1] == 'nil'):
            return ("true", "true")
        else:
            return ("false", "nil")
    else:
        print("Variable doesn't have value")
        return ("error", "error")

#########################################numberp method###################################################
def func_numberp(var_dict, tree_root):
    value = tree_root.children[0].data[0]

    if(value == 'literal'):
        return ("true", "true")
    else:
        value = var_dict.get(tree_root.children[0].data[1])
        if value is not None:
            if(value[0] == 'literal'):
                return ("true", "true")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            return ("error", "error")

#########################################zerop method###################################################
def func_zerop(var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]

    if(typeValue == 'literal'):
        value = tree_root.children[0].data[1]
        if(value == '0'):
            return ("true", "true")
        else:
            return ("false", "nil")

    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            if (identVal[0] == 'literal'):
                if(identVal[1] =='0'):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
        else:
            return ("false", "nil")

#########################################minusp method###################################################
def func_minusp(var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]

    if(typeValue == 'literal'):
        value = int(tree_root.children[0].data[1])
        if(value < 0):
            return ("true", "true")
        else:
            return ("false", "nil")

    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            if (identVal[0] == 'literal'):
                if(int(identVal[1]) < 0):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
        else:
            return ("false", "nil")
    else:
        return ("false", "nil")


#########################################equal method###################################################
def func_eqaul(var_dict, tree_root):
    firType = tree_root.children[0].data[0]
    secType = tree_root.children[1].data[0]

    firVal = tree_root.children[0].data[1]
    secVal = tree_root.children[1].data[1]

    # literal str to int
    if(firType == 'literal'):
        firVal = int(firVal)

    if(secType == 'literal'):
        secVal = int(secVal)

    # ident 인 경우 null 체크
    if(firType == 'ident'):
        if (var_dict.get(firVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(secVal)
            if(identChk[0] == 'literal'):
                secVal = int(identChk[1])
            else:
                secVal = identChk[1]

    # 비교할 값의 타입들이 같은지 체크
    if( type(firVal) == type(secVal)):
        # 같은 타입 or 둘 다 ident
        if(firType == secType):
            if(firVal == secVal):
                return ("true", "true")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal == secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal == secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
    else:
        print("Function == not supported between different type")


#########################################less_than method###################################################
def func_less_than(var_dict, tree_root):
    firType = tree_root.children[0].data[0]
    secType = tree_root.children[1].data[0]

    firVal = tree_root.children[0].data[1]
    secVal = tree_root.children[1].data[1]

    # literal str to int
    if(firType == 'literal'):
        firVal = int(firVal)

    if(secType == 'literal'):
        secVal = int(secVal)

    # ident 인 경우 null 체크
    if(firType == 'ident'):
        if (var_dict.get(firVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(secVal)
            if(identChk[0] == 'literal'):
                secVal = int(identChk[1])
            else:
                secVal = identChk[1]

    # 비교할 값의 타입들이 같은지 체크
    if( type(firVal) == type(secVal)):
        # 같은 타입 or 둘 다 ident
        if(firType == secType):
            if(firVal < secVal):
                return ("true", "true")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal < secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal < secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
    else:
        print("Function < not supported between different type")

#########################################greater method###################################################
def func_greater_than(var_dict, tree_root):
    firType = tree_root.children[0].data[0]
    secType = tree_root.children[1].data[0]

    firVal = tree_root.children[0].data[1]
    secVal = tree_root.children[1].data[1]

    # literal str to int
    if(firType == 'literal'):
        firVal = int(firVal)

    if(secType == 'literal'):
        secVal = int(secVal)

    # ident 인 경우 null 체크
    if(firType == 'ident'):
        if (var_dict.get(firVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(secVal)
            if(identChk[0] == 'literal'):
                secVal = int(identChk[1])
            else:
                secVal = identChk[1]

    # 비교할 값의 타입들이 같은지 체크
    if( type(firVal) == type(secVal)):
        # 같은 타입 or 둘 다 ident
        if(firType == secType):
            if(firVal > secVal):
                return ("true", "true")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal > secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal > secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
    else:
        print("Function > not supported between different type")



#########################################greater_equal method###################################################
def func_greater_equal(var_dict, tree_root):
    firType = tree_root.children[0].data[0]
    secType = tree_root.children[1].data[0]

    firVal = tree_root.children[0].data[1]
    secVal = tree_root.children[1].data[1]

    # literal str to int
    if(firType == 'literal'):
        firVal = int(firVal)

    if(secType == 'literal'):
        secVal = int(secVal)

    # ident 인 경우 null 체크
    if(firType == 'ident'):
        if (var_dict.get(firVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(secVal)
            if(identChk[0] == 'literal'):
                secVal = int(identChk[1])
            else:
                secVal = identChk[1]

    # 비교할 값의 타입들이 같은지 체크
    if( type(firVal) == type(secVal)):
        # 같은 타입 or 둘 다 ident
        if(firType == secType):
            if(firVal >= secVal):
                return ("true", "true")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal >= secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal >= secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
    else:
        print("Function >= not supported between different type")

#########################################less_equal method###################################################
def func_less_equal(var_dict, tree_root):
    firType = tree_root.children[0].data[0]
    secType = tree_root.children[1].data[0]

    firVal = tree_root.children[0].data[1]
    secVal = tree_root.children[1].data[1]

    # literal str to int
    if(firType == 'literal'):
        firVal = int(firVal)

    if(secType == 'literal'):
        secVal = int(secVal)

    # ident 인 경우 null 체크
    if(firType == 'ident'):
        if (var_dict.get(firVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            return ("error", "error")
        else:
            identChk = var_dict.get(secVal)
            if(identChk[0] == 'literal'):
                secVal = int(identChk[1])
            else:
                secVal = identChk[1]

    # 비교할 값의 타입들이 같은지 체크
    if( type(firVal) == type(secVal)):
        # 같은 타입 or 둘 다 ident
        if(firType == secType):
            if(firVal <= secVal):
                return ("true", "true")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal <= secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal <= secVal):
                    return ("true", "true")
                else:
                    return ("false", "nil")
            else:
                return ("false", "nil")
    else:
        print("Function <= not supported between different type")

#########################################strigp method###################################################
def func_stringp(var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]
    value = tree_root.children[0].data[1]
    if(typeValue =='string'):
        return ("true", "true")
    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            print(identVal)
            if(identVal[0] == 'string'):
                return ("true", "true")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            return ("error", "error")
    else:
        return ("false", "nil")

#########################################COND method###################################################
def function_cond(var_dict,tree_root):

    if len(tree_root.children)%2!=0:
        return "Error : COND parameter number should be even"
    check=False
    for index, child in enumerate(tree_root.children):
        if (index%2)==0:
            result1=eval(var_dict,child,True)
            if(type_check(var_dict,result1)!="false"):
                check=True
        elif (index%2)!=0:
            result2=eval(var_dict,child,True)
            if(check):
                return result2

    return ("false","nil")

#########################################COND method###################################################

#########################################IF method###################################################
def function_if(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)

    if(type_check(var_dict,result1)=="false"):
        if(len(tree_root.children)==3):
            result3=eval(var_dict,tree_root.children[2],True)
            return result3
        else:
            return ("false","nil")

    else:
        result2=eval(var_dict,tree_root.children[1],True)
        return result2

#########################################IF method###################################################


########################################print method###################################################
def function_print(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)

    return result1

#########################################PRINT method###################################################



def post_eval(tree_root, result):
    print(result[1])
    return None



#인터프리터 반환값 출력용
def sementic_analysis(var_dict, tree_root):
    result = eval(var_dict, tree_root, ident_calc=False)
    post_eval(tree_root, result)
    return None
