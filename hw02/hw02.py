import re

print("Task 1 ===================================")


def find_and_print(messages):
    # Messages can be divided into 2 parts:
    # 1. expressing real number form within string, which need to change into number form to check whether is larger than 17
    # 2. put some keywords(symbols or behaviors) in a set that should be of age.
    #    Myabe I can add more sets as dataSets and another function number parameter to check is over/under age division...
    # Steps:
    # 1. check whether there is number sign within message (need to know how to parse string by regular expression)
    # (1) set the match mode by re.compile() function storing in numberAge
    # (2) place message into the mode which return match object.
    # cases: a. matched: match.group(0) => return all matching result
    #        b. matched: match.group(1) => return the first group '()' I set in 1.(1)
    # 2. check whether there is keyword in messages

    # define match mode
    numberAge = re.compile(r'(\d+) years old')
    # keywords set
    ageOverEighteen = {"college student", "vote", "legal age", "marriage",
                       "driver license", "adult", "loan", "pension", "Graduate student", "PhD"}
    for name, message in messages.items():
        # check whether number age > 17
        matchAge = numberAge.search(message)
        if matchAge and int(matchAge.group(1)) > 17:
            print(name)
            continue
        # check whether keywords in
        for keyword in ageOverEighteen:
            if keyword in message:
                print(name)
                break


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})


print("Task 2 ===================================")
def calculate_sum_of_bonus(data):
    # Performance for all are salary*baseBonusRate 0.2
    # BonusRate gaps are different:
    # 1.Engineer: 0.05
    # 2.CEO: 0.1
    # 3.Sales: 0.2
    # salary should chnage into number data type in TWD
    totalBonus = 0
    for employee in data['employees']:
        # Convert salary to number and change USD to TWD if needed
        salary = employee['salary']
        if isinstance(salary, str):
            if "USD" in salary:
                salary = int(salary.replace("USD", "")) * 30
            else:
                salary = int(salary.replace(",", ""))


        # baseBonusRate
        if employee['role'] in ['Engineer', 'CEO', 'Sales']:
            bonusRate = 0.1
        # perfermaces for engineer: level gap => 0.05
        if employee['role'] == 'Engineer' and employee['performance'] == 'above average':
            bonusRate += 0.05
        elif employee['role'] == 'Engineer' and employee['performance'] == 'below average':
            bonusRate -= 0.05

        # perfermaces for ceo: level gap => 0.1
        if employee['role'] == 'CEO' and employee['performance'] == 'above average':
            bonusRate += 0.1
        elif employee['role'] == 'CEO' and employee['performance'] == 'below average':
            bonusRate -= 0.1

        # perfermaces for sales: level gap => 0.2
        if employee['role'] == 'Sales' and employee['performance'] == 'above average':
            bonusRate += 0.2
        elif employee['role'] == 'Sales' and employee['performance'] == 'below average':
            bonusRate -= 0.2

        bonus = salary * bonusRate
        totalBonus += bonus

    if totalBonus > 10000:
        totalBonus = 10000

    print(totalBonus)


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})


print("Task 3 ===================================")
def func(*data):
    charCount = {}
    found = False
    for name in data:
        char = name[1]
        if char not in charCount:
            # need to create an empty dictionary first for char (can't get char automatically in the same time)
            charCount[char] = {}
            charCount[char]["count"] = 1
            charCount[char]["fullName"] = name
        else:
            charCount[char]["count"] += 1

    for key, value in charCount.items():
        if value["count"] == 1:
            print(value["fullName"])
            found = True
    if not found:
        print("沒有")


func("彭大牆", "王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有


print("Task 4 ===================================")

def get_number(index):
    if index == 0:
        print(0)
    # If index is even
    if index % 2 == 0:
        count = (index // 2) * 3
        print(count)
    # If index is odd
    else:
        count = (index // 2 + 1) * 3 + 1
        print(count)


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15

# Task 4 for recursion不熟，練習
print("Task 4-2 ===================================")

def get_numberRec(index):
    if index == 0:
        count = 0
        return count
    if index == 1:
        count = 4
        return count
    # If index is even
    if index % 2 == 0:
        count = get_numberRec(index - 2) + 3
        return count
    # If index is odd
    else:
        count = get_numberRec(index - 2) + 3
        return count


print(get_numberRec(1))  # print 4
print(get_numberRec(5))  # print 10
print(get_numberRec(10))  # print 15


print("Task 5 ===================================")

def find_index_of_car(seats, status, number): 
    countAvail = {}
    for i in range(len(status)):
        if status[i] == 1 and seats[i] >= number:
            countAvail[i] = seats[i] - number
    if not countAvail:
        print(-1)
        return
    else: 
        minAvail = min(countAvail.values())
        for key, value in countAvail.items():
            if value == minAvail:
                print(key)
    

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4 
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1 
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  #  print 2 
 