import parse


    #eval function get value by parse_tree from parser.
    #this function will traverse parse_tree by child to root order and sequentially get value.


def eval(var_dict,tree_root,ident_calc=False):

    if(type(tree_root)!=parse.TreeNode):return "Error"
    print(tree_root.postorder())
    #print(tree_root.depth())

    if tree_root.data[0] =='literal':
        result=function_literal(tree_root)
        return result

    elif tree_root.data[0] =='string':
        result=function_literal(tree_root)
        return result

    elif tree_root.data[0] =='literal_list':
        result=function_literal(tree_root)
        return result

    elif tree_root.data[0]=='ident':
        result=function_ident(var_dict,tree_root,ident_calc)
        return result
# 정상적으로 작동하나 수정사항 있음(반환값 아직 없음)
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

    """
    elif(tree_root.data[1]==다른함수):
        다른 함수에 대한 eval 함#tn
    """
################################# literal method###################################
def function_literal(tree_root):
    return tree_root.data
################################# literal method###################################


################################# literal_list method###################################
def function_literal_list(tree_root):
    return tree_root.data
################################# literal_list method###################################


################################# string method###################################
def function_string(tree_root):
    return tree_root.data
################################# string method###################################


################################# ident method###################################
def function_ident(var_dict,tree_root,ident_calc):
    if ident_calc==False:
        return tree_root.data
    if ident_calc==True:
        return var_dict[tree_root.data[1]]
################################# ident method###################################


################################# calculus method###################################
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
    result=float_or_int(eval(var_dict,tree_root.children[0])[1])
    if tree_root.data[0]=='+':
        for i in tree_root.children[1:]:
            result = result + float_or_int(eval(var_dict,i)[1])
    if tree_root.data[0]=='-':
        for i in tree_root.children[1:]:
            result = result - float_or_int(eval(var_dict,i)[1])
    if tree_root.data[0]=='*':
        for i in tree_root.children[1:]:
            result = result * float_or_int(eval(var_dict,i)[1])
    if tree_root.data[0]=='/':
        for i in tree_root.children[1:]:
            result = result / float_or_int(eval(var_dict,i)[1])

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
            result=eval(var_dict,child)[1]
            """
            if is_literal_list(child):
                result="'"+eval(var_dict,child)[1]
            else:
                result=eval(var_dict,child)[1]
            """
        else:
            result = result + " "+eval(var_dict,child)[1]
            """
            if is_literal_list(child):
                result=  result + " "+"'"+eval(var_dict,child)[1]
            else:
                result = result + " "+eval(var_dict,child)[1]
            """
    return ('literal_list','('+result+')')
#########################################list method###################################################


#########################################setq method###################################################
def function_setq(var_dict,tree_root):
    if len(tree_root.children)%2!=0:
        return "Error : setq parameter number is odd"
    for index, child in enumerate(tree_root.children):
        if (index%2)==0:
            variable=eval(var_dict,child,False)
        elif (index%2)!=0:
            value=eval(var_dict,child,True)
            var_dict[variable[1]]=value

#########################################setq method###################################################


#########################################car method###################################################
def literal_list_to_list(string_literal_list):
    result=list()
    temp=string_literal_list[1:-1]
    while(1):
        try:
            index_start=temp.index('(')
            if index_start!=0:
                result.extend(temp[:index_start-1].split(' '))

            index_end=temp.index(')')

            while(1):
                if temp[index_end+1]==')':
                    index_end = index_end+1
                else:
                    break

            temp_literal_list=temp[index_start:index_end+1]
            result.append(temp_literal_list)
            temp=temp[index_end+2:]
        except:
            result.extend(temp.split(' '))
            break

    return result

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
    list_py = literal_list_to_list(literal_list[1])
    first_element=list_py[0]
    token=detect_token(first_element)
    return (token, first_element)

#########################################car method###################################################


def function_cdr(var_dict,tree_root):
    literal_list=eval(var_dict,tree_root.children[0],True)
    list_py = literal_list_to_list(literal_list[1])
    new_literal_list_py=list_py[1:]
    new_literal_list='('+" ".join(new_literal_list_py)+')'
    return ('literal_list',new_literal_list )
