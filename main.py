import lex
import parse
import evalu



    #for one loop, interpreter receives input string from user and it prints results.
    #var_dict is dictionary for user's variable.


print("LISP Interpreter")
var_dict={}


while(1):
    buffer=input('>')
    try:
        result=evalu.eval(var_dict,parse.parser(var_dict,lex.lexer(buffer)))
        print(result)
        print(var_dict)
    except NotImplementedError:
        pass

"""
while(1):
    buffer=input('>')
    while(1):
        stack=[]
        for i in buffer:
            if(i=="("):
                stack.append(i)
            elif(i==")"):
                stack.pop()
        if(len(stack)!=0):
            print("Not match pair of '()'")
            break
        else:
            try:
                #result=evalu.eval(var_dict,parse.parser(var_dict,lex.lexer(buffer)))
                lex_result=lex.lexer(buffer)
                parse_result=parse.parser(var_dict,lex_result)
                evalu.sementic_analysis(var_dict,parse_result)
                #print(result)
                #print(var_dict)
            except NotImplementedError:
                pass
            break
"""
