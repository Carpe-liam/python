/* 
    Recursive Sigma
    Input: integer
    Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */

/*
1. given a number
2. create a counter (i) set i = 1
3. create a var sum = 0

// while loop
while loop (conditional) {
    do logic 
    increase i
}

4. create while loop
    4.1 when counter === num (rounded down) -> break
    4.2 add counter to sum 
    4.3 increment counter
5. return sum 
*/

function recursiveSigma(num) {
    // edge cases
    if(num <= 0){
        return 0
    }
    // base case
    return Math.floor(num) + recursiveSigma((Math.floor(num))-1)
    // recursive statement
}

console.log(recursiveSigma(num1));

// ****************************************************************
// ****************************************************************
// ****************************************************************

/* 
    Recursively sum an arr of ints
*/

const nums11 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) {
    // edge cases
    if((nums.length) <= 0){
        return 0
    }
    // base case
    // recursive statement
    return nums.pop() + sumArr(nums)
}
console.log(sumArr(nums11))