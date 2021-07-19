import ast

class user:
    def __init__(self):
        self.names=[]
        self.status=[]
        self.start=[]
        self.stop=[]
        self.amount=[]
        self.cague_data=[]
    def save(self):
        open("data.txt","w").close()
        file = open("data.txt","a")
        file.write(str([self.names,self.status,self.start,self.stop,self.amount,self.cague_data]))
    def load(self):
        with open("data.txt") as f:
            lines=str(f.readlines())
            lines=lines[2:-2]
            lines=ast.literal_eval(lines)
            data = lines
            self.names=data[0]
            self.status=data[1]
            self.start=data[2]
            self.stop=data[3]
            self.amount=data[4]
            self.cague_data=data[5]
    def get_data(self,no_string=False):
        if no_string==False:
            return str([self.names,self.status,self.start,self.stop,self.amount,self.cague_data])
        else:
            return [self.names,self.status,self.start,self.stop,self.amount,self.cague_data]
    def get_data_real(self):
        temp=[]
        for i in range(len(self.amount)):
            temp.append(self.amount[i])
        return str(temp)
    def get_cague_moy(self, index):
        temp=0
        for i in range(len(self.cague_data[index])):
            temp=temp+(self.cague_data[index][i][0])
        return temp/(i+1)
    def del_last(self, index):
        self.cague_data[index]=self.cague_data[index][:-1]
        self.amount[index]=self.amount[index]-1
