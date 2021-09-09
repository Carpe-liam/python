/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;

const str5 = "a(b)(c";
const expected5 = false;

const str6 = "ab)(c";
const expected6 = false;

const str7 = "abc";
const expected7 = true;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    var countL = 0;
    var countR = 0;
    for(var i=0; i<str.length; i++){
        if(str[i] === "("){
            countL++;
            console.log(countL)
        }
        else if(str[i] === ")"){
            countR ++;
            console.log(countR)
        }
        if (countR > countL){
            return false
        }
    }
    if(countL == countR){
        return true
    }
    else{
        return false
    }
}
console.log(   parensValid(str4)    );




// ***********************************************************************************************
// ***********************************************************************************************
// ***********************************************************************************************


/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str11 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str12 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str13 = "A(1)s[O (n]0{t) 0}k";
const expected13 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var stack = [];
    var open = "({["
    var closerToOpen = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for(let i=0; i<str.length; i++){
        if(open.includes(str[i])){
            stack.push(str[i]);
        }
        else if(str[i] in closerToOpen) {
            if (closerToOpen[str[i]] === stack[stack.length-1]){
                stack.pop()
            }
            else{
                return false
            }
        }
    }
    return stack.length === 0
}

console.log(   bracesValid(str12)   );