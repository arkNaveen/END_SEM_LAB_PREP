s = "This is a Sample String"
s2 = "Naveen K"
s3 = "My favaourite is Badmiton"
sx = "K\tL\tM\tMall"
si = "EC21B1030"
si2 = 30

print(s3.capitalize())
print(s2.casefold())
print(s.center(35))

# returns the number of occurences
print(s2.count("i"))
print(s3.encode(encoding = "ascii" , errors = "namereplace"))
print("The string " + s2 +" \nends with K ? " + str(s2.endswith('K')) + " found at index " + str(s2.index('K')))
print("The string " + s2 +" \nstarts with N ? " + str(s2.startswith('K')) + " found at index " + str(s2.index('N')))
print("Alternate location of N >? and " + str(s2.rfind('n'))+ " "+str(s2.rindex('n')))
print(sx.expandtabs(4))
print("K was found at " + str(s2.find('K')) + " Location also " )


# Formatting
print("My name is {} and my roll number is {} and {:b} in binary".format(s2,si,si2))

a = {'x':'PSP', 'y':'IDS'}
print("This is {y} and feels like {x}".format_map(a))


m = "lorem ipsum is simply printing script like "
n = "756738912"
o = "def"
p = "ilove30"


print("{} is LowerCase>? {}".format(m,m.islower()))
print(m.upper())
print("{} is upperCase>? {}".format(m,m.isupper()))

print("\"756738912\" is digit>? {}".format(n.isdigit()))
print("\"756738912\" is decimal>? {}".format(n.isdecimal()))
print("\"756738912\" is numeric>? {}".format(n.isnumeric()))

print(o.isidentifier())


stro = m + n + o + p
stro2 = (m+p).replace(" ","b")
print("The string \n{} \nis printable >? {}".format(stro, stro.isprintable()))

print("The sring \n{} \nis alphanumeric >? {}".format(stro2,stro2.isalnum()))

print("\nis alphabetic >? {}".format(stro2.isalpha()))

print("\nis identifier >? {}".format(stro2.isidentifier()))

print("\nis space >? {}".format(stro2.isspace()))

xtx = "SAMMY"
trans = str.maketrans("M","X")
print(xtx.translate(trans))

print(stro.title())
print("\nis the above string in Title {}".format((stro.title()).istitle()))

li = {"i","ama","ROCK","STAR"}
print("*".join(li))
sli = "*".join(li)
print(sli.split("*"))

if(si.isupper()):
    print(si.swapcase())
    print(si.islower())
    print(si.ljust(30))
    print(si.rjust(30))
    print(si.lstrip("30"))
    print(si.rstrip("30"))
    print(si.rsplit("3"))
    
r = "i am superman yall not batman"
print(r.partition("am"))
print(r.rpartition("am"))
print(r.zfill(30))

text = """This is a multi line string\nbrqace for impact \ncommand of breaching orders"""

print(text.splitlines())
# END OF PROGRAM

