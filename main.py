import lex
import parse
import evalu



    #for one loop, interpreter receives input string from user and it prints results.
    #var_dict is dictionary for user's variable.


print("LISP Interpreter")
var_dict={}


while(1):
    buffer=input('>')
    while(1):
        stack=[]
        for i in buffer:
            if(i=="("):
                stack.append(i)
            elif(i==")"):
                stack.pop()
        if(len(stack)!=0): # 괄호검사후 짝이 안맞으면 다시 입력값을 받는다
            print("Not match pair of '()'")
            break
        else:
            try: # 괄호검사후 짝이 맞으면 코드를 처리해준다.
                lex_result=lex.lexer(buffer)
                parse_result=parse.parser(var_dict,lex_result)
                evalu.sementic_analysis(var_dict,parse_result)

            except NotImplementedError:
                pass
            break
