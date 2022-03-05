import tkinter
from tkinter.filedialog import *
class pizzeria:
    def pizza(file):
        hi = open(file,"r")
        list_indi=[]
        

        def find_ingerdiants(list_indi):
        
            for i in hi:
                if len(i)>2:
                    k = i.split()
                    for j in k:
                        if len(j)>2:

                            if j not in list_indi: 
                                list_indi.append(j)
                    
                

        find_ingerdiants(list_indi) 


        score_indi = []
        def score(list_indi):
        
            
            for s in range(0,len(list_indi)):
                
                x=0
                like=0
                dislike=0
                hello = open(file,"r")
                for i in hello:
                
                    x+=1
                    
                    if len(i)>2:
                        k = i.split()
                    
                        for j in k:
                        
                            if list_indi[s] == j:
                                
                                if x%2 == 0:
                                    like+=1
                                    
                                else:
                                    dislike+=1
                        
                
                score_indi.append(like-dislike)
                
            
        score(list_indi)

        str1=""
        sum1=0  
        for i in range(len(score_indi)):
        
            if score_indi[i]>0:
                sum1 = sum1+1
                str1= str1+" "+list_indi[i]
        ans=str(sum1)+str1
        newfile = open("Ans.txt","w+")
        newfile.write(ans)

pizzeria.pizza(file=askopenfilename())
