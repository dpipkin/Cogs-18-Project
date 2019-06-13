from my_module.my_project_functions import hot_or_iced

def test_hot_or_iced():
    test_input = 63
    test= hot_or_iced(test_input)
    assert test=='iced'
    
test_hot_or_iced