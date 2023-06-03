/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0
    for (let i=0;i<accounts.length;i++){
        let curr = 0
        for(let j=0;j<accounts[i].length;j++)
            curr += accounts[i][j]
        if (curr > max)
            max = curr
    }
    return max
};