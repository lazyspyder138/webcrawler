import random

class Node:

    def __init__(self,key,level,index=0):
        self.key = key
        self.index=index
        self.forward = [None]*(level + 1)


class SkipList:
    def __init__(self,max_level,p=.4):
        self.maxLevel = max_level
        self.p = p
        self.head = Node(-1,self.maxLevel)
        self.level = 0
        self.sksize=0

    def randomLevelGenerator(self):
        level = 0
        while random.random() < self.p and level < self.maxLevel:
            level+=1
        return level

    def insertElement(self,key):
        update = [None]*(self.maxLevel+1)
        curr_ptr = self.head

        for i in range(self.level,-1,-1):
            while curr_ptr.forward[i] and curr_ptr.forward[i].key <key:
                curr_ptr=curr_ptr.forward[i]
            update[i]=curr_ptr
        
        curr_ptr  = curr_ptr.forward[0]
        #idx = curr_ptr.index
        idx = update[0].index
        if curr_ptr == None or curr_ptr.key != key:
            rand_level = self.randomLevelGenerator()

            if self.level < rand_level:
                for i in range(self.level+1,rand_level+1):
                    update[i] = self.head
                self.level = rand_level
            
            new_node = Node(key,rand_level,idx+1)
            for i in range(rand_level+1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            print(f"Successfully inserted key {key}.")
            self.sksize+=1

    def find(self,key):
        ptr = self.head

        for i in range(self.level, -1, -1):
            while ptr.forward[i] and ptr.forward[i].key < key:
                ptr = ptr.forward[i]
            
        ptr = ptr.forward[0]

        if ptr and ptr.key == key:
            print("Key Found :",key)
            return 1
        else:
            print("Key not Found!!!")
            return 0
    def findIndex(self,key_index):
        ptr = self.head

        for i in range(self.level, -1, -1):
            while ptr.forward[i] and ptr.forward[i].index < key_index:
                ptr = ptr.forward[i]
            
        ptr = ptr.forward[0]

        if ptr and ptr.index == key_index:
            print("Index:",key_index,",Value:",ptr.key)
        else:
            print("Key not Found!!!")
    
    
    def size(self):
        return self.sksize
            
    
    def display(self):
        print("#############Skip List###############")
        head_ptr  = self.head 
        for level_ind in range(self.level+1):
            print(f"Level: {level_ind}:=>",end=" ")
            node_ptr = head_ptr.forward[level_ind]
            while node_ptr!=None:
                print(node_ptr.key,end=" ")
                node_ptr = node_ptr.forward[level_ind]
            print()
        
        print("#####################################")

    def removeElement(self,key):
        update = [None]*(self.maxLevel+1)

        curr_ptr = self.head

        for i in range(self.level,-1,-1):
            while curr_ptr.forward[i] and curr_ptr.forward[i].key < key:
                curr_ptr=curr_ptr.forward[i]
            update[i] = curr_ptr
        
        curr_ptr = curr_ptr.forward[0]

        if curr_ptr != None  and curr_ptr.key == key:

            for i in range(self.level+1):

                if update[i].forward[i]!=curr_ptr:
                    break
                update[i].forward[i] = curr_ptr.forward[i]

            while self.level > 0 and self.head.forward[self.level] == None:
                self.level -= 1
            print(f"Successfully deleted {key}")
            self.sksize-=1
        else:
            print("No Such Key present. Pls try display your choice")

    def removeElementByIndex(self,key_index):
        update = [None]*(self.maxLevel+1)

        curr_ptr = self.head
        next_ptr = self.head

        for i in range(self.level,-1,-1):
            while curr_ptr.forward[i] and curr_ptr.forward[i].index < key_index:
                curr_ptr=curr_ptr.forward[i]
                next_ptr=next_ptr.forward[i]
            update[i] = curr_ptr
        curr_ptr = curr_ptr.forward[0]
        if curr_ptr!=None:
            next_ptr = curr_ptr.forward[0]
        if curr_ptr != None  and curr_ptr.index == key_index:

            for i in range(self.level+1):

                if update[i].forward[i]!=curr_ptr:
                    break
                update[i].forward[i] = curr_ptr.forward[i]

            while self.level > 0 and self.head.forward[self.level] == None:
                self.level -= 1
            print(f"Successfully deleted {key_index}")
            self.sksize-=1
            while next_ptr!=None:
                next_ptr.index = next_ptr.index-1
                next_ptr = next_ptr.forward[0]
        else:
            print("No Such index present. Pls try display your choice")
        
        
        




if __name__ == "__main__":
    max_level = int(input("Enter Max Level: "))
    p = float(input("Enter p value: "))
    skip_list = SkipList(max_level,p)
    continue_flag=True
    choice = int(input("1.Insert\n2.Delete\n3.Display Keys\n4.Search key\n5.Remove element by index\n6.Search key using index value.\n7.List Size\n0.Exit\nEnter your choice: "))
    while continue_flag:
        continue_flag=False
        if choice == 1:
            key = int(input("Enter your key to insert in skip list:"))
            skip_list.insertElement(key)
            y = input("Enter y/Y to continue: ")
        elif choice == 2:
            key = int(input("Enter your key for deletion: "))
            skip_list.removeElement(key)
            y = input("Enter y to continue: ")
        elif choice == 3:
            skip_list.display()
            y = input("Enter y to continue: ")
        elif choice == 4:
            key = int(input("Enter your key for search: "))
            skip_list.find(key)
            y = input("Enter y to continue: ")
        elif choice == 5:
            key = int(input("Enter your index to delete: "))
            skip_list.removeElementByIndex(key)
            y = input("Enter y to continue: ")
        elif choice == 6:
            key = int(input("Enter your key for search: "))
            skip_list.findIndex(key)
            y = input("Enter y to continue: ")
        elif choice == 7:
            print("List size is:",skip_list.size())
            y = input("Enter y to continue: ")
        else:
            print("Enter valid input!!!!!!")
        continue_flag = (y=="y" or y=="Y")
        if(continue_flag):
            choice = int(input("Enter your choice again: "))