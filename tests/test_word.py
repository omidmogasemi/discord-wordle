from Word import Word 
import pytest 

@pytest.mark.parametrize("word,output", [(Word(), "ADIEU")]) 
def test_getword(word, output): 
    word.setWord("Adieu") 
    assert word.getWord() == output 