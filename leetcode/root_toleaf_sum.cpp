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
    int sumNumbers(TreeNode* root) {
      if (!root) {
          return 0; 
      }  
      return getnext(root,0,0); 
    }
    
    int getnext(TreeNode* root, int number, int total) {
        if (!root) {
            return total; 
        }
        number = number*10 + root-> val; 
        
        if (root->left == NULL && root->right == NULL) {
            total += number; 
            return total; 
        } else {
            total = getnext(root->left, number, total) + getnext(root->right, number, total); 
            return total; 
        }
        
            
    }
    
};