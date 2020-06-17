def reduceString(s, l): 
    count = 1; 
    steps = 0; 
    
    for i in range(1,l): 
        if (s[i] is s[i - 1]): 
            count += 1; 
   
        else:  
            steps -=(int)(count / 2); 
   
            count = 1; 
        steps +=(int)(count / 2); 
    return steps; 
  
    
s = "aa";
s= "aaabccddd"
   
l = len(s); 
print (reduceString(s, l)); 
   
