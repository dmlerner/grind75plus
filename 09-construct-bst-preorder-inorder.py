# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# ten thirty nine eleven oh three

 def reconstruct(preorder, inorder):
     if not preorder:
            return

        root_val = preorder[0]

        inorder_root_index = inorder.index(root_val)
        left_inorder = inorder[:inorder_root_index]
        nl = len(left_inorder)
        right_inorder = inorder[inorder_root_index+1:]
        nr = len(right_inorder)

        left_preorder = preorder[1:1+nl]
        right_preorder = preorder[1+nl:]

        left = reconstruct(left_preorder, left_inorder)
        right = reconstruct(right_preorder, right_inorder)

        return TreeNode(root_val, left, right)
