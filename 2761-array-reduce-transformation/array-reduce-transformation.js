/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let acc = init;
    for (let i = 0; i < nums.length; i++) {
        acc = fn(acc, nums[i]);
    }
    return acc;
};

// Example usage
const arr = [1, 2, 3, 4];
const sum = reduce(arr, (acc, curr) => acc + curr, 0);
console.log(sum); // 10
