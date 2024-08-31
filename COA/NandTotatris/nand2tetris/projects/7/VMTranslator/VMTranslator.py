import sys
import Parser
import CodeWriter

def main():
    if len(sys.argv) != 2:
        print("Usage: python VMTranslator.py <input_file.vm>")
        sys.exit(1)

    input_filename = sys.argv[1]


    parse = Parser.Parser(input_filename)
    codeWriter = CodeWriter.CodeWriter(input_filename)

    while parse.hasMoreCommands():
        parse.advance()
        if parse.commandType() == "C_ARITHMETIC":
            codeWriter.writeArithmetic(parse.currentCommand)

        elif parse.commandType() in {"C_POP", "C_PUSH"}:
            codeWriter.writePushPop(parse.commandType(), parse.arg1(), int(parse.arg2()))

    codeWriter.closeFile()

if __name__ == "__main__":
    main()
