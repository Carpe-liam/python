/*
    Sum To One Digit
    Implement a function sumToOne(num)​ that,
    given a number, sums that number’s digits
    repeatedly until the sum is only one digit. Return
    that final one digit result.

    Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

const num4 = 255;
const expected4 = 3

const num5 = "";
const expected4 = 3

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {
    if(num === isNaN){
        return false
    }
    let arr = num.toString().split("");
    console.log(arr);
    var sum = 0;
    if(arr == NaN){
        return false
    }
    if(arr.length > 0){
        for(let i=0; i<arr.length; i++){
            if(arr.length == 1){
                sum = parseInt(arr[0])
                return sum
            }
            else{
                sum += parseInt(arr[i])
            }
        }
        if(sum > 9){
            parseInt(sum)
            sum = sumToOneDigit(sum)
            return sum
        }
    }
    return sum
}

console.log(sumToOneDigit(num5))

// ******************************************************

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/* 
    String Anagrams
    Given a string,
    return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
    Ok to use built in methods
*/

const str1 = "lim";
const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
function generateAnagrams(str, solutions = [], partial = "") {
    if (!str) {
        solutions.push(partial);
    }

    for (let i = 0; i < str.length; i++) {
        const leftSlice = str.slice(0, i);
        const rightSlice = str.slice(i + 1); // skips current letter
        generateAnagrams(leftSlice + rightSlice, solutions, partial + str[i]);
    }
    return solutions;
}