/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const res = []
    for (let i=1;i<=n;i++){
        switch(true){
            case i%3===0 && i%5===0:
                res.push("FizzBuzz")
                break
            case i%3===0:
                res.push("Fizz")
                break
            case i%5===0:
                res.push("Buzz")
                break
            default:
                res.push(i.toString());
        }
    }
    return res
};

// Tests
console.log(fizzBuzz(15)) // ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]