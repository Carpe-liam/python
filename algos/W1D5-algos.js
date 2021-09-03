const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

////////////////////////////////
//          Algo 1            //
////////////////////////////////


function isPalindrome(str) {
    for(var i=0; i<str.length/2;i++) {
        if(str[i] == str.charAt(str.length-1-i)) {
            continue
        }
        else{
            console.log(false)
            return false
        }
    }
    console.log(true)
    return true
}

isPalindrome(str1)
isPalindrome(str4)
isPalindrome(str3)
isPalindrome(str2)


////////////////////////////////
//          Algo 2            //
////////////////////////////////
/* 
    Longest Palindrome
    For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
    Strings longer or shorter than complete words are OK.
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
*/
function isPalindrome(str) {
    for(var i=0; i<str.length/2;i++) {
        if(str[i] == str.charAt(str.length-1-i)) {
            continue
        }
        else{
            return false
        }
    }
    return true
}

const str11 = "what up, daddy-o?";
const expected11 = "dad";

const str12 = "uh, not much";
const expected12 = "u";

const str13 = "Yikes! my favorite racecar erupted!";
const expected13 = "e racecar e";

const str14 = "a1001x20002y5677765z";
const expected14 = "5677765";

const str15 = "a1001x20002y567765z";
const expected15 = "567765";

function longestPalindromicSubstring(str) {
    var longBoi = str[0]
    for(var i =0; i<str.length; i++){
        for(var k = i+1; k<str.length; k++){
            if(isPalindrome(str.substr(i, k-i)) == true && str.substr(i, k-i).length > longBoi.length) {
                longBoi = str.substr(i, k-i)
            }
        }
    }
    console.log(longBoi)
    return longBoi
}

longestPalindromicSubstring(str11)
longestPalindromicSubstring(str12)
longestPalindromicSubstring(str13)
longestPalindromicSubstring(str14)
longestPalindromicSubstring(str15)