"""The meaning of using GLOBAL within a function is that other elements outside the function will
be affected and given the value called for in the GLOBAL statement"""

"""The disadvantage of using GLOBAL within a function is that
 it might change the value of outer elements, thus leading to wrong results
  in calculations and multiple errors. Thus, the outer elements will have to ba changed as well"""

""" in this code:

x: int = 1
def foo():
print(x)
x = 4
foo()

We will get an error, because python won't know if it should call for the outer 'x' or the inner one.
"""





