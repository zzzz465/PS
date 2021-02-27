/**
 * Definition for a binary tree node.
 * */
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

 function isSymmetric(root: TreeNode | null): boolean {
    let curr: TreeNode[] = [root]
    let next: TreeNode[] = []
    
    function getNextLevelNodes() {
        next = []
        for(const node of curr) {
            if (node) {
                next.push(node.left)
                next.push(node.right)
            } else {
                next.push(null, null)
            }
        }
        
        curr = next
    }
    
    function isMirror(nodes: TreeNode[]): boolean {
        let lo = 0, hi = nodes.length - 1
        
        while (lo < hi) {
            if (
                (nodes[lo] !== null && nodes[hi] === null) ||
                (nodes[lo] === null && nodes[hi] !== null) ||
                (nodes[lo] !== null && nodes[hi] !== null && nodes[lo].val !== nodes[hi].val)) {
                return false
            } else {
                lo++; hi--;
            }
        }
        
        return true
    }
    
    getNextLevelNodes()
    
    while (curr.some(node => node !== null)) {
        if (isMirror(curr)) {
            getNextLevelNodes()
        } else {
            return false
        }
    }
    
    return true
};