from Word import Word 
import pytest 

@pytest.mark.parametrize("word,output", [(Word(), "ADIEU")]) 
def test_givenMatchingWord_thenCalcAccuracyIsTrue(word, output): 
    word.setWord("Adieu") 
    res = word.calcAccuracy("Adieu") 
    assert res[0] == True 
    print(res[1]) 