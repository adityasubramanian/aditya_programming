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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res; 
        if (root != NULL) {
        	dfs(root,"", res); 
        return res; 
        }
    }
    void dfs(TreeNode *root, string out, vector<string> &res) {
    	string value = to_string(root->val); 
    	out += value; 
    	if (root->left == NULL && root->right==NULL) {
    		res.push_back(out); 
    	} else {
    		if (root->left != NULL) {
    			dfs(root->left, out +"->", res); 
    		}
    		if (root->right != NULL) {
    			dfs(root->right, out +"->", res); 
    		}
    	}
    }
};