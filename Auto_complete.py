class Node :
    def __init__(self,value):
        self.value = value
        self.child = []

class TreeOfAutoComplete :
    def __init__(self):
        self.root = Node('root')
    def insert(self,string):
        # string = self.split_string(string)
        self.insert_helper(self.root,string,0)

    def insert_helper(self,node,string,counter):
        if counter >= len(string) :
            return
        flag = 0
        temp = None

        for i in node.child :
            if string[counter] == i.value:
                temp = i
                flag=1
                break
        if not flag :
            temp = Node(string[counter])
            node.child.append(temp)
            self.insert_helper(temp,string,counter+1)
        else :
            self.insert_helper(temp,string,counter+1)

    def split_string(self,string):
        return [i for i in string]

    def autoComplete(self,prefix):
        arr = []
        string = ""
        arr = self.autoComplete_helper(self.root,prefix,0,arr)
        if len((arr)):
            for i in arr[:-1]:
                string = string + str(i.value)

            self.dfs(arr[-1],string)
        else :
            return -1

    def autoComplete_helper(self, node, prefix, counter, arr):
        if counter >= len(prefix):
            return
        flag = 0
        temp = None
        for i in node.child:
            if prefix[counter] == i.value:
                flag = 1
                temp = i
                arr.append(temp)
                break

        if flag:
            self.autoComplete_helper(temp, prefix, counter + 1, arr)

        return arr
    def dfs(self, node, string):
        string = string + node.value
        if node.child == []:
            print(string)
            return
        else:
            counter = 0
            self.dfs(node.child[counter], string)
            if len(node.child) > 1:
                for i in range(1, len(node.child)):
                    self.dfs(node.child[i], string)


tree = TreeOfAutoComplete()
tree.insert("aamohamed")
tree.insert("aabb")
tree.insert("aabc")
tree.insert("aadn")
tree.insert("ackh")
tree.insert("cbms")
tree.insert("kota")
tree.autoComplete("ko")

# print(tree.root.child[0].child[0].child[2].value)
# a="ms"
# print(a[-1])
# print(tree.root.child[0].child[0].child[1].child[0].value)
# a=['b','c','d','a']
# a.sort()
# print(a)
# print(ord('B'))



def help_in_auto_complete(self, obj, string):
    if obj == []:
        return
    print(obj.child)
    string = string + str(obj.value)
    print(string)
    # self.help_in_auto_complete(obj.child,string)
