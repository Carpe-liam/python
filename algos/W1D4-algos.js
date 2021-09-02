/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 

    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
  */

/////////////////////////////////
//     Christians Answers      //
/////////////////////////////////

function encode(str) {
    if(str.length == 0){
        return str
    }
    let count = 0;
    let newStr = str[0];
    for(let char of str) {
        if (newStr[newStr.length-1] !== char) {
            newStr += count+char;
            count = 0;   
        }
        count++;
    }
    newStr += count;
    return newStr.length < str.length ? newStr : str;
}
console.log((encode("aaaaaaaaaacccbbbbbbbbbbbbbbbbbbbb")));

function decode(str){
    let decoded = "";
    for(let i = 0; i < str.length; i++){
        let char = str[i];
        let numStr = "";
        while(!isNaN(str[i+1])){
            numStr += str[++i];
        }
        decoded += char.repeat(parseInt(numStr));
    }
    return decoded;
}
console.log(decode("a5c3b12"));



































const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

const str5 = "aaaabbcdddaaa";
const expected5 = "a4b2c1d3a3";


//////////////////////////////
//          Algo 1          //  // broken
//////////////////////////////
function encodeStr(str) {
    newStr=[]
    newLis=''
    for(let i=0; i<str.length; i++){
        newStr.push(str[i])
        }
    let count =1
    for(let x=0; x<newStr.length;x++){
        if(newStr[x] == newStr[x+1]) {
            count++ 
            console.log(newStr[x] + newStr[x+1])
        }   
        else if (newStr[x] != newStr[x+1]){
            if(count > 2){
                newLis+= newStr[x]+count
            }
            if(count == 2){
                newLis += newStr[x]
            }
            else{
                newLis+= newStr[x]+count
            }
            count=1
        }
        else{
            console.log(newStr[x])
            count++
        }
    }
    console.log(newLis)
}
encodeStr(str5)

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs only if the
 * character occurs more than two time.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */






/* 
    String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */

function decodeStr(str) {}

var str = "aaabbbbcc";

for (let i = 0; i < str.length; i++) {}

