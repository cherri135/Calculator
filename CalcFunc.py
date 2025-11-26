import time
import operator

operators = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}

def CheckIfOperator(Char):
    for operator in operators:
        if Char == operator:
            return True

def RemoveDoubleOperators(ProblemToCalculate):

    clean = ""

    LastWasOper = False

    for Char in ProblemToCalculate:
        if CheckIfOperator(Char):
            if LastWasOper:
                continue
            else:
                LastWasOper = True
                clean += Char
        else:
            LastWasOper = False
            clean += Char

    return clean

def RemoveOperatorsAtEnd(ProblemToCalculate, clean):

    if CheckIfOperator(clean[-1]):
        clean = ProblemToCalculate[:-1]
        RemoveOperatorsAtEnd(ProblemToCalculate, clean)

    return clean

def RoundNumberIfPossibleAtEnd(result):

    if result[-1] == "0" or result[-1] == 0:
        CleanedResult = result[:-1]
        result = CleanedResult
        if result[-1] == ".":
            CleanedResult = result[:-1]
            result = CleanedResult
            return result
        RoundNumberIfPossibleAtEnd(result)

    return result

def FixInput(Problem):
    ProblemToCalculate = ""

    NumberOneIs = False
    OperatorIs = False
    SecondNumberIs= False



    for Char in Problem:
        try:
            int(Char)
            ProblemToCalculate = ProblemToCalculate + str(Char)
        except ValueError:
            if CheckIfOperator(Char):
                ProblemToCalculate = ProblemToCalculate + str(Char)
            elif Char == ".":
                ProblemToCalculate = ProblemToCalculate + str(Char)

    for char in ProblemToCalculate:
        if NumberOneIs == False:
            try:
                int(char)
                NumberOneIs = True
            except ValueError:
                continue
        elif OperatorIs == False:
            if CheckIfOperator(char) == True:
                OperatorIs = True
        elif SecondNumberIs == False:
            try:
                int(char)
                SecondNumberIs = True
            except ValueError:
                continue
    
    if  NumberOneIs == True and OperatorIs == True and SecondNumberIs == True:
        return ProblemToCalculate
    else:
        print("\nyou gotta have atleast 2 numbers with an operator in between hun (it doesnt take any letters btw)\nIt looked like this:", ProblemToCalculate)
        TakeProblem()

def CalculateProblem(ProblemToCalculate):

    FirstNum = None
    oper = None
    SecondNum = None

    lenght = 0

    while True:

        if CheckIfOperator(ProblemToCalculate[0]):

            ProblemToCalculate = ProblemToCalculate[1:]

        else:
            break

        time.sleep(0.1)

    ProblemToCalculate = RemoveDoubleOperators(ProblemToCalculate)

    clean = ProblemToCalculate

    ProblemToCalculate = RemoveOperatorsAtEnd(ProblemToCalculate, clean)

    print("\nFixed it if there was some syntax errors :P\nYourProblem:", ProblemToCalculate)

    while True:

        for char in ProblemToCalculate:
            try:
                if char != ".":
                    char = float(char)
                    char = int(char)
                if FirstNum is None:
                    FirstNum = str(char)
                else:
                    FirstNum += str(char)
            except ValueError:
                if char == ".":
                    FirstNum += str(char)
                elif FirstNum == None:
                    continue
                else:
                    FirstNumLenght = len(FirstNum)
                    break
        
        for char in ProblemToCalculate:
            if CheckIfOperator(char):
                if oper is None:
                    oper = str(char)
                    break

        if oper == None:
            exit()
        
        for char in ProblemToCalculate[FirstNumLenght:]:
            try:
                if char != ".":
                    char = float(char)
                    char = int(char)
                if SecondNum is None:
                    SecondNum = str(char)
                else:
                    SecondNum += str(char)
            except ValueError:
                if char == ".":
                    SecondNum += str(char)
                elif SecondNum == None:
                    continue
                else:
                    break
        break

    lenght = len(FirstNum + oper + SecondNum)

    ProblemToCalculate = ProblemToCalculate[lenght:]

    OpToCalc = operators[str(oper)]

    result = ""

    if float(FirstNum) != None and str(oper) == "/" and float(SecondNum) == 0:
        result = "Error: tried to divide by 0"
        return result

    else:
        result = str(OpToCalc(float(FirstNum), float(SecondNum)))

    if ProblemToCalculate == "":

        result = RoundNumberIfPossibleAtEnd(result)
        return result
    
    else:

        ProblemToCalculate = str(result) + str(ProblemToCalculate)
        FirstNum = None
        oper = None
        SecondNum = None
        lenght = 0
        return CalculateProblem(ProblemToCalculate)

def CheckIfContinue():
    A = input("\n\nYa wanna make another calculation?\ny / n\n\nanswer:").lower()

    if A == "y":
        TakeProblem()
    elif A == "n":
        print("alright bye\n")
        exit()
    else:
        print("Type only 'y' or 'n' yeah?")
        CheckIfContinue()

def TakeProblem():
    while True:
        try:
            Problem = input("\nsay your math problem yeah: ")
            break
        except KeyboardInterrupt:
            print("\ney, u cancelled it")

    ProblemToCalculate = FixInput(Problem)

    result = CalculateProblem(ProblemToCalculate)

    print("\nresult =", result)

    CheckIfContinue()

TakeProblem()