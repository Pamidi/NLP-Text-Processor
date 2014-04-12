class Node:     
    def __init__(self,ch,flag): # Constructor for Node Object
        self.ch = ch
        self.flag = flag
        self.left = 0
        self.right = 0
        self.center = 0                    

    def Add(self,string,node): # Function to add a string 

        key = string[0] 
        
        if node == 0 :
            node = Node(key,0) 

        if key < node.ch :          
            node.left = node.Add(string,node.left)  

        elif key > node.ch :          
            node.right = node.Add(string,node.right)

        else :  
            if len(string) == 1 :
                node.flag = 1  
            else : node.center = node.Add(string[1:],node.center)
            
        return node    

    def spdfs(self,match,result):  # DFS for Ternary Search Tree
        
        if self.flag == 1 : 
            result.append(match)

            
        if self.center == 0 and self.left == 0 and self.right == 0:            
            return  
                         
        if self.center != 0 :            
            self.center.spdfs(match + self.center.ch,result)
            
            
        if self.right != 0 :         
            self.right.spdfs(match[:-1]+self.right.ch,result)            
            
        if self.left != 0 :            
            self.left.spdfs(match[:-1]+self.left.ch,result)  

    def simple(self,string):  # Function to search a string in the Ternary Search Tree
        temp = self
        i=0
        while temp != 0 :
            if (string[i] < temp.ch) :  temp = temp.left;
            elif(string[i] > temp.ch) : temp = temp.right;
            else :
                i=i+1              
                if(i == len(string)):
                    return temp.flag 
                temp = temp.center

        return 0
            
    
        
    def search(self,string,match,result):
        # Function to implement Auto complete search
    
        if len(string) > 0:
            key = string[0]

            if key < self.ch :
                if(self.left == 0):
                    print("No Match Found")
                    return                            
                self.left.search(string,match,result)

            elif key > self.ch :
                if(self.right == 0):
                    print("Not Match Found")
                    return
                self.right.search(string,match,result)

            else :                
                if len(string) == 1:                                         
                    if self.flag == 1 : 
                        result.append(match+self.ch)
                    if self.center != 0 :
                        self.center.spdfs(match+self.ch+self.center.ch,result)
                    return 1                
                self.center.search(string[1:],match+key,result)                        
            
        else :
            print("Invalid String")
            return
            
def fileparse(filename,node):

    #Parse the Input Dict file and build the TST   
    fd = open(filename)    
    line = fd.readline().strip('\r\n') 
    while line !='':
        
        node.Add(line,node)
        line = fd.readline().strip('\r\n')


if __name__=='__main__':
    
    root = Node('',0)

    # Give the Path to the Dictionary File in
    Path_to_dict = "english_words.txt"
    
    fileparse(Path_to_dict,root)
    
    inp = ''
    while inp !='q':
        inp = raw_input("Enter String : ",)
        result = []
        root.search(inp,'',result) 
        for i in result:
           print i