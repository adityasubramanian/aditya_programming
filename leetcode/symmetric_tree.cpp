/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) {
            return true; 
        }
        return helper(root->left, root->right); 
    }
    bool helper(TreeNode* rootone, TreeNode* roottwo) {
        if (!rootone && !roottwo) {
            return true; 
        }
        if (!rootone || !roottwo) {
            return false; 
        }
        if (rootone->val != roottwo->val) {
            return false; 
        }
        return helper(rootone->left, roottwo->right) && helper(rootone->right, roottwo->left); 
    }
};



