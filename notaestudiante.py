s1=(input("digitar la nota de seguimiento uno:"))
s1f="s1*0.1"
p1=(input("digitar la nota de parcial uno:"))
p1f="p1*0.25"
s2=(input("digitar la nota de seguimiento dos:"))
s2f="s2*0.1"
p2=(input("digitar la nota de parcial dos:"))
p2f="p2*0.3"
l=(input("digitar la nota de l:"))
lf="l*0.25"
sn="s1f+p1f+s2f+p2f+lf"
print("suma de notas:",sn)

if sn>=3.0:
   print("paso el semestre")
else:
   print("no paso el semestre")

