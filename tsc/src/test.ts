class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function isValidBST(root: TreeNode | null): boolean {
  function _isValid(
    root: TreeNode | null,
    minimum?: number,
    maximum?: number
  ): boolean {
    if (root === null) return true;

    if (minimum !== undefined) {
      if (root.val <= minimum) return false;
    }

    if (maximum !== undefined) {
      if (root.val >= maximum) return false;
    }

    let flags = [];
    if (maximum !== undefined)
      flags.push(_isValid(root.left, minimum, root.val));
    else flags.push(_isValid(root.left, minimum, root.val));

    if (minimum !== undefined)
      flags.push(_isValid(root.right, root.val, maximum));
    else flags.push(_isValid(root.right, root.val, maximum));

    return flags[0] && flags[1];
  }

  return _isValid(root);
}

const root = new TreeNode(32)
root.left = new TreeNode(26)
root.right = new TreeNode(47)
root.right.right = new TreeNode(56)
root.left.left = new TreeNode(19)
root.left.left.right = new TreeNode(27)

console.log(isValidBST(root))

module.exports = undefined