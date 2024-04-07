n=int(input())
sentence=[input() for i in range(n)]
# # print(sentence)

def slump(s):
        if len(s)==0:
            return s
        else:
            i=1
            while s[-i]=="F":
                 i+=1
                #  print(i)
            # print(i)
            if s[-i]=="D" or s[-i]=="E":
                #  print(s)
                 return slump(s[:-i])+s[-i:]

def real_slump(s):
     if s[-1]=="G" and slump(s[:-1])==s[:-1]:
          return s         
    
        

def Slimp(k):
    if len(k)==2:
        if k=="AH":
            return k
    elif len(k)>2:
         if k[0]=="A" and k[-1]=="!" and k[1]=="B":  
              return k[0]+k[1]+Slimp(k[2:-1])+k[-1:]
         elif k[0]=="A" and k[-1]=="!":
              if k[1:-1]==real_slump(k[1:-1]):
                   return k[0]+real_slump(k[1:-1])+k[-1:]
    
              
def slurpy(s):
    if s[-1]=="!":
         i=0
         while s[i]!="A":
              i+=1
              return real_slump(s[:i+1]),Slimp(s[i+1,]),"NO"
    elif s[-1]=="H" and s[-2]=="A":
        return real_slump(s[:-2]),Slimp(s[-2:]),"NO"
    elif s[-1]=="G":
         i=1
         while s[-i]!="!":
              i+=1
              return Slimp(s[:-i-1]),real_slump(s[-i-1:]),"YES"
   
         

print("SLURPYS OUTPUT")
for i in sentence:
     print(slurpy(i)[2])
print("END OF OUTPUT")
  
     
     
          
     

        

                  
                        
                