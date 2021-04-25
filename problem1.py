with open('sample_input.txt', 'r') as f:
    f_content = f.readlines()
    
    some,employees=f_content[0].split(":")
    employees=int(employees)
    
    with open('sample_output.txt', 'a') as foutput:
       
        goodies={}
        output_list=[]
        

        
        for f in f_content[5:]:
            goo,price=f.split(":")
            goodies[goo]=int(price)
            
       
        
        
        # foutput.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
        prices=[int(i) for i in list(goodies.values())]
        prices.sort(reverse=True)
        
        length_considered=(len(prices)- employees)

        for i in range(length_considered):
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
            print(value)
            if int(value) in c_price and count < employees:
                str1=key+": "+str(value)
                output_list.append(str1)
                count=count+1
       

        foutput.write("Number of employees: "+str(employees))
        foutput.write("\n\n")
        foutput.write("Here the goodies that are selected for distribution are: ")
        foutput.write("\n\n")
        
        for i in output_list:
            foutput.write(i)
            foutput.write("\n")
            
            
        foutput.write("\n")    
        foutput.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(difference))
        foutput.write("\n\n\n")   
         