#include <vector>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    vector<int> vec;
public:
    TreeNode* sortedListToBST(ListNode* head) {
        linkedListToVector(head);
        return sortedListToBSTrec(0, vec.size()-1);
    }
    TreeNode* sortedListToBSTrec(int start, int end){
        if(start > end)
            return nullptr;
        int mid = start + (end-start)/2;
        if((end - start)%2 != 0)
            mid = mid+1;
        TreeNode* midNode = new TreeNode(vec[mid]);
        midNode->left = sortedListToBSTrec(start, mid-1);
        midNode->right = sortedListToBSTrec(mid+1,end);
        return midNode;
    }
    void linkedListToVector(ListNode* head){
        while (head != nullptr){
            vec.push_back(head->val);
            head = head->next;
        }
    }
};

int main(){
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);
    head->next->next->next->next->next = new ListNode(6);
    head->next->next->next->next->next->next = new ListNode(7);
         
    Solution* sol = new Solution();
    sol->sortedListToBST(head);

    
}
