class SequenceListClass:
    def __init__(self):
        self.SequenceList = []
        return None
    #create SeqList
    def CreateSeqList(self, SeqList):
        self.SequenceList.clear()
        for elem in SeqList:
            self.SequenceList.append(elem)
        return None
    #print SeqList
    def PrintSeqList(self):
        print('SeqList is :')
        if self.SequenceList:
            for elem in self.SequenceList:
                print(elem)
        return None
    #get SeqList length
    def GetSeqListLength(self):
        if self.SequenceList:
            return len(self.SequenceList)
    #get Value by index
    def GetElement(self, index):
        if index > len(self.SequenceList) or index < 0:
            print('out of bound')
            return -1
        return self.SequenceList[index]
    #insert element
    def InsertElement(self, index, value):
        if index >= len(self.SequenceList) or index < 0:
            print('out of bound')
            return -1
        self.SequenceList.insert(index, value)
        return None
    #delet element
    def DeletElement(self, index):
        if index >= len(self.SequenceList) or index < 0:
            print('out of bound')
            return -1
        del self.SequenceList[index]
        return None
    #judge list if is empty
    def IsEmpty(self):
        if len(self.SequenceList) == 0:
            return True
        return False

if __name__ == '__main__':
    seqList = [1, 2, 3, 4, 5, 6, 7, 8]
    SeqList = SequenceListClass()
    SeqList.CreateSeqList(seqList)
    SeqList.PrintSeqList()
    print('SeqList length is', SeqList.GetSeqListLength())

    SeqList.InsertElement(2, 13)
    SeqList.PrintSeqList()

    SeqList.DeletElement(4)
    SeqList.PrintSeqList()



