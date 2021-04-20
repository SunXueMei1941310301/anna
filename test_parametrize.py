import pytest;
def add_funtion(a,b):
    return a+b
#参数化，参数加别名，ids
@pytest.mark.parametrize("a,b,expected",
                         [(3,5,8),
                          (-1,-2,-3),
                          (100000,100000,200000),
                          ],ids=["int","minus","bigint"])
def test_add(a,b,expected):
    assert add_funtion(a,b)==expected
#参数可以组合
@pytest.mark.parametrize("a",[0,1])
@pytest.mark.parametrize("b",[-2,10000])
def test_foo(a,b):
    print("测试数据组合：a->%s,b->%s"%(a,b))