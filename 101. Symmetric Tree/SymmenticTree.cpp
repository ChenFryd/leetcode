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
    bool isSymmetric(TreeNode* root) {
        return isSymTwoNodes(root->left,root->right);
    }
    bool isSymTwoNodes(TreeNode* left, TreeNode* right){
        if (left == nullptr && right != nullptr)
            return false;
        if (right == nullptr && left != nullptr)
            return false;
        if (left == nullptr && right == nullptr)
            return true;
        return (left->val == right->val) && isSymTwoNodes(left->right,right->left) && isSymTwoNodes(left->left,right->right);
    }
};
