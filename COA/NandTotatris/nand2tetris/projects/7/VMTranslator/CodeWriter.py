import os

class CodeWriter:
    def __init__(self, filePath):
        self.filePath = filePath.split(".vm")[0] + ".asm"
        self.file = open(self.filePath, "w+")
        self.fileName = os.path.basename(self.filePath)
        self.compareCounter = 0

    def setFileName(self, fileName):
        self.fileName = fileName + ".asm"

    def unaryOp(self, operation):
        asmInstr = (
            "@SP\n"
            "AM = M - 1\n"
            "M = " + operation + "M\n"
            "@SP\n"
            "M = M + 1\n"
        )
        return asmInstr

    def binaryOp(self, operation):
        asmInstr = (
            "@SP\n"
            "AM = M - 1\n"
            "D = M\n"
            "@SP\n"
            "AM = M - 1\n"
            "M = M " + operation + " D\n"
            "@SP\n"
            "M = M + 1\n"
        )
        return asmInstr

    def compareOp(self, command):
        asmInstr = (
            "@SP\n"
            "AM = M - 1\n"
            "D = M\n"
            "@SP\n"
            "AM = M - 1\n"
            "D = M - D\n"
            "@PASS" + str(self.compareCounter) + "\n"
            "D;J" + command.upper() + "\n"
            "D = 0\n"
            "@END" + str(self.compareCounter) + "\n"
            "0;JMP\n"
            "(PASS" + str(self.compareCounter) + ")\n"
            "@SP\n"
            "D = -1\n"
            "(END" + str(self.compareCounter) + ")\n"
            "@SP\n"
            "A = M\n"
            "M = D\n"
            "@SP\n"
            "M = M + 1\n"
        )
        self.compareCounter += 1
        return asmInstr

    def writeArithmetic(self, command):
        asmInstr = ""
        if command == "add":
            asmInstr = self.binaryOp("+")
        elif command == "sub":
            asmInstr = self.binaryOp("-")
        elif command == "neg":
            asmInstr = self.unaryOp("-")
        elif command == "eq":
            asmInstr = self.compareOp(command)
        elif command == "gt":
            asmInstr = self.compareOp(command)
        elif command == "lt":
            asmInstr = self.compareOp(command)
        elif command == "or":
            asmInstr = self.binaryOp("|")
        elif command == "and":
            asmInstr = self.binaryOp("&")
        elif command == "not":
            asmInstr = self.unaryOp("!")
        self.file.write(asmInstr)

    def writePush(self):
        asmInstr = (
            "@SP\n"
            "A = M\n"
            "M = D\n"
            "@SP\n"
            "M = M + 1\n"
        )
        return asmInstr

    def writePushPop(self, command, segment, index):
        asmInstr = ""
        segmentTranslator = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
            "pointer": 3,
            "temp": 5
        }

        if command == "C_PUSH":
            if segment == "static":
                asmInstr = (
                    "@" + self.fileName.split(".")[0] + "." + str(index) + "\n"
                    "D = M\n"
                    + self.writePush()
                )
            elif segment in {"local", "argument", "this", "that"}:
                asmInstr = (
                    "@" + segmentTranslator[segment] + "\n"
                    "D = M\n"
                    "@" + str(index) + "\n"
                    "A = D + A\n"
                    "D = M\n"
                    + self.writePush()
                )
            elif segment == "constant":
                asmInstr = (
                    "@" + str(index) + "\n"
                    "D = A\n"
                    + self.writePush()
                )
            elif segment in {"pointer", "temp"}:
                asmInstr = (
                    "@R" + str(index + segmentTranslator[segment]) + "\n"
                    "D = M\n"
                    + self.writePush()
                )

        elif command == "C_POP":
            if segment == "static":
                asmInstr = (
                    "@SP\n"
                    "AM = M - 1\n"
                    "D = M\n"
                    "@" + self.fileName.split(".")[0] + "." + str(index) + "\n"
                    "M = D\n"
                )
            elif segment in {"local", "argument", "this", "that"}:
                asmInstr = (
                    "@" + segmentTranslator[segment] + "\n"
                    "D = M\n"
                    "@" + str(index) + "\n"
                    "D = D + A\n"
                    "@R13\n"
                    "M = D\n"
                    "@SP\n"
                    "AM = M - 1\n"
                    "D = M\n"
                    "@R13\n"
                    "A = M\n"
                    "M = D\n"
                )
            elif segment in {"pointer", "temp"}:
                asmInstr = (
                    "@SP\n"
                    "AM = M - 1\n"
                    "D = M\n"
                    "@R" + str(index + segmentTranslator[segment]) + "\n"
                    "M = D\n"
                )
        self.file.write(asmInstr)

    def closeFile(self):
        self.file.close()
        try:
            os.rename(self.filePath, os.path.join(os.path.dirname(self.filePath), self.fileName))
        except FileExistsError:
            os.remove(os.path.join(os.path.dirname(self.filePath), self.fileName))
            os.rename(self.filePath, os.path.join(os.path.dirname(self.filePath), self.fileName))
