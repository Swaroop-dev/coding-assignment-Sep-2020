#context manager for openening and closing file
with open('sample_input.txt', 'r') as f:
    f_content = f.readlines()
    
    some,employees=f_content[0].split(":")
    employees=int(employees)
    
    with open('sample_output.txt', 'a') as foutput:
       
        goodies={}
        required_goodies=[]
        
#parsing  data from the file    
        for f_it in f_content[5:]:
            goo,price=f_it.split(":")
            goodies[goo]=int(price)
              
       
        prices=[int(i) for i in list(goodies.values())]
        prices.sort(reverse=True)
        
        actual_length=(len(prices)- employees)

        for i in range(actual_length):
            maxprice=prices[i]
            minprice=prices[employees+i]
            if i == 0:
                difference=maxprice-minprice
                choosen_index=i
            elif (maxprice-minprice)<difference:
                difference=maxprice-minprice
                choosen_index=i
                
        c_price=prices[choosen_index:employees+choosen_index]

        difference=max(c_price)-min(c_price)        
        
        count=0

        for key,value in goodies.items():
            prices[count]
            if int(value) in c_price and count < employees:
                str1=key+": "+str(value)
                required_goodies.append(str1)
                count=count+1
       
#writing neccesary things to ouput file
        foutput.write("Number of employees: "+str(employees))
        foutput.write("\n\n")
        foutput.write("Here the goodies that are selected for distribution are: ")
        foutput.write("\n\n")
        
        for i in required_goodies:
            foutput.write(i)
            foutput.write("\n")
            
            
        foutput.write("\n")    
        foutput.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
        foutput.write("\n\n\n")   
         