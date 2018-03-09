def main():
    
    cont = "y" # init cont to start loop
    
    # loop while cont is n, convert cont to lower
        
       #get input from user        
        sDegF = 50

        #ERROR HANDLING
        nDegF = float(sDegF)
        
        print("%0.1f Degrees Fahrenheit" % nDegF)
        
        nDegC = ( nDegF - 32) * 5 / 9
        
        print("%0.1f Degrees Centigrade" % nDegC)
        
       # IF - ELSE IF - ELSE Messages
        
        # check if user want to covert another temp
        
if __name__ == "__main__":
    main()
