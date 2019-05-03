a = 20

if a==20:
    print("nilai anda adalah", a)

if a is not 40:
    print("nilai anda bukan 60")

print(80*"=")

nilai =30

if 80<=nilai<=100:
    print("nilai anda adalah A")
elif 70<=nilai<80:
    print("nilai anda adalah B")
elif 60<=nilai<70:
    print("nilai anda adalah C")
elif 50<=nilai<60:
    print("nilai anda adalah D")
else:
    print("maaf nilai anda adalah",nilai,", anda dinyatakan tidak lulus")

print(80*"=")

#operator logika pada list dan string

kucing = ["chaky","choky","chuky","unyil","ucrit","oren","pussy","pengkor","ucul"]
lucu = "eek"
lucu2 = "chaky"

print("- siapakah kucing terlucu disini, ",lucu2,"atau",lucu,"?")
if lucu2 in kucing:
    print('- fahri bilang, "kucing terlucu disini adalah',lucu2,'"')
if not lucu in kucing:
    print('- fahri bilang, "kalau nama kucing',lucu,'saya tidak kenal"')

print(80*"=")
print("\n")