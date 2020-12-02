
function=['+','/','*','-',"setq","list","cdr","car","nth","cons","reverse","append","length","member","assoc","remove","subst","atom","null","numberp","zerop","minusp","equal","<",">=","stringp","if","cond","cadr"]



    #parser makes parse_tree(class TreeNode) by token_list(list of tuple) from lexer.
    #parser first check start of parentheses and end of parentheses, and check function beside the first parentheses.
    #if sure, then check by function parser(ex-calc,set_q).
    #each function parser check syntax error and make parse_tree by TreeNode.
    #finally, function parser return parse_tree or error message.


def parser(var_dict,token_list):
    print(token_list)
    if((';',';') in token_list):
        index=token_list.index((';',';'))
        token_list=token_list[:index]
    if(len(token_list)==0):
        print("there is no readable code")
        return
    if(token_list.pop(0)[0]!='('):print("there is not first bracket ");return 'error'
    if(token_list.pop()[0]!=')'): print("there is not end bracket ");return 'error'
    funct=token_list.pop(0)
    func=funct[0]
    parse_tree=TreeNode(funct)
    if(not func in function):
        print("there is no function")
        return

    # parsing arithmetic function
    if(func=='+'or func=='/' or func=='*'or func=='-'):
        result=calc(var_dict,parse_tree,token_list)
        #print(result.postorder())
        return result

    # parsing SETQ function
    elif(func=='setq'):
        result=set_q(parse_tree,token_list)
        #print(result.postorder())
        return result

    # parsing LIST function
    elif(func=='list'):
        result=make_list(parse_tree,token_list)
        return result
    # parsing CAR function
    elif(func=='car'):
        result=car(var_dict,parse_tree,token_list)
        return result
    # parsing CDR function
    elif(func=='cdr'):
        result=cdr(var_dict,parse_tree,token_list)
        return result
    # parsing NTH function
    elif(func=='nth'):
        result=nth(var_dict,parse_tree,token_list)
        return result
    # parsing cons function
    elif(func=='cons'):
        result=cons(var_dict,parse_tree,token_list)
        return result
    # parsing Reverse function
    elif(func=='reverse'):
        result=reverse(var_dict,parse_tree,token_list)
        return result
    # parsing Append function
    elif(func=='append'):
        result=make_append(var_dict,parse_tree,token_list)
        return result
    # parsing length function
    elif(func=='length'):
        result=length(var_dict,parse_tree,token_list)
        return result
    # parsing member function
    elif(func=='member'):
        result=member(var_dict,parse_tree,token_list)
        return result
    # parsing assoc function
    elif(func=='assoc'):
        result=assoc(var_dict,parse_tree,token_list)
        return result
    # parsing remove function
    elif(func=='remove'):
        result=remove(var_dict,parse_tree,token_list)
        return result
    # parsing subst function
    elif(func=='subst'):
        result=subst(var_dict,parse_tree,token_list)
        return result

    elif(func=='cadr'):
        result=cadr(var_dict,parse_tree,token_list,funct[1])
        return result

    # parsing ATOM function  X가 ATOM(심볼)일 때만 참(true)를 반환
    elif(func=='atom'):
        result=atom(var_dict, parse_tree, token_list)
        return result
    #parsing NULL function X가 NIL일 때만 참(true)을 반환
    elif(func=='null'):
        result=null_chk(var_dict, parse_tree, token_list)
        return result
    #parsing NUMBERP function X가 숫자일 때만 참(true)을 반환
    elif(func=='numberp'):
        result=numberp(var_dict, parse_tree, token_list)
        return result
    #parsing ZEROP function X가 0일 때만 참(true)을 반환함. X가 숫자가 아니면 ERROR
    elif(func=='zerop'):
        result=zerop(var_dict, parse_tree, token_list)
        return result
    #parsing MINUSP function X가 음수일 때만 참(true)을 반환함. X가 숫자가 아니면 ERROR
    elif(func=='minusp'):
        result=minusp(var_dict, parse_tree, token_list)
        return result
    #parsing EQUAL function  X와 Y가 같으면 참(true)을 반환
    elif(func=='equal'):
        result=equal_chk(var_dict, parse_tree, token_list)
        return result
    #parsing < function X < Y 이면 참(true)을 반환
    elif(func=='<'):
        result=less_than(var_dict, parse_tree, token_list)
        return result
    #parsing >= function  X >= Y 이면 참(true)을 반환
    elif(func=='>='):
        result=greater_equal(var_dict, parse_tree, token_list)
        return result
    #parsing STRINGP function X가 STRING일 때만 참(true)을 반환
    elif(func=='stringp'):
        result=stringp(var_dict, parse_tree, token_list)
        return result
    """
    elif(func==다른함수):
        다른 함수에 대한 parse 함수
        return 함수 결과
    """




