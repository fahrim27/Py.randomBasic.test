import difflib


tebak1 = input('masukkan nama kucing 1: ')
tebak1 = str(tebak1)
tebak2 = input('masukkan nama kucing 2: ')
tebak2 = str(tebak2)

sequence = difflib.SequenceMatcher(isjunk=None,a=tebak1,b=tebak2)
difference = sequence.ratio()*100
difference = round(difference,1)
print(50*'=')
print(str(difference) + "% kesamaan nama")
