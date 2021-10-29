filepath = "valaszok.txt"
fileobject = open(filepath, "r")
number_of_contestants = fileobject.readlines()
print("2. Feladat: A versenyen ", len(number_of_contestants) - 1, " versenyző indult.")
fileobject.close()

fileobject = open(filepath, "r")
my_list = []
reading = fileobject.read().replace("\n", " ")
my_list.append(str(reading))
id = input("3. Feladat: Kérem adja meg a versenyző azonosítóját: ")
if id in my_list == True:
    print("A hozzá tartozó megoldások: ", my_list.index(id, +1, +14))

answers = my_list.index(id, +1, +14)
correct = "BCCCDBBBBCDAAA"
print("4. Feladat: A helyes megoldások: BCCCDBBBBCDAAA\n")
for i in correct:
    if answers == correct:
        print("+")
    else:
        print(" ")


fileobject = open(filepath, "r")
task_number = int(input("5. Feladat: Kérem adja meg egy feladat sorszámát: "))
a = 0
if 15 > task_number > 0:
    if task_number == correct[task_number]:
        a += 1
    else:
        a = a



fileobject.close()


fileobject = open(filepath, "r")
mylist = []
reading = fileobject.read()
mylist.append(reading)
p = 0
answer = ""
for i in correct:
    if i > 0 and i < 6:
        if answer[i] == correct[i]:
            p += 3
            if i > 5 and i < 11:
                if answer[i] == correct[i]:
                    p += 4
                    if i > 10 and i < 14:
                        p += 5
                        if i == 14:
                            p += 6
        else:
            p = p

print(f"6. Feladat: A versenyzők {p / number_of_contestants} százaléka átlagosan jól válaszolt.")

fileobject.close()

mylist.sort()
print("7. Feladat: A verseny legjobbjai: ")
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])

