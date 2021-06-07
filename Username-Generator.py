# NickName Generator
# I studied python only for 2 days so i will make this code perfect as i study more, i have better ideas for username generator. This code is open so you can edit it as long as you don't steal the credits (you can add yours as extra)

# Put your nickname and birth date as additional nick suggestions will come out

# extra
male = 1
female = 0
Male = 1
Female = 0
yes = 1
no = 0
Yes = 1
No = 0

# YOU MUST CHANGE INFO. HERE TO YOUR
name = "Eddie"  # your name here
surname = "Johnson"  # put your surname
nickname = "Wolf"  # your nickname here
birth_d = "2002"  # put your birth date here if you want it to be known
married = No # are you married? Yes/No (If you don't wanna reply keep it as "No")
gender = Male  # change it to your gender male/female
nick_need = No  # Do you want ur nick to be in ur username. Put here Yes/No
birth_need = Yes  # do you want your birth date to be in your username Yes/No
s_need = Yes  # do you want your surname to be in ur username. Yes/No

# for me:
# n, n1 are nicknames n is the one user asked
# b,b1 are birth dates same as nick
# s,s1 are surnames same as nick
# a = the, a1 = aka ( related to nicknames )
# g is mr/mrs

# for developers/supporters:

# code itself
print("This code is valid till 2100")
print("Possible nicknames you asked for: ")

# birth related
if birth_need == 1:
    if birth_d == "":
        print("Input your birth date to line 18 please.")
    elif int(birth_d) >= 2000:
        b = int(birth_d) - 2000
        b1 = b
    elif int(birth_d) >= 1900:
        b = int(birth_d) - 1900
        b1 = b
elif birth_need == 0:
    b = ""
    if birth_d == "":
        print("Input your birth date to line 18 please, because script will generate extra usernames other than your "
              "request.")
    elif int(birth_d) >= 2000:
        b1 = int(birth_d) - 2000
    elif int(birth_d) >= 1900:
        b1 = int(birth_d) - 1900
else:
    print("Some error in line 21, please check it or contact owner through instagram 'pycharm.az'")

# nick related
if nick_need == 1:
    a = "the"
    a1 = "aka"
    if nickname == "":
        print("Input your nickname to line 17 please.")
    else:
        n = nickname
        n1 = nickname
elif nick_need == 0:
    a = ""
    a1 = ""
    n = ""
    if nickname == "":
        print("Input your nickname to line 17 please, because script will generate extra usernames other than your "
              "request.")
    else:
        n1 = nickname
elif nick_need == "":
    # add here nickname generator if empty (note for the future)
    print("Some error in line 20, please check it or contact owner through instagram 'pycharm.az'")


# surname related
if s_need == 1:
    if surname == "":
        print("Input your surname to line 16 please.")
    else:
        s = surname
        s1 = surname
elif s_need == 0:
    s = ""
    if surname == "":
        print("Input your surname to line 16 please, because script will generate extra usernames other than your "
              "request.")
    else:
        s1 = surname
elif s_need == "":
    # add here nickname generator if empty (note for the future)
    print("Some error in line 22, please check it or contact owner through instagram 'pycharm.az'")


# gender check
if gender == 1:
    m = "Mr"
elif gender == 0:
    if married == 1:
        m = "Mrs"
    elif married == 0:
        m = "Ms"

# printing nicknames you asked for
q = m + name + s + a1 + n + str(b)
w = m + name + s + a + n + str(b)
r = name + s + a1 + n + str(b)
t = name + s + a + n + str(b)
y = m + s + name + a1 + n + str(b)
u = m + s + name + a + n + str(b)
i = s + name + a1 + n + str(b)
o = s + name + a + n + str(b)
un = [q, w, r, t, y, u, u, i, o]
un1 = list(dict.fromkeys(un))
print(un1)

# printing nicknames i suggest
print("Nicknames i suggest (i think these will be better): ")
print(s1 + "the" + n1 + str(b1))
print(s1 + "aka" + n1 + str(b1))
print(name + "the" + n1)
print(name + "aka" + n1)
print(m + s1 + str(b1))
print(m + n1 + str(b1))
print(n1 + s1 + str(b1))
print(s1 + "the" + n1)
print(s1 + "aka" + n1)
print(name + str(b1))
print(m + s1)
print(m + n1)
print(n1 + s1)
