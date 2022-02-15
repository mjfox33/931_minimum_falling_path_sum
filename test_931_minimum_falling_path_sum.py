import code_931_minimum_falling_path_sum as c

def test_example_1():
    s = c.Solution()
    assert s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]) == 13

def test_example_2():
    s = c.Solution()
    assert s.minFallingPathSum([[-19,57],[-40,-5]]) == -59

def test_21_of_49():
    s = c.Solution()
    assert s.minFallingPathSum([[10,-98,44],[-20,65,34],[-100,-1,74]]) == -218