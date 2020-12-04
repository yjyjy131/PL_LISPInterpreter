import parse


    #eval function get value by parse_tree from parser.
    #this function will traverse parse_tree by child to root order and sequentially get value.



#eval이 반환한 튜플값에서 lexeme을 읽어서 출력해준다.
def post_eval(tree_root, result):
    print(result[1])
    return None



#인터프리터 반환값 출력용
# main함수에서 사용하기 위함. eval을 통해서 파싱트리의 값을 계산하여 튜플형태로 반환. 이 튜플형태로부터 post_eval이 실제 반환값(lexeme)을 print해준다.
def sementic_analysis(var_dict, tree_root):
    result = eval(var_dict, tree_root, ident_calc=False)
    post_eval(tree_root, result)
    return None


def eval(var_dict,tree_root,ident_calc=False):

    if(type(tree_root)!=parse.TreeNode):raise NotImplementedError
#들어온 파스트리에서 루트 노드에 있는 토큰(함수)가 뭔지 확인 후에 이에 맞게 처리해주는 함수를 불러줌
#각 처리해주는 함수들의 반환값은 모두 튜플이다. 5를 반환하는게 아니라 ('literal','5') 처럼 (토큰,lexeme)형태로 반환함 => 재귀적으로 호출하여 처리하기 위함
# 이 값을 이후 post_eval이라는 함수에서 불러 실제로 인터프리터에서 출력해야되는 값을 eval이 반환한 튜플에서 빼내서 출력해준다(lexeme값)

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


    elif tree_root.data[0] in ['/','*','+','-']:
        result = function_calculus(var_dict,tree_root)
        return result

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

#################################TypeCheck method###################################
def type_check(var_dict,target):
# 들어온 인자가 어떤 token값을 가지는지 알려줌(변수가 온 경우 저장된 값의 token을 알려줌)
    if(target[0]=="ident"):
        if(target[1] in var_dict):
            return var_dict[target[1]][0]
        else:
            print("Value Error : unbounded value "+"'"+target[1]+"'")
            raise NotImplementedError
    else: return target[0]



################################# literal method###################################
def function_literal(var_dict,tree_root):
    return tree_root.data #파스트리에 숫자만 들어온 경우 해당 값을 반환해줌



################################# literal_list method###################################
def function_literal_list(var_dict,tree_root):
    return tree_root.data #파스트리에 리스트만 들어온 경우 해당 값을 반환해줌



################################# string method###################################
def function_string(var_dict,tree_root):
    return tree_root.data #파스트리에 string만 들어온 경우 해당 값을 반환해줌


################################# true method###################################
def function_true(var_dict,tree_root):
    return tree_root.data #파스트리에 T만 들어온 경우 해당 값을 반환해줌



################################# false method###################################
def function_false(var_dict,tree_root):
    return tree_root.data #파스트리에 false만 들어온 경우 해당 값을 반환해줌




################################# ident method###################################
def function_ident(var_dict,tree_root,ident_calc):
    if ident_calc==False:
        return tree_root.data
    if ident_calc==True:
        if(tree_root.data[0]=="ident"):
            if(tree_root.data[1] in var_dict):
                return var_dict[tree_root.data[1]]
            else:
                print("Value Error : unbounded value "+"'"+tree_root.data[1]+"'")
                raise NotImplementedError
#파스트리에 변수만 들어온 경우 이미 저장된 값인지 확인하고 해당 값을 반환해줌


################################# variable method###################################
def function_variable(var_dict,tree_root):
    return ('variable',tree_root.data[1])
#파스트리에 'x형태가 들어온 경우 해당 값을 반환해준다.


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

