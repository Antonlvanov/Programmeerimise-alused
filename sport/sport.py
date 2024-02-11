import random

sportlased = []
tulemused = []

def fill_lists():
    global sportlased, tulemused
    num_athletes = int(input("Sisestage sportlaste arv: "))
    for i in range(num_athletes):
        name = input(f"Sisestage sportlase nimi {i+1}: ")
        sportlased.append(name)
        result = max(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
        tulemused.append(result)

def top_n_results(n):
    sorted_results = sorted(zip(tulemused, sportlased), reverse=True)
    print(f"Parimad {n} tulemused:")
    for i in range(min(n, len(sorted_results))):
        result, athlete = sorted_results[i]
        print(f"{i+1}. {athlete}: {result}")

def sort_results():
    sorted_results = sorted(zip(tulemused, sportlased))
    print("Sorteeritud nimekiri tulemuste järgi kasvavalt:")
    for i in range(len(sorted_results)):
        result, athlete = sorted_results[i]
        print(f"{i+1}. {athlete}: {result}")

def find_results_by_name(names):
    for name in names:
        try:
            index = sportlased.index(name)
            print(f"{name} tulemus: {tulemused[index]}")
        except ValueError:
            print(f"Sportlast {name} ei leitud.")

def disqualify_below_threshold(threshold):
    global sportlased, tulemused
    disqualified_indices = []
    for i in range(len(tulemused)):
        if tulemused[i] < threshold:
            disqualified_indices.append(i)
    for index in sorted(disqualified_indices, reverse=True):
        del sportlased[index]
        del tulemused[index]
    sorted_results = sorted(zip(tulemused, sportlased), reverse=True)
    print("\nUuendatud sportlaste nimekiri ja nende tulemused:")
    for i, (result, athlete) in enumerate(sorted_results):
        print(f"{i+1}. {athlete}: {result}")
        
def average():
    total_results = sum(tulemused)
    average = total_results / len(tulemused)
    print(f"Kõigi sportlaste keskmine tulemus: {average}")

fill_lists()
while True:
    print("\nMenüü:")
    print("1. Vaata parimaid tulemusi")
    print("2. Sorteeri nimekiri kahanemisjärjekorras tulemuste järgi")
    print("3. Leia sportlase tulemus(või tulemused) nime järgi")
    print("4. Diskvalifitseeri sportlased, kelle tulemus on madalam kui etteantud lävend")
    print("5. Näita sportlaste keskmist tulemust")
    print("0. Välju")
    choice = input("Valige tegevus: ")
    if choice == '1':
        n = int(input("Sisestage parimate tulemuste arv: "))
        top_n_results(n)
    elif choice == '2':
        sort_results()
    elif choice == '3':
        names = input("Sisestage sportlaste nimed (koma eraldatud): ").split(',')
        find_results_by_name(names)
    elif choice == '4':
        threshold = int(input("Sisestage diskvalifikatsiooni lävend: "))
        disqualify_below_threshold(threshold)
    elif choice == '5':
        average()
    elif choice == '0':
        break
    else:
        print("Vale valik. Palun proovige uuesti.")