# <arithmetic_stmt> -> ( (+|-|*|/) <expr> {<expr>})
def calc(var_dict,parse_tree,token_list):
    while(len(token_list)>0):
        if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)==0 or len(token_list)!=0):
        print("there is no operand")
        return 'error'

    return parse_tree



# <setq_stmt> -> ( setq <ident> <expr> ... )
def set_q(parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'

    while(len(token_list)>0):
        factor(parse_tree,token_list)
        if(not expr(parse_tree,token_list)):return 'error'

    if(len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (setq <ident> <expr> <ident> <expr> ...)")
        return 'error'

    return parse_tree





# <list_stmt> -> ( list <expr> {<expr>})
def make_list(parse_tree,token_list):
    while(len(token_list)>0):
        if(not expr(parse_tree,token_list)):return 'error'

    if(len(parse_tree.children)==0 or len(token_list)!=0):
        print("there is no list item")
        return 'NIL'

    return parse_tree


# <car_stmt> -> ( car <expr> )
def car(var_dict,parse_tree,token_list):

    if(len(token_list)==0):
        print("CAR:there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'

    if(len(parse_tree.children)!=1 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (car <expr>)")
        return 'error'

    return parse_tree


# <cdr_stmt> -> ( cdr <expr> )
def cdr(var_dict,parse_tree,token_list):

    if(len(token_list)==0):
        print("CDR:there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=1 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (cdr <expr>)")
        return 'error'

    return parse_tree

# <cadr_stmt> -> ( cadr <expr> )
def cadr(var_dict,parse_tree,token_list,func):

    if(len(token_list)==0):
        print("CADR : there is no argument")
        return 'error'


    func=func[1:-1]
    if(func[-1]=="d"):
        parse_tree=TreeNode(("cdr","cdr"))
    elif(func[-1]=="a"):
        parse_tree=TreeNode(("car","car"))
    func=func[:-1]
    if(not expr(parse_tree,token_list)):return 'error'




    while(len(func)!=0):
        if(func[-1]=="d"):
            temp=TreeNode(("cdr","cdr"))
            temp.add([parse_tree])
        elif(func[-1]=="a"):
            temp=TreeNode(("car","car"))
            temp.add([parse_tree])
        func=func[:-1]
        parse_tree=temp

    return parse_tree





# <nth_stmt> -> ( nth <expr> <expr> )
def nth(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("NTH : there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=2 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (nth <expr> <expr>)")
        return 'error'

    return parse_tree


# <cons_stmt> -> ( cons <expr> <expr> ) ;
def cons(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=2 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (setq <variable> <expr>)")
        return 'error'

    return parse_tree


# <reverse_stmt> -> ( reverse <expr>)
def reverse(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'

    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=1 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (reverse <expr>)")
        return 'error'

    return parse_tree


# <append_stmt> -> ( append <expr> {<expr>})
def make_append(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return "NIL"
    if(not expr(parse_tree,token_list)):return 'error'
    while(len(token_list)>0):
        if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)==0 or len(token_list)!=0):
        print("there is no list")
        return 'error'

    return parse_tree


# <length_stmt> -> ( length <expr> ) ;
def length(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=1 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to ( length <expr>)")
        return 'error'

    return parse_tree


# <member_stmt> -> ( member <expr> <expr> )
def member(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=2  or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (member <expr> <expr>)")
        return 'error'

    return parse_tree

# <assoc_stmt> -> ( assoc <expr> <expr> )
def assoc(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=2 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (assoc <expr> <expr>)")
        return 'error'

    return parse_tree

# <remove_stmt> -> ( remove <expr> <expr> )
def remove(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    print(len(parse_tree.children))
    if(len(parse_tree.children)!=2 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (remove <expr> <expr>)")
        return 'error'

    return parse_tree

# <subst_stmt> -> ( subst <expr> <expr> <expr>)
def subst(var_dict,parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(not expr(parse_tree,token_list)):return 'error'
    if(len(parse_tree.children)!=3 or len(token_list)!=0):
        print("cannot match argument")
        print("please match format to (subst <expr> <expr> <expr>)")
        return 'error'

    return parse_tree

# <expr> -> <factor>  | (<stmt>)
# <stmt> -> (<function> <expr> {<expr>})  # 'parser' function work for this
# <function> -> + | - | * | / | setq | list | car | cdr | nth | cons | reverse | append | length | assoc | remove | subst | member | ...

# parsing ATOM function
def atom(var_dict, parse_tree, token_list):
    temp = token_list[0]
    if (temp[0]!='ident'): 
        print("error") 
        return "error"
    else:
        factor(parse_tree, token_list)
        return parse_tree
  
#parsing NULL function 
def null_chk(var_dict, parse_tree, token_list):
    temp = token_list[0]
    if (temp[0]!='ident'): 
        print("error")
        return "error"
    else:
        factor(parse_tree, token_list)
    return parse_tree

#parsing NUMBERP function   
def numberp(var_dict, parse_tree, token_list):
    temp = token_list[0]
    if (temp[0]!='ident' and temp[0]!='literal'): 
        print("error")
        return "error"
    else:
        factor(parse_tree, token_list)
    return parse_tree

#parsing ZEROP function 
def zerop(var_dict, parse_tree, token_list):
    temp = token_list[0]
    if (temp[0]!='ident' and temp[0]!='literal'): 
        print("error")
        return "error"
    else:
        factor(parse_tree, token_list)
    return parse_tree 

#parsing MINUSP function 
def minusp(var_dict, parse_tree, token_list):
    temp = token_list[0]
    if (temp[0]!='ident' and temp[0]!='literal'): 
        print("error")
        return "error"
    else:
        factor(parse_tree, token_list)
    return parse_tree 

#parsing EQUAL function 
def equal_chk(var_dict, parse_tree, token_list):
    if (len(token_list)==2): 
        while(len(token_list)>0):
            if(not expr(parse_tree, token_list)):return 'error'
        return parse_tree
    else:
        print("equal function parameter out of range")
        return "error" 

#parsing < function
def less_than(var_dict, parse_tree, token_list):
    if (len(token_list)==2): 
        while(len(token_list)>0):
            if(not expr(parse_tree, token_list)):return 'error'
        return parse_tree
    else:
        print("less than function parameter out of range")
        return "error" 

#parsing >= function 
def greater_equal(var_dict, parse_tree, token_list):
    if (len(token_list)==2): 
        while(len(token_list)>0):
            if(not expr(parse_tree, token_list)):return 'error'
        return parse_tree
    else:
        print("greater equal function parameter out of range")
        return "error" 

#parsing STRINGP function
def stringp(var_dict, parse_tree, token_list):
    factor(parse_tree, token_list)
    return parse_tree 


def expr(parse_tree,token_list):
    if(len(token_list)==0):
        print("there is no argument")
        return False
    if(token_list[0][0]=='('):
        new_token=[]
        stack=[]
        end=0
        for i in token_list:
            if(i==('(','(')):
                stack.append(i)
                new_token.append(i)
                end=end+1
            elif(i==(')', ')')):
                if(len(stack)==1):
                    end=end+1
                    stack.pop()
                    new_token.append(i)
                    break
                else:
                    end=end+1
                    new_token.append(i)
                    stack.pop()
            else:
                end=end+1
                new_token.append(i)
        del token_list[:end]
        result=parser(parse_tree,new_token)
        if(type(result)!=TreeNode):return False
        else:parse_tree.add([result])
    else:
        factor(parse_tree,token_list)

    return True

# <factor> -> <literal>| <variable> | <string> | <literal_list> | <ident> | <bool>
def factor(parse_tree,token_list):
    parse_tree.add([TreeNode(token_list.pop(0))])


    return True

def is_exist_list(var_dict,parse_tree):
    if(parse_tree.data[0]=='ident'):
        if(parse_tree.data[1] in var_dict):
            if(var_dict[i.data[1]][0]!="literal_list"):#나중에 var_list로 수정
                return False
    elif(parse_tree.data[0]=="variable" or parse_tree.data[0]=="string" or parse_tree.data[0]=="literal"):
        return False
    elif(parse_tree.data[1]=="+" or parse_tree.data[1]=="-" or parse_tree.data[1]=="*" or parse_tree.data[1]=="/"):
        return False
    elif(parse_tree.data[1]=="car" or parse_tree.data[1]=="nth" or parse_tree.data[1]=="length" or parse_tree.data[1]=="remove"):
        return False
    elif(parse_tree.data[1]=="setq"):
        if(not is_exist_list_all(var_dict,parse_tree.children[1])):return False
    elif(parse_tree.data[1]=="member"):pass #NIL반환하는 경우를 찾아서 처리해줘야함
    elif(parse_tree.data[1]=="nth"):pass #list를 반환하지 않는 경우를 찾아줘야1

    return True

def is_numeric(var_dict,parse_tree):
    if(parse_tree.data[0]=='ident'):
        if(parse_tree.data[1] in var_dict):
            if(var_dict[parse_tree.data[1]][0]!="literal" ):
                return False
    elif(parse_tree.data[0]=="variable" or parse_tree.data[0]=="string" or parse_tree.data[0]=="literal_list"):
        return False
    elif(parse_tree.data[1]=="list" or parse_tree.data[1]=="cdr" or parse_tree.data[1]=="cons" or parse_tree.data[1]=="reverse"or parse_tree.data[1]=="subst"):
        return False
    elif(parse_tree.data[1]=="append" or  parse_tree.data[1]=="member" or parse_tree.data[1]=="remove"or parse_tree.data[1]=="assoc"):
        return False
    elif(parse_tree.data[1]=="setq"):
        if(not is_numeric(var_dict,parse_tree.children[1])):return False
    elif(parse_tree.data[1]=="car"):pass #숫자를 반환하지 않는 경우를 찾아서 처리해줘야함
    elif(parse_tree.data[1]=="nth"):pass #숫자를 반환하지 않는 경우를 찾아줘야1

    return True

def is_numeric_all(var_dict,parse_tree):
    for i in parse_tree.children:
        if(i.data[0]=='ident'):
            if(i.data[1] in var_dict):
                if(var_dict[parse_tree.data[1]][0]!="literal" ):
                    return False
        elif(i.data[0]=="variable" or i.data[0]=="string" or i.data[0]=="literal_list"):
            return False
        elif(i.data[1]=="list" or i.data[1]=="cdr" or i.data[1]=="cons" or i.data[1]=="reverse"or i.data[1]=="subst"):
            return False
        elif(i.data[1]=="append" or  i.data[1]=="member" or i.data[1]=="remove"or i.data[1]=="assoc"):
            return False
        elif(i.data[1]=="setq"):
            if(not is_numeric_all(var_dict,i.children[1])):return False
        elif(i.data[1]=="car"):pass #숫자를 반환하지 않는 경우를 찾아서 처리해줘야함
        elif(i.data[1]=="nth"):pass #숫자를 반환하지 않는 경우를 찾아줘야1

    return True

#for making parse_tree
class TreeNode(object):
    def __init__(self,data, children=[]):
        self.data=data
        self.children=list(children)

        #add children for TreeNode, it should give list of TreeNode
    def add(self,children):
        self.children.extend(children)

        #check it has tree structure
    def isleaf(self):
        if len(self.children)==0:
            return True
        else:
            return False

        #traverse by order(left->right->root)
    def postorder(self):

        traverse = []

        if self.children:
            for i in self.children:
                traverse += i.postorder()
        traverse.append(self.data)
        return traverse

        #return TreeNode's depth
    def depth(self):
        level=[]

        if self.children:
            for i in self.children:
                level.append(i.depth())
        else:
            return 1

        return max(level) + 1

        #return who is deeper between left children TreeNode and right children TreeNode
    def whodeeper(self):
        level=[]
        for i in self.children:
            level.append(i.depth())
        max_num=max(level)
        index=level.index(max_num)
        return index
