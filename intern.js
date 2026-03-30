console.log("Hi Everyone");
console.log("Welcome to JavaScript");

console.log("Factorial of 5 is: ");
function factorial(n){
    if(n==0 || n==1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}
console.log(factorial(5));

console.log("Addition of 5 and 10 is: ");
function add(a,b){
    return a+b;
}

console.log(add(5,10));

console.log("Subtraction of 10 and 5 is: ");
function sub(a,b){
    return a-b;
}

console.log(sub(10,5));

console.log("Multiplication of 5 and 10 is: ");
function mul(a,b){
    return a*b;
}

console.log(mul(5,10));

console.log("Division of 10 and 5 is: ");
function div(a,b){
    return a/b;
}       

console.log(div(10,5));