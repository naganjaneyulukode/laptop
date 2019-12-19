#Importing subpackage
#import pckg.spkg.sm1
##import pckg.spkg.sm2
#Accessing the code pckg.spkg.sm1.sf1m1()
#pckg.spkg.sm2.sf1m2()

#Length of import is more. So we can avoid this by bringing needed 
#functions/code to packages namespace. For this we use
#special file "__init__.py". Instead of importing the code
#here we import this in the __init__.py making it accesssible from 
#packages namespace as below. See __init__.py code to understand how

# from pckg import f1m1
# from pckg import f1m2
# from pckg import var1

# print(var1)
# f1m1()
# f1m2()
