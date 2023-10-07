def checking_input_list(words):
    if not words:  # check for
        print("if not words")

    if not len(words):  # check for 0
        print("if not len(words):")

    if not "      ":
        print(" empyt string")


checking_input_list([])


A0 = None
A1 = True
B0 = None
B1 = True

if not (A0 or B0):
    # = not (False)
    print("if not (A0 or B0):")

if not (A0 and B1):
    print("if not (A0 and B1):")
if not (A0 and B0):
    print("if not (A0 and B0):")

if None or None:
    print("if None or None:")  # does not print
