    //loop through the list/array
    //for each value, add to list
        //after each value place a separator

/* 
Given an arr and a separator string, output a string of every item in the array separated by the separator.

No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided
*/

//////////////////////////////
//          Algo 1          //
//////////////////////////////

const arr1 = [1, 2, 3];
const separator1 = ", ";
const Aexpected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const Aexpected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const Aexpected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const Aexpected4 = "1";

const arr5 = [];
const separator5 = ", ";
const Aexpected5 = "";


//create function that takes in a list/array & separator
function array_toList(list, sep){
    //create new string
    var str = ""
    // check if list/array contains more than 1 value
    if(list.length > 1){
        //for loop through array/list start & +1
        for(let i=0; i<list.length; i++){
            //add to new string
            str += list[i];
            //add sep to new string
            if(i < (list.length -1)){
                str += sep
            }
        }
    }
    // if only one value, return list
    else if(list.length ==1){
        for(let i=0; i<list.length; i++){
            //add to new string
            str += list[i];
            console.log(str)
            return str
        }
    }
    else{
        console.log("' '")
    }
    console.log(str)
    //return new string
    return str
}

array_toList(arr1, ", ")
array_toList(arr2, "-")
array_toList(arr3, " - ")
array_toList(arr4, ", ")
array_toList(arr5, ", ")



/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {}

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

//////////////////////////////
//          Algo 2          //
//////////////////////////////

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const Bexpected1 = "1, 13-15, 37-38, 70";

const nums2 = [75];
const Bexpected2 = "75";

const nums3 = [];
const Bexpected3 = "";

const nums4 = [75, 76, 'nooo', 80, 81];
//const Bexpected4 = False;

//create function
function abookIndex(nums) {
    //create empty string
    var str =''
    //check if array is empty
    if((nums.length) == []){
        console.log('False');
        //return False
        return false;
    }
    //check if array only has 1 value
    if((nums.length) == 1){
        //return "value"
        str += nums[0]
        return str
    }
    //if 2+ values - for loop through array
    if((num.length) >= 2){
        //check for consecutive ranges
        //set temp values to hold start-stop
        let start = 0
        let stop = 0
        for(let i=0; i<nums.length; i++){
            //if range is consecutive then replace with "start-stop" of range
            if(nums[i] - nums[i+1] == 0){
                start = num[i];
                //if()
            }
            //if not consecutive, place "value (aka page#)"
        }
    }
    //return the string
    //return str
}
//abookIndex(nums2);
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++
// +++++++++++++ END OF TIME ++++++++++++++++++++++++++++
//+++++++++++++++++++++++++++++++++++++++++++++++++++++++

//////////////////////////////////////////
//          Algo 2 Walkthrough          //
//////////////////////////////////////////

function bookIndex(pageNums){
    let formattedPages = ""
    let pageRangeStart = 0;

    for (let i=0; i<pageNums.length; i++) {
        let currentPage = pageNums[i]
        let nextPage = pageNums[i+1]
        let pageRangeStop = i

        //if not consecutive
        if (currentPage +1 !== nextPage) {
            //single page, no range
            formattedPages += currentPage
        }   else{
            formattedPages += `${pageNums[pageRangeStart]}-${pageNums[pageRangeStop]}`
        }
        if (i !== pageNums.length-1) {
            formattedPages += ", "
        }
    
        pageRangeStart = i+1
    }
    console.log(formattedPages)
    return formattedPages
}

bookIndex(nums1)









/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */