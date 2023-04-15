/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	l := minDepth(root.Left) + 1
	r := minDepth(root.Right) + 1
	if l == 1 {
		return r
	}
	if r == 1 {
		return l
	}
	return min(l, r)
}

func min(a, b int) int {
	if a <= b {
		return a
	}
	return b
}
