from pyscript import document, display

def average_grade(e):
    num1 = float(document.getElementById("english").value)
    num2 = float(document.getElementById("math").value)
    num3 = float(document.getElementById("science").value)
    
    avg = (num1 + num2 + num3)/3
    display(avg, target="avg")

# conditional check to display if student passed
# i searched on w3schools for help on how to do this :3
    if avg > 75:
        display("passed", target="pass")
    else:
        display("failed", target="pass")

heading = "grade average finder ─ .✦"
display(heading, target="heading")