/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {

    for( let i=0; i<arr.length; i++ )
    {
      arr[i]=fn(arr[i],i);
    }
       return arr;
};

let arr = [1,2,3,4,5];
arr = map(arr, (x) => x*2);
console.log(arr); // [2,4,6,8,10]