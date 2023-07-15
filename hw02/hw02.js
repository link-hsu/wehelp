//  Task 1
function findAndPrint(messages) {
  //  Messages can be divided into 2 parts:
  //  1. expressing real number form within string, which need to change into number form to check whether is larger than 17
  //  2. put some keywords(symbols or behaviors) in a set that should be of age.
  //     Myabe I can add more sets as dataSets and another function number parameter to check is over/under age division...
  //  Steps:
  //  1. check whether there is number sign within message (need to know how to parse string by regular expression)
  //  (1) set the match mode by match function storing in numberAge
  //  rm. match(/(\d+) years old/g) return total matching result; match(/(\d+) years old/) return the first matching result.
  //  cases: a. matched: match[0] => return overall matching result
  //         b. matched: match[1] => return the first group '()' I set in 1.(1)
  //  2. check whether there is keyword in messages

  // keywords set
  const keywords = new Set([
    "college student",
    "vote",
    "legal age",
    "marriage",
    "driver license",
    "adult",
    "loan",
    "pension",
    "Graduate student",
    "PhD",
  ]);

  for (let name in messages) {
    let message = messages[name];

    // define match mode
    let numberAge = message.match(/(\d+) years old/);
    // check whether number age > 17
    if (numberAge && Number(numberAge[1]) > 17) {
      console.log(name);
      continue;
    }
    // check whether keywords in
    for (let keyword of keywords) {
      if (message.includes(keyword)) {
        console.log(name);
        break;
      }
    }
  }
}

findAndPrint({
  Bob: "My name is Bob. I'm 18 years old.",
  Mary: "Hello, glad to meet you.",
  Copper: "I'm a college student. Nice to meet you.",
  Leslie: "I am of legal age in Taiwan.",
  Vivian: "I will vote for Donald Trump next week",
  Jenny: "Good morning.",
});

// Task 2
function calculate_sum_of_bonus(data) {
  // Performance for all are salary*baseBonusRate 0.2
  // BonusRate gaps are different:
  // 1.Engineer: 0.05
  // 2.CEO: 0.1
  // 3.Sales: 0.2
  // salary should chnage into number data type in TWD
  let totalBonus = 0;

  // Convert salary to number and change USD to TWD if needed
  for (let employee of data.employees) {
    let salary = employee.salary;

    if (typeof salary === "string") {
      if (salary.includes("USD")) {
        salary = parseInt(salary.replace("USD", "")) * 30;
      } else {
        salary = parseInt(salary.replace(",", ""));
      }
    }

    // baseBonusRate
    let bonusRate = 0.1;
    if (
      ["Engineer", "CEO", "Sales"].includes(employee.role)
    ) {
      bonusRate = 0.1;
    }

    //perfermaces for engineer: level gap => 0.05
    if (
      employee.role === "Engineer" &&
      employee.performance === "above average"
    ) {
      bonusRate += 0.05;
    } else if (
      employee.role === "Engineer" &&
      employee.performance === "below average"
    ) {
      bonusRate -= 0.05;
    }

    // perfermaces for ceo: level gap => 0.1
    if (
      employee.role === "CEO" &&
      employee.performance === "above average"
    ) {
      bonusRate += 0.1;
    } else if (
      employee.role === "CEO" &&
      employee.performance === "below average"
    ) {
      bonusRate -= 0.1;
    }

    // perfermaces for ceo: level gap => 0.2
    if (
      employee.role === "Sales" &&
      employee.performance === "above average"
    ) {
      bonusRate += 0.2;
    } else if (
      employee.role === "Sales" &&
      employee.performance === "below average"
    ) {
      bonusRate -= 0.2;
    }
    let bonus = salary * bonusRate;
    totalBonus += bonus;
  }

  if (totalBonus > 10000) {
    totalBonus = 10000;
  }

  console.log(totalBonus);
}

calculate_sum_of_bonus({
  employees: [
    {
      name: "John",
      salary: "1000USD",
      performance: "above average",
      role: "Engineer",
    },
    {
      name: "Bob",
      salary: 60000,
      performance: "average",
      role: "CEO",
    },
    {
      name: "Jenny",
      salary: "50,000",
      performance: "below average",
      role: "Sales",
    },
  ],
});

//Task 3
function func(...data) {
  let charCount = {};
  let found = false;

  for (let name of data) {
    let char = name[1];

    if (!(char in charCount)) {
      // Need to create an empty object first for char
      charCount[char] = {};
      charCount[char].count = 1;
      charCount[char].fullName = name;
    } else {
      charCount[char].count += 1;
    }
  }

  for (let value of Object.values(charCount)) {
    if (value.count === 1) {
      console.log(value.fullName);
      found = true;
    }
  }

  if (!found) {
    console.log("沒有");
  }
}

func("彭大牆", "王明雅", "吳明"); // print：彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print：林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print：沒有

//Task 4

function get_number(index) {
  let count = 0;
  if (index === 0) {
    console.log(count);
  }
  // If index is even
  if (index % 2 === 0) {
    count = Math.floor(index / 2) * 3;
    console.log(count);
  }
  //  If index is odd
  else {
    count = (Math.floor(index / 2) + 1) * 3 + 1;
    console.log(count);
  }
}

get_number(1); // print 4
get_number(5); // print 10
get_number(10); // print 15

//Task 4 - for recursion exercise

function get_numberRec(index) {
  let count = 0;
  if (index === 0) {
    return count;
  }
  if (index === 1) {
    count = 4;
    return count;
  }
  // If index is even
  if (index % 2 === 0) {
    count = Math.floor(index / 2) * 3;
    return count;
  }
  //  If index is odd
  else {
    count = (Math.floor(index / 2) + 1) * 3 + 1;
    return count;
  }
}

console.log(get_numberRec(1)); // print 4
console.log(get_numberRec(5)); // print 10
console.log(get_numberRec(10)); // print 15