#사칙연산 처리 함수
def function_calculus(var_dict,tree_root):
    result=eval(var_dict,tree_root.children[0],True)
    #첫번째 인자의 값을 계산하고 그 값이 literal인지 확인
    if(type_check(var_dict,result)!="literal"):
        print(tree_root.data[1]+"Type Error : argument should be literal")
        raise NotImplementedError
    result=float_or_int(result[1])

    # 들어온 인자만큼 각 인자별로 literal인지 확인해주고 첫번째 인자에 계속 연산(+/*-)해줌
    if tree_root.data[0]=='+':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("+ Type Error : argument should be literal")
                raise NotImplementedError
            result = result + float_or_int(check[1])
    if tree_root.data[0]=='-':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("- Type Error : argument should be literal")
                raise NotImplementedError
            result = result - float_or_int(check[1])
    if tree_root.data[0]=='*':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("* Type Error : argument should be literal")
                raise NotImplementedError
            result = result * float_or_int(check[1])
    if tree_root.data[0]=='/':
        for i in tree_root.children[1:]:
            check=eval(var_dict,i,True)
            if(type_check(var_dict,check)!="literal"):
                print("/ Type Error : argument should be literal")
                raise NotImplementedError
            result = result / float_or_int(check[1])

    return ('literal',str(result))



#########################################list method###################################################
#들어온 토큰이 list인지 확인해줌
def is_literal_list(treenode):
    if treenode.data[0]=='literal_list':
        return True
    else:
        return False

#list연산 처리 함수
def function_list(var_dict,tree_root):
    result = str()
    #들어온 인자들을 다 리스트에 추가해줌
    #내부에서 리스트는 문자열 형태로 저장됨
    for index, child in enumerate(tree_root.children):
        if index==0:
            result=eval(var_dict,child,True)[1]

        else:
            result = result + " "+eval(var_dict,child,True)[1]

    return ('literal_list','('+result+')')



#########################################setq method###################################################
#setq 처리 함수
def function_setq(var_dict,tree_root):
    return_list=list()
    #setq는 인자가 무조건 짝수개
    if len(tree_root.children)%2!=0:
        return "Error : setq parameter number is odd"
    for index, child in enumerate(tree_root.children):
        if (index%2)==0:
            variable=eval(var_dict,child,False)
            #setq는 홀수번째 인자가 반드시 변수(ident)여야 함
            if variable[0]!='ident':
                print("setq function even variable is not ident")
                raise NotImplementedError

        elif (index%2)!=0:
            value=eval(var_dict,child,True)
            var_dict[variable[1]]=value
            return_list.append(value)
    return return_list[len(return_list)-1]




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

#문자열로 저장된 리스트에서, 리스트 내 원소가 어떤 token값을 가지는지 출력해줌
# 내부적으로 리스트는 문자열 형태로 저장됨
def detect_token(string):
    first_char=string[0]
    if first_char=='"':
        return 'string'
    elif first_char=='(':
        return 'literal_list'
    elif first_char.isalpha():
        return 'variable'
    else:
        return 'literal'

# CAR 처리 함수
def function_car(var_dict,tree_root):
    literal_list=eval(var_dict,tree_root.children[0],True)
    #CAR의 인자값에 대한 계산을 해준 후, 이 결과가 list인지 확인해줌
    if(type_check(var_dict,literal_list)!="literal_list"):
        print("CAR Type Error : argument should be list")
        raise NotImplementedError
    list_py = literal_list_to_list(literal_list[1])
    if(len(list_py)==0):return ("false", "nil")
    first_element=list_py[0]
    token=detect_token(first_element)
    return (token, first_element)




#########################################cdr method###################################################
# CDR 처리 함수
def function_cdr(var_dict,tree_root):

    literal_list=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,literal_list)!="literal_list"):
        print("CDR Type Error : argument should be list")
        raise NotImplementedError
    #CAR의 인자값에 대한 계산을 해준 후, 이 결과가 list인지 확인해줌
    # 인자로 받은 list를 파이썬 list로 만들어 연산을 해준 후,
    # 이 새로운 list를 다시 문자열 형태로 변환해준후 이 값을 반환
    list_py = literal_list_to_list(literal_list[1])
    new_literal_list_py=list_py[1:]
    new_literal_list='('+" ".join(new_literal_list_py)+')'
    return ('literal_list',new_literal_list )



