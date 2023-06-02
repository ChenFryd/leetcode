/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res = [];
    for(let i = 0; i < arr.length; i++) {
        if(fn(arr[i], i)) {
            res.push(arr[i]);
        }
    }  
    return res;
};  

let arr = [1,2,3,4,5];
arr = filter(arr, (x) => x%2===0);
console.log(arr); // [2,4]