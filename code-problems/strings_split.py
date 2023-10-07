input1 = "sab asdf qwerwer"
input2 = "asdf\nasdf"
input3 = "asdf\nasdf\t"
input4 = "sab     asdf qwerwer     "

inputs = [input1, input2, input3, input4]

for input in inputs:
    cnt = len(input.split())
    print(cnt)
