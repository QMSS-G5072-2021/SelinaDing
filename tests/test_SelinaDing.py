from SelinaDing import SelinaDing

def test_cipher():
    result = cipher(text = 'ding', shift = 1, encrypt = True)
    assert(result) == 'ejoh'
