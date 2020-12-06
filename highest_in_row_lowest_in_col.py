# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
 
# Function to get max element 
def maxelement(arr): 
    # get number of rows and columns 
    no_of_rows = len(arr) 
    #print(arr[0])
    no_of_column = len(arr[0]) 

    final=0
    for i in range(no_of_rows): 
          
        # Initialize max1 to 0 at beginning 
        # of finding max element of each row 
        max1 = 0  
        min1=0
        column=0
        for j in range(no_of_column): 
            if arr[i][j] > max1 : 
                max1 = arr[i][j] 
                print(max1)
                #final=max1
                column=j
     
            
        for k in range(no_of_rows):
                if arr[k][column] >= max1 : 
                    min1=max1
                    print("min "+str(min1))
        if max1==min1:
            final=max1
        else:
            final=-1
        # print maximum element of each row 
        #print("-1") 
    print(final)
    
T = [[4,5,6],[1,3,2],[7,8,9]]
maxelement(T)
