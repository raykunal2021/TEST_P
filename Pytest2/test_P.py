import pytest

def sum(a,b):
    return a+b



@pytest.mark.parametrize("input,input1,output",[(2,2,4),(3,4,7)])

def test_add(input,input1,output):

    result=sum(input,input1)
    assert result==output