/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (root == nullptr)
            return 0;
        if (root->left == nullptr && root->right == nullptr)
            return root->val;
        if (root->left == nullptr && root->right != nullptr)
            return sumNumbersRec(root->right,root->val);
        if (root->left != nullptr && root->right == nullptr)
            return sumNumbersRec(root->left,root->val);
        return sumNumbersRec(root->left,root->val)+sumNumbersRec(root->right,root->val);
    }
    int sumNumbersRec(TreeNode* root, int value){
        if (root == nullptr)
            return 0;
        if (root->left == nullptr && root->right == nullptr)
            return 10*value+root->val;
        if (root->left == nullptr && root->right != nullptr)
            return sumNumbersRec(root->right,10*value+root->val);
        if (root->left != nullptr && root->right == nullptr)
            return sumNumbersRec(root->left,10*value+root->val);
        return sumNumbersRec(root->left,10*value+root->val)+sumNumbersRec(root->right,10*value+root->val);
    }
    
};
