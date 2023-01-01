from fortune_cookie import app

    
def test_call_text_content():
    result = app.call_text()
    assert 0 < len(result)


def test_call_text_type():
    result = app.call_text()
    assert type(result) == str