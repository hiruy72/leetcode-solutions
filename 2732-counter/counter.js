/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n;  // store the current count
    
    return function() {
        return count++;  // return current value, then increment
    };
};

// Example usage
const counter = createCounter(10);
console.log(counter()); // 10
console.log(counter()); // 11
console.log(counter()); // 12
