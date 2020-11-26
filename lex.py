import re


temp=0
buffer=str()
nextToken=str()
lexeme=str()
buffersize=0
lexLen=0
nextChar=str()
token_list=[]


    #lexer makes token_list(list of tuple) by input_string(string) from user.
    #lexer maps lexeme and corresponding token.
    #then makes a list of tuple(token,lexeme) for input_string gives it to parser.
    #lex.py code is made from c code(front.c) in PL lecture note.


def lexer(input_string):
    global buffer
    global buffersize
    global temp
    global token_list
    token_list=[]
    buffer=input_string.strip()
    temp=0
    buffersize=len(buffer)
    getChar()
    lex()
    while(temp<=buffersize):
        lex()
    return token_list

def symbol(lex):
    cmpstr=lex.lower()
    #print(cmpstr)
    if(cmpstr=="setq"):return "setq"
    elif(cmpstr=="list"):return "list"
    elif(cmpstr=="cdr"):return "cdr"
    elif(cmpstr=="car"):return "car"
    elif(cmpstr=="nth"):return "nth"
    elif(cmpstr=="cons"):return "cons"
    elif(cmpstr=="reverse"):return "reverse"
    elif(cmpstr=="append"):return "append"
    elif(cmpstr=="length"):return "length"
    elif(cmpstr=="member"):return "member"
    elif(cmpstr=="assoc"):return "assoc"
    elif(cmpstr=="remove"):return "remove"
    elif(cmpstr=="subst"):return "subst"
    elif(cmpstr=="atom"):return "atom"
    elif(cmpstr=="null"):return "null"
    elif(cmpstr=="numberp"):return "numberp"
    elif(cmpstr=="zerop"):return "zerop"
    elif(cmpstr=="minusp"):return "minusp"
    elif(cmpstr=="equal"):return "equal"
    elif(cmpstr=="stringp"):return "stringp"
    elif(cmpstr=="if"):return "if"
    elif(cmpstr=="cond"):return "cond"
    elif(cmpstr=="caddr"):return "caddr" #car+cdr 조합은 곧 만들 예정
    elif(cmpstr=="t"):return "true"
    elif(cmpstr=="nil"):return"false"
    else:return "ident"

def lookup(ch):
    if ch in ['(', ')', '+', '-', '*', '/', ';', '=', '<', '>', '#', "'",'"']:
        return ch
    else:
        return 'error'
def getChar():
    global nextChar
    global buffer
    global temp

    if temp<buffersize:
        nextChar=buffer[temp]
    else:
        nextChar='\0'
    temp=temp+1
def getNonBlank():
    global nextChar
    while(nextChar.isspace()):
        getChar()
def lex():
    global lexLen
    global nextChar
    global nextToken
    global lexeme
    lexLen=0
    lexeme=''
    getNonBlank()
    if(nextChar.isalpha()):
        addChar()
        getChar()
        while(nextChar.isalpha() or nextChar.isdigit()):
            addChar()
            getChar()
        nextToken=symbol(lexeme)
    elif(nextChar.isdigit()):
        addChar()
        getChar()
        cnt=0
        while(nextChar=="." or nextChar.isdigit()):
            if(nextChar=="." and cnt==0):
                cnt=cnt+1
            elif(nextChar=="." and cnt!=0):
                print(lexeme+"is bad number")
                raise NotImplementedError
            addChar()
            getChar()
        nextToken = 'literal'
    elif(nextChar=="'"):
        getChar()
        if(nextChar=="("):
            stack=[]
            blank=[]
            stack.append(nextChar)
            while(True):
                if(nextChar==" " and len(blank)!=0):
                    getChar()
                elif(nextChar==" " and len(stack)>1 and lexeme[-1]=="("):
                    getChar()
                else:
                    if(nextChar==" " and len(blank)==0):
                        blank.append(nextChar)
                    elif(nextChar!=" " and len(blank)!=0):
                        blank.pop()
                    elif(nextChar=="("):
                        if(len(lexeme)>0 and lexeme[-1]==")"):
                            lexeme=lexeme+" "
                    addChar()
                    getChar()
                if(nextChar=="("):
                    stack.append(nextChar)
                elif(nextChar==")"):
                    if(len(stack)==1):
                        stack.pop()
                        break
                    else:
                        if(lexeme[-1]==" "):
                            lexeme=lexeme[:-1]
                        stack.pop()

            addChar()
            getChar()
            lexeme="("+lexeme[1:-1].strip()+")"
            nextToken="literal_list"
        else:
            addChar()
            getChar()
            while(nextChar.isalnum()):
                addChar()
                getChar()
            nextToken="variable" # it means case of 'X #나중에 symbol로 이름 바꾸기
    elif(nextChar=='"'):
        addChar()
        getChar()
        while(nextChar!='"'):
            addChar()
            getChar()
        addChar()
        getChar()
        nextToken="string"
    elif(nextChar=="-"):
        addChar() #-들어감
        getChar()
        if(nextChar.isspace()):
            nextToken="-"
        else:
            if(nextChar.isdigit()):
                addChar()
                getChar()
                cnt=0
                while(nextChar=="." or nextChar.isdigit()):
                    if(nextChar=="." and cnt==0):
                        cnt=cnt+1
                    elif(nextChar=="." and cnt!=0):
                        print(lexeme+"is bad number")
                        raise NotImplementedError
                    addChar()
                    getChar()
            nextToken='literal'

    else:
        nextToken=lookup(nextChar)
        addChar()
        getChar()
    #print("Next token is: "+nextToken+", Next lexeme is "+lexeme)
    token_list.append((nextToken,lexeme))

def addChar():
    global temp
    global lexLen
    global buffer
    global lexeme
    global nextChar
    if(nextChar.isalpha()):nextChar=nextChar.lower()
    if(lexLen<=98):
        lexeme=lexeme+nextChar
        lexLen = lexLen + 1
    else:
        print("Error-lexeme is too long")
