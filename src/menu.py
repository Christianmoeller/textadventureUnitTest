def menu(question, functions):
    notDone = True
    print(question)
    answerlist = list(functions.keys())
    for i in range(len(answerlist)):
        print(i+1, ":", answerlist[i])
    while notDone:
        userinput = input()
        if userinput.isnumeric():
            userinput = int(userinput)-1
            if userinput in list(range(len(answerlist))):
                function = functions[answerlist[userinput]]
                perform(function[0], function[1])
                notDone = False
            else:
                print("Bitte eine passende Antwort")
        else:
            if userinput in answerlist:
                function = functions[userinput]
                perform(function[0], function[1])
            else:
                print("Bitte eine passende Antwort")

def perform(func, args):
    func(*args)