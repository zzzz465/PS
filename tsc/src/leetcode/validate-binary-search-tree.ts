/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

 function isValidBST(root: TreeNode | null): boolean {
    function _isValid(root: TreeNode | null, minimum?: number, maximum?: number): boolean {
        if (root === null)
            return true
        
        if (minimum !== undefined) {
            if (root.val <= minimum)
                return false
        }
        
        if (maximum !== undefined) {
            if (root.val >= maximum)
                return false
        }
        
        return _isValid(root.left, minimum, root.val) && _isValid(root.right, root.val, maximum)
    }
    
    return _isValid(root)
};

// inorder-traversal 을 사용하는 방법도 있다!

function isValidBST(root: TreeNode | null): boolean {
    function inorderTraversal(root: TreeNode | null, result: number[]) {
        if (root === null)
            return

        inorderTraversal(root.left, result)
        result.push(root.val)
        inorderTraversal(root.right, result)
    }

    const traversalResult: number[] = []
    inorderTraversal(root, traversalResult)

    for (let i = 0; i < traversalResult.length - 1; i++) {
        if (traversalResult[i] >= traversalResult[i+1])
            return false
    }

    return true
}