#########################################nth method###################################################
#NTH 처리 함수

def function_nth(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,result1)!="literal"):
        print("NTH Type Error : First argument should be Zero or Natural Number")
        raise NotImplementedError

    number=float_or_int(result1[1])
    #첫번째 인자에 대한 계산후 이 값이 숫자인지 확인해준다.
    if(type(number)!=int or number<0):
        print("NTH Type Error : First argument should be Zero or Natural Number")
        raise NotImplementedError
    #첫번째 인자에 대한 계산후 이 값이 0이거나 자연수인지 확인해준다.
    result2=eval(var_dict,tree_root.children[1],True)
    if(type_check(var_dict,result2)!="literal_list"):
        print("NTH Type Error : Second argument should be List")
        raise NotImplementedError
    #두번째 인자에 대한 계산후 이 값이 list인지 확인해준다.
    #list값(string 형태)를 python list로 만들어준후 length를 확인후 해당 순서의 값을 빼내준다.
    list_py = literal_list_to_list(result2[1])


    if(len(list_py)-1<number):return ("false","nil")
    else:return (detect_token(list_py[number]),list_py[number])




#########################################cons method################################################
#cons 처리 함수
def function_cons(var_dict,tree_root):
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    token = type_check(var_dict,right_result)
    #두번째 인자가 list인지 확인해준다.

    if token!='literal_list':
        print("CONS TYPE Error : second argument should be list")
        raise NotImplementedError
    #list값(string 형태)를 python list로 만들어준후 length를 확인후 첫번쨰 인자를 추가해준다.
    py_new_list = literal_list_to_list(right_result[1])
    py_new_list.insert(0,left_result[1])
    # 이 새로운 list를 다시 문자열 형태로 변환해준후 이 값을 반환
    new_literal_list='('+" ".join(py_new_list)+')'
    return ('literal_list',new_literal_list)



#########################################reverse method################################################
#reverse처리 함수
def function_reverse(var_dict,tree_root):
    result=eval(var_dict,tree_root.children[0],True)
    token = type_check(var_dict,result)
    #첫번째 인자가 list인지 확인해준다.
    if token!='literal_list':
        print("REVERSE Type Error : argument should be list")
        raise NotImplementedError
    #list값(string 형태)를 python list로 만들어준후 순서를 뒤집어 새로운 list를 만든다
    py_new_list = literal_list_to_list(result[1])
    py_new_list=py_new_list[::-1]
    # 이 새로운 list를 다시 문자열 형태로 변환해준후 이 값을 반환
    new_literal_list='('+" ".join(py_new_list)+')'
    return ('literal_list',new_literal_list)



#########################################append method################################################
#append 처리 함수
def function_append(var_dict,tree_root):
    list_element=list()
    #각 인자가 list인지 확인해준다. list가 맞다면 이를 python list형태로 변환하여 종합하는 python list인 list_element에 추가해준다
    for child in tree_root.children:
        result=eval(var_dict,child,True)
        token = type_check(var_dict,result)
        if token!='literal_list':
            print("APPEND Type Error : all argument should be list")
            raise NotImplementedError
        else:
            list_element.extend(literal_list_to_list(result[1]))
    # list_element를 다시 문자열 형태로 변환해준후 이 값을 반환
    new_literal_list='('+" ".join(list_element)+')'
    return ('literal_list',new_literal_list)



#########################################member method################################################
#member 처리 함수
def function_member(var_dict,tree_root):
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    #두번째 인자가 list인지 확인해준다.
    token = type_check(var_dict,right_result)
    if token!='literal_list':
        print("MEMBER Type Error : second argument should be list")
        raise NotImplementedError
    target_element=left_result[1]
    py_new_list = literal_list_to_list(right_result[1])
    #list값(string 형태)를 python list로 만들어준후 찾는 인자가 있는지 확인후 있으면 그 인자부터의 리스트를 다시 문자열로 변환하여 반환해준다.
    try:
        index=py_new_list.index(target_element)
        py_new_list=py_new_list[index:]
        new_literal_list='('+" ".join(py_new_list)+')'
        return ('literal_list',new_literal_list)
    except:
        return ('false','nil')



