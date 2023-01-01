from fortune_cookie import app

    
def test_call_text_content() -> None:
    result = app.call_text()
    assert 0 < len(result)


def test_call_text_type() -> None:
    result = app.call_text()
    assert type(result) == str