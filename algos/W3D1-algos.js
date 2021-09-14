/* 
    Given a string that may have extra spaces at the start and the end,
    return a new string that has the extra spaces at the start and the end trimmed (removed)
    do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello there world     ";
const expected2 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    var newStr = ""
    for(var i=0; i<str.length; i++){
        if(str[i] != " "){
            newStr += str[i];
        }
        else if(str[i] == " " && str[i+1] != " " && str[i-1] != " "){
            newStr += str[i]
        }
    }
    return newStr
}
console.log(trim(str2));


/* 
    Balance Index
    Here, a balance point is ON an index, not between indices.
    Return the balance index where sums are equal on either side
    (exclude its own value).
    
    Return -1 if none exist.
*/

const nums1 = [5, 7, 2, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [8, -2, 10, 1, 1, 1, 1, 1, 1];
const expected3 = 2;
/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {
    if(nums.length < 3){
        return -1
    }
    for(var i=0; i<nums.length; i++){
        let sum1 = 0
        let sum2 = 0
        if(i>0){
            for(var j=0; j<i; j++){
                sum1+= nums[j]
            }
            for(var k=nums.length-1; k>i; k--){
                sum2 += nums[k]
            }
            console.log("at i ", i, "sum1 ", sum1, "sum2 ", sum2 )
            if(sum1==sum2){
                return i
            }
        }
    }
}

console.log(balanceIndex(nums1))