/* 
    Given an array of strings
    return a sum to represent how many times each array item is found (a frequency table)
    Useful methods:
    Object.hasOwnProperty("keyName")
        - returns true or false if the object has the key or not
    Python: key in dict
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];  
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

function frequencyTableBuilder(arr) {
    var dict = {};
    for(var i=0; i<arr.length; i++){
        if(dict[arr[i]] == undefined){
            dict[arr[i]] = 1
        }
        else{
            dict[arr[i]] += 1
        }
    }
    return dict;
}
console.log(frequencyTableBuilder(arr3));



/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */



// ********************************************************

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected1 = 1;

const nums2 = [5, 4, 5];
const expected2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected4 = 1;

function oddOccurrencesInArray(nums) {
    var dict = {};
    for(var i=0; i<nums.length; i++){
        if(dict[nums[i]] == undefined){
            dict[nums[i]] = 1
        }
        else{
            dict[nums[i]] += 1
        }
    }
    for(const key in dict){
    if(dict[key] % 2 != 0){
        return +key
    }
    }
}

console.log(oddOccurrencesInArray(nums4));