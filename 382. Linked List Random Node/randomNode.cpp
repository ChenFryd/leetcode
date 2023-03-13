#include <random>
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
    private:
    ListNode* headNode;
    int counter=0;
public:
    Solution( ListNode* head) {
        headNode = head;
        ListNode* curr = head;
        while (curr != nullptr){
            counter++;
            curr = curr->next;
        }
    }
    
    int getRandom() {
        int num = rand() % counter;
        int nodeCounter=0;
        ListNode* curr = headNode;
        while ( nodeCounter != num){
            nodeCounter++;
            curr = curr->next;
        }
        return curr->val;
    }
};

int main(){
    ListNode* node3 = new ListNode(3);
    ListNode* node2 = new ListNode(2,node3);
    ListNode* node1 = new ListNode(1,node2);
    Solution* solution = new Solution(node1);
    solution->getRandom(); // return 1
    solution->getRandom(); // return 3
    solution->getRandom(); // return 2
    solution->getRandom(); // return 2
    solution->getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
}
/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
