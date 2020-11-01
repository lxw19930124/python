class SeqenuStackClass:
    """define SeqenuStackClass"""

    def __init__(self, stackList):
        self.__list = stackList

    def Pop(self):
        del self.__list[len(self.__list) - 1]
        return None

    def Push(self, element):
        self.__list[len(self.__list) - 1] = element
        return None

    def Top(self):
        return self.__list[len(self.__list) - 1]

    def PrintStack(self):
        print('stack is :')
        for ele in self.__list:
            print(ele)
        return None

if __name__ == '__main__':
    stackList = [1, 2, 3, 4, 5]
    stack = SeqenuStackClass(stackList)

    stack.PrintStack()

    stack.Pop()
    stack.PrintStack()

    stack.Push(8)
    stack.PrintStack()

    print(stack.Top())