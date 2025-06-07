responses = ["Hello, My name is Machine","What may I help you?","Thank You","Bye-Bye",
    "Sorry, I don't know this","But next time I will surely do"]
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def end():
    print(responses[2])
    print(responses[3])
def extract_num(t1):
    l1=[]
    for w in t1.split():
        try:
            l1.append(float(w))
        except:
            pass
    return l1
def subhash():
    print("Subhash is a student of SGVU")
    print("He is from bihar")

operations={"ADDITION":add,"SUM":add,"PLUS":add,"ADD":add,"SUB":sub,"SUBTRACT":sub,"MINUS":sub,"MULTIPLY":mul,"DIVISION":div,"EVEN":even,"ODD":even}
commands={"SUBHASH":subhash,"BYE":end}