#########################################remove method################################################
#remove처리함수
def function_remove(var_dict,tree_root):
    result=list()
    left_result=eval(var_dict,tree_root.children[0],True)
    right_result=eval(var_dict,tree_root.children[1],True)
    #두번째 인자가 list인지 확인해준다.
    token = type_check(var_dict,right_result)
    if token!='literal_list':
        print("REMOVE Type Error : second argument should be list")
        raise NotImplementedError
    target_element=left_result[1]
    py_new_list = literal_list_to_list(right_result[1])
    #list값(string 형태)를 python list로 만들어준후 target_element가 있는지 확인하여 이 인자가 없는 새로운 리스트를 만든 후,다시 문자열로 변환하여 반환해준다.
    for i in py_new_list:
        if i!=target_element:
            result.append(i)

    new_literal_list='('+" ".join(result)+')'
    return ('literal_list',new_literal_list)


#########################################length method##################################################
#length처리함수
def function_length(var_dict,tree_root):

    #들어온 인자가 list인지 확인해준다.
    result=eval(var_dict,tree_root.children[0],True)
    if(type_check(var_dict,result)!="literal_list"):
        print("LENGTH Type Error : argument should be List")
        raise NotImplementedError
    #list값(string 형태)를 python list로 만들어준후 이 리스트의 길이를 구한 뒤 길이값을 반환해준다.
    list_py = literal_list_to_list(result[1])

    out=str(len(list_py))


    return ("literal",out)



#########################################ASSOC method##################################################
#assoc처리함수
def function_assoc(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)
    #두번째 인자가 list인지 확인해준다.
    result2=eval(var_dict,tree_root.children[1],True)
    if(type_check(var_dict,result2)!="literal_list"):
        print("ASSOC Type Error : Second argument should be List")
        raise NotImplementedError

    list_py = literal_list_to_list(result2[1])

    #list값(string 형태)를 python list로 만들어준후 내부인자가 모두 list인지 확인해준다.
    for i in list_py:
        if(detect_token(i)!="literal_list"):
            print("ASSOC Type Error : List's argument should be List")
            raise NotImplementedError
    #찾는 list가 있는지 첫번쨰 인자를 통해 검사한다. 있으면 그 인자를 save변수에 저장하고,이를 나중에 반환한다.
    check=False
    for i in list_py:
        temp=literal_list_to_list(i)
        if(result1==(detect_token(temp[0]),temp[0])):
            save=i
            check=True
            break

    if(check):return ("literal_list",save)
    else:return ("false","nil")



#########################################SUBST method##################################################
#subst 처리 함수
def function_subst(var_dict,tree_root):

    result1=eval(var_dict,tree_root.children[0],True)

    result2=eval(var_dict,tree_root.children[1],True)
    #세번째 인자가 list인지 확인해준다.
    result3=eval(var_dict,tree_root.children[2],True)
    if(type_check(var_dict,result3)!="literal_list"):
        print("SUBST Type Error : Third argument should be List")
        raise NotImplementedError
    #list값(string 형태)를 python list로 만들어준후 두번쨰 인자가 있으면 첫번째 인자로 바꿔서 새로 저장해준다.
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




#########################################atom method###################################################
# literal, string, variable
# ident ( ident , literal, string, variable )

def func_atom (var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]

    if(typeValue == 'variable' or typeValue == 'literal' or typeValue == 'string'):
        return ("true", "t")

    elif(typeValue == 'ident'):
        value = var_dict.get(tree_root.children[0].data[1])
        if value is not None:
            #print(value)
            if(value[0] == 'variable' or value[0] == 'literal' or value[0] == 'string'):
                return ("true", "t")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
    else:
        return ("false", "nil")



#########################################null method###################################################
def  func_null (var_dict, tree_root):
    value = var_dict.get(tree_root.children[0].data[1])
    if value is not None:
        if(value[1] == 'nil'):
            return ("true", "t")
        else:
            return ("false", "nil")
    else:
        print("Variable doesn't have value")
        raise NotImplementedError #return ("error", "error")

