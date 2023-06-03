function listnode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

/**
 * @param {listNode} head
 * @return {listNode}
 */
var middleNode = function (head) {
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};
// Tests
let head = new listnode(1, new listnode(2, new listnode(3, new listnode(4, new listnode(5)))))
console.log(middleNode(head)) // 3