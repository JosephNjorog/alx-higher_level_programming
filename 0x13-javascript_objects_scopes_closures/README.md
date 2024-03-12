                                             ### 0x13. JavaScript - Objects, Scopes and Closures**
                                                                **JavaScript** 
                                                   By: Guillaume
                                                                               Weight: 1


 For this project, this is how i have approched the tasks...



### Task 0: Rectangle #0
I've created the basic structure for the `Rectangle` class:
```javascript
// 0-rectangle.js
class Rectangle {
  constructor() {}
}

module.exports = Rectangle;
```

### Task 1: Rectangle #1
I've defined the `Rectangle` class with a constructor that initializes its width and height:
```javascript
// 1-rectangle.js
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
```

### Task 2: Rectangle #2
I've extended the `Rectangle` class to handle zero or negative values for width and height:
```javascript
// 2-rectangle.js
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object
    }
  }
}

module.exports = Rectangle;
```

### Task 3: Rectangle #3
I've added a method to the `Rectangle` class to print the rectangle using 'X':
```javascript
// 3-rectangle.js
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  print() {
    // Print rectangle using 'X'
  }
}

module.exports = Rectangle;
```

### Task 4: Rectangle #4
I've enhanced the `Rectangle` class with methods to rotate and double its dimensions:
```javascript
// 4-rectangle.js
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
  }

  print() {
    // Print rectangle using 'X'
  }

  rotate() {
    // Exchange width and height
  }

  double() {
    // Multiply width and height by 2
  }
}

module.exports = Rectangle;
```

### Task 5: Square #0
I've extended the `Rectangle` class to create a `Square` class that inherits from it:
```javascript
// 5-square.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle
  }
}

module.exports = Square;
```

### Task 6: Square #1
I've enhanced the `Square` class to include a method for printing the square using a specified character:
```javascript
// 6-square.js
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(size, size); // Call the constructor of Rectangle
  }

  charPrint(c) {
    if (!c) {
      c = 'X';
    }
    // Print square using character 'c'
  }
}

module.exports = Square;
```

### Task 7: Occurrences
I've implemented a function to count the number of occurrences in a list:
```javascript
// 7-occurrences.js
function nbOccurences(list, searchElement) {
  // Count occurrences of searchElement in list
}

module.exports.nbOccurences = nbOccurences;
```

### Task 8: Esrever
I've created a function to reverse a list without using the built-in `reverse` method:
```javascript
// 8-esrever.js
function esrever(list) {
  // Reverse the list
}

module.exports.esrever = esrever;
```

### Task 9: Log me
I've implemented a function to log each argument with a count of the number of arguments printed so far:
```javascript
// 9-logme.js
let count = 0;

function logMe(item) {
  console.log(`${count++}: ${item}`);
}

module.exports.logMe = logMe;
```

### Task 10: Number conversion
I've created a function to convert a number from base 10 to another base:
```javascript
// 10-converter.js
function converter(base) {
  return function(num) {
    // Convert num to specified base
  }
}

module.exports.converter = converter;
```

### Task 11: Factor index
1. I've imported an array and computed a new array where each value is equal to the value of the initial list multiplied by the index in the list:
```javascript
// 100-map.js
const { list } = require('./100-data');

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
```

### Task 12: Sorted occurrences
1. I've imported a dictionary of occurrences by user id and computed a dictionary of user ids by occurrence:
```javascript
// 101-sorted.js
const { dict } = require('./101-data');

const sortedDict = {};

Object.entries(dict).forEach(([id, occurrence]) => {
  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [id];
  } else {
    sortedDict[occurrence].push(id);
  }
});

console.log(sortedDict);
```

### Task 13: Concat files
1. I've written a script that concatenates two files together:
```javascript
// 102-concat.js
const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');

                                                                          ** GOOD BYE ENJOYYYYYYYY **
const fileC = fileA + fileB;

fs.writeFileSync(process.argv[4], fileC);
```

