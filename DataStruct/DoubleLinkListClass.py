HEAD = -9999

class Node:
    """define node"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prior = None

class DoubleLinkListClass:
    """define SingLinkListClass"""

    def __init__(self):
        self.__head = Node(HEAD)
        self.__head.next = None
        self.__head.prior = None

    #judge if is empty
    def IsEmpty(self):
        return self.__head.next == None

    #get list length
    def GetListLength(self):
        cur = self.__head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count

    #prnt list
    def PrintList(self):
        print('link list is :')
        cur = self.__head.next
        while cur != None:
            print(cur.elem)
            cur = cur.next

    #create list
    def CreateList(self, element):
        cur = self.__head
        for ele in element:
            node = Node(ele)
            cur.next = node
            node.prior = cur
            node.next = None
            cur = node

    #insert node
    def InsertNode(self, index, element):
        length = self.GetListLength()
        if index > length or index < 0:
            print('out of bound')
            return None
        cur = self.__head.next
        count = 1
        while count < index:
            cur = cur.next
            count += 1
        node = Node(element)
        cur.next.prior = node
        node.next = cur.next
        cur.next = node
        node.prior = cur

    #delete node
    def DeleteNode(self, index):
        length = self.GetListLength()
        if index > length or index < 0:
            print('out of bound')
            return None
        cur = self.__head
        count = 0
        while count < index:
            cur = cur.next
            count += 1
        node = cur.next
        node.next.prior = cur
        cur.next = node.next
        del node

    #get element location
    def GetElementLocate(self, element):
        cur = self.__head.next
        location = 0
        while cur.elem != element:
            location += 1
            cur = cur.next
        return location



if __name__ == '__main__':
    linkList = DoubleLinkListClass()
    if linkList.IsEmpty():
        print('this is empty list')

    print('list length is : ', linkList.GetListLength())

    nums = [1, 2, 3, 4, 5]

    linkList.CreateList(nums)
    linkList.PrintList()

    linkList.InsertNode(2, 8)
    linkList.PrintList()

    linkList.DeleteNode(3)
    linkList.PrintList()

    print(linkList.GetElementLocate(8))