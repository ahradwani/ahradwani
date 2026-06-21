"""

To run Python code you need to copy | paste the code in your  python local editor, 
or just use one of the python online interpreter. Here are some links for 
python online compyler.


https://www.online-python.com/

https://www.programiz.com/python-programming/online-compiler/

https://www.onlinegdb.com/online_python_compilAb


copy and run the code, change to see the efficts.

About:
    This simple code will use * to draw a diamond shape on the screen based on the size the user will enter.

Created in: 21.6.2026
Powered By:  AHRADWANI.fun | Learning Hub.

"""

# This line rows will be the diamond size. 
rows = int(input("Enter number of rows: "))

# This code will draw the upper part of the diamond
for i in range(0, rows):
    for j in range(0, rows - i -1):
        print(" ",end="")
    for j in range (0,i +1):
        print("* ",end="")
    print() 
    
# This part  will draw the second hulf of the diamond.    
for i in range(0, rows -1):
    for j in range(0, i + 1 ):
        print(" ", end="")
    for  j in range(0, rows  -i - 1 ): 
        print("* ", end="")
    print()



        
