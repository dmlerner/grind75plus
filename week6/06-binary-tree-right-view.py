# https://leetcode.com/problems/binary-tree-right-side-view/
# ten fourteen - ten eighteen
def get_right_view(root):
    right_view = []
    last_level = [root]
    next_level = []
    while last_level:
        right_view.append(last_level[-1])
        for l in last_level:
            if l.left:
                next_level.append(l.left)
            if l.right:
                next_level.append(l.right)
        last_level = next_level
        next_level = []

