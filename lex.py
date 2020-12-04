import re


temp=0
buffer=str()
nextToken=str()
lexeme=str()
buffersize=0
lexLen=0
nextChar=str()
token_list=[]
fun_cadr=re.compile('ca+d+r') #a와 d가 최소 1번 이상 나오는 lexeme을 판단하기 위함 (cadr 종류에 대한 모든 경우의 수를 처리하기 위함)

    #lexer makes token_list(list of tuple) by input_string(string) from user.
    #lexer maps lexeme and corresponding token.
    #then makes a list of tuple(token,lexeme) for input_string gives it to parser.
    #lex.py code is made from c code(front.c) in PL lecture note 4.


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
    # 들어온 lexeme이 예약어인지 확인해준다. 아닌 경우 변수 취급
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
    elif(cmpstr=="print"):return "print"
    elif(cmpstr=="if"):return "if"
    elif(cmpstr=="cond"):return "cond"
    elif(fun_cadr.match(cmpstr)!=None):return "cadr" # 조합을 'ca+d+r'이라는 정규표현식으로 나타냄
    elif(cmpstr=="t"):return "true"
    elif(cmpstr=="nil"):return"false"
    elif(cmpstr=="print"):return"print"
    else:return "ident"

def lookup(ch):
    if ch in ['(', ')', '+', '-', '*', '/', '\\',';', '=', '<', '>', '#', "'",'"']:
        return ch
    else:
        print(ch+" is not readable syntax")
        raise NotImplementedError
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
        nextToken=symbol(lexeme) #들어온 lexeme이 ident인지 혹은 예약어인지 판단해줌
    elif(nextChar.isdigit()):
        addChar()
        getChar()
        cnt=0  #정수 혹은 실수(소수점)가 들어온 경우를 받아줌
        while(nextChar=="." or nextChar.isdigit()):
            if(nextChar=="." and cnt==0):
                cnt=cnt+1
            elif(nextChar=="." and cnt!=0):
                print(lexeme+"is bad number")
                raise NotImplementedError
            addChar()
            getChar()
        nextToken = 'literal'
    elif(nextChar=="'"): #'(1 2 3) 나 'x가 들어오는 경우 각각 literal_list와 variable로 판단
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
            nextToken="variable" # 'x 'a 같은게 들어온 경우 variable로 취급
    elif(nextChar=='"'): #큰 따옴표를 감싸진 문자열이 들어오는 경우 string 취급
        addChar()
        getChar()
        while(nextChar!='"'):
            addChar()
            getChar()
        addChar()
        getChar()
        nextToken="string"
    elif(nextChar=="-"): # -가 들어온 경우 -연산자인지 혹은 -숫자(음수)를 나타내기 위한건지 판단
        addChar()
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

    else: #그 외 기호가 들어온 경우
        nextToken=lookup(nextChar)
        addChar()
        getChar()
    # 최종반환값은 (토큰,lexeme)형태의 튜플이며, 각 입력값은 이런 튜플의 리스트로 변환된다.(이후 parser함수로 전달)
    token_list.append((nextToken,lexeme))

def addChar():
    # 모든 lexeme은 소문자로 변환돼서 저장된다.
    # lexeme 최대 길이는 98이다.
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
