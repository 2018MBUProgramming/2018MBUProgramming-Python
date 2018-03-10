def main():
    
    # Loop if user wants to convert another temp
    
    # get input from user        
    sDegF = 50

    # Error Handling
    
    nDegF = float(sDegF)
    
    print("%0.1f Degrees Fahrenheit" % nDegF)
    
    nDegC = ( nDegF - 32) * 5 / 9
    
    print("%0.1f Degrees Centigrade" % nDegC)
    
    # IF - ELSE IF - ELSE Messages
    
if __name__ == "__main__":
    main()
