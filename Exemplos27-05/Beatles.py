import time

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Lista dos Beatles:", beatles)

for i in range(2):  
    membro = input("Digite o nome do próximo membro da banda: ")
    beatles.append(membro)

print("Lista dos Beatles:", beatles)

del beatles[3:]  

beatles.insert(0, "Ringo Starr")

print("Lista final dos Beatles:", beatles)

time.sleep(2)