class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None  #root node doesn't contain parent Node


    def add_child(self,child):   #after creating a node just adding that node as a child
        child.parent = self
        self.children.append(child)

    #level=0
    def print_tree(self):
        spaces = '  ' * self.get_level()
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                    child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level


def build_product_tree():    #creating node then adding those created node as their child using add_child()
                             #this is a method where we are instantiating object  of TreeNode
    root = TreeNode("product nature-->Electronics:")

    laptop = TreeNode("product category-->Laptop:")
    laptop.add_child(TreeNode("Mac_Book"))
    laptop.add_child(TreeNode("Microsoft_surface"))
    laptop.add_child(TreeNode("Lenovo_Thinkpad"))

    cellphone = TreeNode("product category-->Cell_Phone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("product category-->TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Onida"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__=='__main__':
    object = build_product_tree()
    object.print_tree()
