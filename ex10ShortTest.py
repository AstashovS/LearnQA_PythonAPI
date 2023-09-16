import pytest

def test_input_phrase_length():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, "Фраза не короче 15 символов"