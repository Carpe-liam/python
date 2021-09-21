function factorial(num){
    num = Math.trunc(num)
    if(num <= 1){
        return 1;
    }
    else{
        return num * factorial(num-1);
    }
}
console.log(factorial(6.8))

function fibonacci(num){
    if(num < 0){
        return "Can't be negative!"
    }
    else if(num ==0 || num == 1){
        return num;
    }
    else{
        return(fibonacci(num-1) + fibonacci(num-2))
    }
}
console.log(fibonacci(10))

// More Efficient
function fibonacciR(num, fibArr=[0, 1], count=0){
    var fibArr
    var count
    if (count >= num){
        return fibArr[num]
    }
    fibArr.push((fibArr[fibArr.length-1] + fibArr[fibArr.length-2]))
    count++
    return fibonacciR(num, fibArr, count)
}