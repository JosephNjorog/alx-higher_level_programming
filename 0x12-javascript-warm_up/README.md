                                                          ### 0x12. JavaScript - Warm up ###
                                                                   JavaScript
                                                      By: Guillaume            Weight: 1
                                                                                                   
                                                                                                     
For this project, this is how i approached the tasks.. stay tunedddddd........


### Task 0: First constant, first print
Just created my first JavaScript script! I defined a constant variable `myVar` with the value "JavaScript is amazing" and used `console.log()` to print it.

```javascript
// 0-javascript_is_amazing.js
const myVar = "JavaScript is amazing";
console.log(myVar);
```

### Task 1: 3 languages
Finished the script to print three lines in different programming languages. Simple `console.log()` statements did the job!

```javascript
// 1-multi_languages.js
console.log("C is fun");
console.log("Python is cool");
console.log("JavaScript is amazing");
```

### Task 2: Arguments
Just wrapped up a script to handle different numbers of arguments. Used `process.argv.length` to determine the number of arguments and printed the appropriate message with `console.log()`.

```javascript
// 2-arguments.js
const args = process.argv.length;
if (args === 2) {
    console.log("No argument");
} else if (args === 3) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
```

### Task 3: Value of my argument
Just wrapped up a script to print the first argument passed to it. Used `process.argv[2]` to access the first argument and printed it using `console.log()`.

```javascript
// 3-value_argument.js
const arg = process.argv[2];
if (!arg) {
    console.log("No argument");
} else {
    console.log(arg);
}
```

### Task 4: Create a sentence
Just completed a script that prints two arguments passed to it in a specific format. Utilized template literals within `console.log()` to achieve this.

```javascript
// 4-concat.js
const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';
console.log(`${arg1} is ${arg2}`);
```

Perfectly done right, let's keep going:

### Task 5: An Integer
I've just finished a script that prints "My number: <first argument converted in integer>" if the first argument can be converted to an integer. Employed `parseInt()` to convert the argument to an integer and checked if it's a valid number using `isNaN()`.

```javascript
// 5-to_integer.js
const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num)) {
    console.log("Not a number");
} else {
    console.log(`My number: ${num}`);
}
```

### Task 6: Loop to languages
Completed a script to print 3 lines using an array of strings and a loop. Avoided using any if/else statement and only used one `console.log()` statement within a loop.

```javascript
// 6-multi_languages_loop.js
const languages = ["C is fun", "Python is cool", "JavaScript is amazing"];
for (let i = 0; i < languages.length; i++) {
    console.log(languages[i]);
}
```


### Task 7: I love C
Just finished a script that prints "C is fun" x times, where x is the first argument of the script. Utilized a loop to print the message multiple times and handled cases where the argument is missing or not a valid number.

```javascript
// 7-multi_c.js
const num = parseInt(process.argv[2]);
if (isNaN(num)) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < num; i++) {
        console.log("C is fun");
    }
}
```

### Task 8: Square
Completed a script that prints a square of a given size using the character 'X'. Utilized nested loops to print the square and handled cases where the size is missing or not a valid number.

```javascript
// 8-square.js
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
    console.log("Missing size");
} else {
    for (let i = 0; i < size; i++) {
        console.log('X'.repeat(size));
    }
}
```


### Task 9: Add
Completed a script that prints the addition of two integers. Defined a function `add(a, b)` to perform the addition and handled cases where one or both of the arguments are missing.

```javascript
// 9-add.js
function add(a, b) {
    return a + b;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])) || 'NaN');
```

### Task 10: Factorial
Just finished a script that computes and prints the factorial of a given integer using recursion. Handled cases where the argument is missing or not a valid number.

```javascript
// 10-factorial.js
function factorial(n) {
    if (isNaN(n)) return 1;
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])) || 'NaN');
```

Great! Let's continue with the next tasks on how i have done  ahaha:

### Task 11: Second biggest!
Just completed a script that searches for the second biggest integer in a list of arguments. Handled cases where there are no arguments, only one argument, or multiple arguments.

```javascript
// 11-second_biggest.js
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
    console.log(0);
} else {
    const sortedArgs = args.sort((a, b) => b - a);
    console.log(sortedArgs[1]);
}
```

### Task 12: Object
Updated a script to replace the value `12` in an object with `89`.

```javascript
// 12-object.js
const myObject = {
  type: 'object',
  value: 12
};
myObject.value = 89;
console.log(myObject);
```


### Task 13: Add file
Implemented a function that returns the addition of two integers, making sure it's visible from outside the script.

```javascript
// 13-add.js
function add(a, b) {
    return a + b;
}

module.exports = {
    add: add
};
```

### Task 14: Const or not const
Modified a script to change the value of a variable `myVar` to `333`.

```javascript
// 100-let_me_const.js
myVar = 333;
```

### Task 15: Call me Moby
Implemented a function that executes a given function a specified number of times, making sure it's visible from outside the script.

```javascript
// 101-call_me_moby.js
function callMeMoby(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction();
    }
}

module.exports = {
    callMeMoby: callMeMoby
};
```

### Task 16: Add me maybe
Created a function that increments a number and calls another function, ensuring it's visible from outside the script.

```javascript
// 102-add_me_maybe.js
function addMeMaybe(number, theFunction) {
    number++;
    theFunction(number);
}

module.exports = {
    addMeMaybe: addMeMaybe
};
```

### Task 17: Increment object
Updated a script by adding a new function `incr` that increments the integer value of an object.

```javascript
// 103-object_fct.js
const myObject = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value++;
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```

That concludes this set of THE PROJECTS tasks . Let me know if you need further assistance in my email or my socials mainly!
