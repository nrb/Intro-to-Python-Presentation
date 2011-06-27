"""
Takes all the exercise scripts in the current directory and converts them into a format suitable for reStructured Text inline examples.

Useful if you want to have executable code that also gets included into a document.
"""
from glob import glob

exercise_scripts = glob("exercise*.py")

for script in exercise_scripts:
    ex_number = script[-4]

    with open(script, "r") as f:
        c = f.read()

    solution_text = ["Solution %s::" % ex_number, "\n"]
    c = c.split("\n")

    # Append indentation and rejoin.
    c = solution_text + ["   " + l for l in c]
    c = "\n".join(c)

    with open("solutions/solution%s.rst" % ex_number, "w") as f:
        f.write(c)



