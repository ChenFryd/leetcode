/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let init =0
    while(num >0){
        if (num %2 ==0)
            num = num /2
        else
            num = num -1
        init++
    }
    return init
};