// Algo 1

/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(A, B) {
    if(A.length == B.length){
        if(A.toLowerCase() == B.toLowerCase()){
            console.log(true);
            for(i=0; i<A.length; i++) {
                if(A[i] == B[i]) {
                    continue
                }
                else{
                    console.log('false in loop')
                    return false
                }
            }
            console.log(true)
            return true
        }
    }
    
}

caseInsensitiveStringCompare(strA1, strB1)
caseInsensitiveStringCompare(strA2, strB2)
caseInsensitiveStringCompare(strA3, strB3)
// Algo 2

/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    var newString = ""
    for(let i=str.length-1; i>=0; i--) {
        newString += str[i];
    }
    return newString;
}

console.log(reverseString(str1));
console.log(reverseString(str2));