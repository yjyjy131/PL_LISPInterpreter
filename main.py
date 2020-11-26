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