#########################################numberp method###################################################
def func_numberp(var_dict, tree_root):
    value = tree_root.children[0].data[0]

    if(value == 'literal'):
        return ("true", "t")
    else:
        value = var_dict.get(tree_root.children[0].data[1])
        if value is not None:
            if(value[0] == 'literal'):
                return ("true", "t")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")

#########################################zerop method###################################################
def func_zerop(var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]
    #print(typeValue)
    if(typeValue == 'literal'):
        value = tree_root.children[0].data[1]
        #print(value)
        if(value == '0'):
            return ("true", "t")
        else:
            return ("false", "nil")

    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            if (identVal[0] == 'literal'):
                if(identVal[1] =='0'):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            else:
                print("Zerop : Error(not number)")
                raise NotImplementedError #return ("error", "error")
        else:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")

    else:
        print("Zerop : Error(not number)")
        raise NotImplementedError #return ("error", "error")
#########################################minusp method###################################################
def func_minusp(var_dict, tree_root):
    typeValue = tree_root.children[0].data[0]

    if(typeValue == 'literal'):
        value = int(tree_root.children[0].data[1])
        if(value < 0):
            return ("true", "t")
        else:
            return ("false", "nil")

    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            if (identVal[0] == 'literal'):
                if(int(identVal[1]) < 0):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            else:
                print("Minusp : Error(not number)")
                raise NotImplementedError #return ("error", "error")
        else:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
    else:
        print("Minusp : Error(not number)")
        raise NotImplementedError #return ("error", "error")


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
            raise NotImplementedError #return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
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
                return ("true", "t")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal == secVal):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal == secVal):
                    return ("true", "t")
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
            raise NotImplementedError #return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
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
                return ("true", "t")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal < secVal):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal < secVal):
                    return ("true", "t")
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
            raise NotImplementedError #return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
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
                return ("true", "t")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal > secVal):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal > secVal):
                    return ("true", "t")
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
            raise NotImplementedError #return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
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
                return ("true", "t")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal >= secVal):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal >= secVal):
                    return ("true", "t")
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
            raise NotImplementedError #return ("error", "error")
        else:
            identChk = var_dict.get(firVal)
            if(identChk[0] == 'literal'):
                firVal = int(identChk[1])
            else:
                firVal = identChk[1]

    if(secType == 'ident'):
        if(var_dict.get(secVal)) is None:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
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
                return ("true", "t")
            else:
                return ("false", "nil")

        # 하나만 ident
        elif(firType != secType):
            if(firType == 'ident'):
                if(firVal <= secVal):
                    return ("true", "t")
                else:
                    return ("false", "nil")
            elif(secType == 'ident'):
                if(firVal <= secVal):
                    return ("true", "t")
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
        return ("true", "t")
    elif(typeValue == 'ident'):
        identVal = var_dict.get(tree_root.children[0].data[1])
        if identVal is not None:
            #print(identVal)
            if(identVal[0] == 'string'):
                return ("true", "t")
            else:
                return ("false", "nil")
        else:
            print("Variable doesn't have value")
            raise NotImplementedError #return ("error", "error")
    else:
        return ("false", "nil")

#########################################COND method###################################################
def function_cond(var_dict,tree_root):
#cond는 조건문 수행문 쌍으로 들어오므로 인자가 반드시 짝수
#각 조건문이 false가 아니면 바로 수행문을 실행시키고 나간다. 모든 조건문이 false면 nil을 반환한다.
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



#########################################IF method###################################################
def function_if(var_dict,tree_root):
#첫번째 인자값이 false면 세번째 인자나 nil을 반환해주고 아니면 두번쨰 인자를 반환해준다.
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




########################################print method###################################################
def function_print(var_dict,tree_root):
# 인자값을 계산한후 해당 값을 반환해준다.
    result1=eval(var_dict,tree_root.children[0],True)

    return result1
