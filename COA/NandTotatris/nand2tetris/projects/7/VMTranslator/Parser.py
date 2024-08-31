class Parser:
    def __init__(self, filePath):
        self.currentCommand = ""
        self.currentCommandCounter = 0
        self.programIn = []

        with open(filePath, 'r') as file:
            self.programIn = file.read().splitlines()
            self.programIn = [line.split("//")[0].strip() for line in self.programIn]  # Remove comments
            self.programIn = list(filter(None, self.programIn))  # Remove empty lines

    def hasMoreCommands(self):
        return self.currentCommandCounter < len(self.programIn)

    def advance(self):
        self.currentCommand = self.programIn[self.currentCommandCounter].split("//")[0]
        self.currentCommandCounter += 1

    def commandType(self):
        commandTypes = {
            "add": "C_ARITHMETIC",
            "sub": "C_ARITHMETIC",
            "neg": "C_ARITHMETIC",
            "eq": "C_ARITHMETIC",
            "gt": "C_ARITHMETIC",
            "lt": "C_ARITHMETIC",
            "and": "C_ARITHMETIC",
            "or": "C_ARITHMETIC",
            "not": "C_ARITHMETIC",
            "pop": "C_POP",
            "push": "C_PUSH",
            "label": "C_LABEL",
            "goto": "C_GOTO",
            "if-goto": "C_IF",
            "function": "C_FUNCTION",
            "call": "C_CALL",
            "return": "C_RETURN"
        }
        return commandTypes[self.currentCommand.split()[0]]

    def arg1(self):
        if self.commandType() == "C_ARITHMETIC":
            return self.currentCommand.split()[0]
        else:
            return self.currentCommand.split()[1]

    def arg2(self):
        return self.currentCommand.split()[2]
