"""
#Doctests - são testes que colocamos na docstring das funções/métodos Python

Para rodar um test do doctest:

python -m doctest -v doctestes.py
--------------------------------------------------------------------------------------
 python -m doctest -v doctestes.py
Trying:
    soma(12, 2)
Expecting:
    3
**********************************************************************
# 
Failed example:
    soma(12, 2)
Expected:
    3
Got:
    14
1 items had no tests:
    doctestes
**********************************************************************
1 items had failures:
   1 of   1 in doctestes.soma
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
-----------------------------------------------------------------------------
python -m doctest -v doctestes.py
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctestes
1 items passed all tests:
   1 tests in doctestes.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""

def verdade():
    """Retorna verdade

    >>> verdade()
    True  #Neste caso o teste falha pq foram dados dois espaços após a palavra True (que obviamente não são visiveis)
    """
    return True


