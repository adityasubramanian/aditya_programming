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
        void flatten(TreeNode *root) {
            if (root == NULL) {
                return;
            } else {
                while (root != NULL){ // keep checking if the root is not null, because we re-assign the root. 
                    if (root->left != NULL){
                        TreeNode* temp=root->left;
                        while (temp->right != NULL) {
                            temp = temp->right;
                        }
                        temp->right = root->right;
                        root->right = root->left;
                        root->left = NULL;
                    }
                    root=root->right;
                }
            }
        }
};