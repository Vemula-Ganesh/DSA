class Solution:
    def interpret(self, command: str) -> str:
        result=""
        for i in range(len(command)-1):
            if command[i]=="G":
                result+="G"
            elif command[i]+command[i+1]=="al":
                result+="al"
            elif command[i]+command[i+1]=="()":
                result+="o"
        if command[-1]=="G":
            result+="G"
        return result

        