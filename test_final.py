from final import *


def test_get_question():
    print("Hurray, code worked\n\n\n")
    with open("question.txt", "r") as question_fh:
        assert get_question(question_fh) == ([['1', 'What is the square of 13.', 'A: 167', 'B: 169', 'C: 196', 'D: 200'], ['2', 'What is the first prime number.', 'A: 0', 'B: 1', 'C: 2', 'D: 3'], ['3', 'Which is a factor of 8.', 'A: 3', 'B: 2', 'C: 5', 'D: 7'], ['4', 'Which is a composite number.', 'A: 2', 'B: 4', 'C: 3', 'D: 5'], ['5', 'What is the square root of 81.', 'A: 6', 'B: 19', 'C: 9', 'D: 2'], ['6', 'How many numbers are between 10 and 20.', 'A: 8', 'B: 9', 'C: 10', 'D: 11'], ['7', 'What is the first perfect number.', 'A: 4', 'B: 5', 'C: 6', 'D: 7']], 7)
test_get_question()


def test_wrong_answers():
    print("Hurray, code worked\n\n\n")
    assert wrong_answers({1: "wrong", 2: "right", 3: "wrong", 4: "wrong"}) == ([['1', 'What is the square of 13.', 'A: 167', 'B: 169', 'C: 196', 'D: 200'], ['3', 'Which is a factor of 8.', 'A: 3', 'B: 2', 'C: 5', 'D: 7'], ['4', 'Which is a composite number.', 'A: 2', 'B: 4', 'C: 3', 'D: 5']], 3)
test_wrong_answers()
    

def test_know_highscore():
    print("Hurray, code worked\n\n\n")
    assert know_highscore("emmanuel", 30) == {'okafor': '35', 'emmanuel': '30', 'chinonso': '25'}
    assert know_highscore("sam", 15) == {'okafor': '35', 'emmanuel': '30', 'chinonso': '25'}
    
test_know_highscore()

def test_choose_retake_question():
    print("\nHurray, code worked\n\n\n")
    assert choose_question([['1', 'What is the square of 13.', 'A: 167', 'B: 169', 'C: 196', 'D: 200'], ['2', 'What is the first prime number.', 'A: 0', 'B: 1', 'C: 2', 'D: 3'], ['3', 'Which is a factor of 8.', 'A: 3', 'B: 2', 'C: 5', 'D: 7'], ['4', 'Which is a composite number.', 'A: 2', 'B: 4', 'C: 3', 'D: 5']], 4 ) != {}
test_choose_retake_question()

def test_choose_question():
    print("\n\n\n\nHurray, code worked\n\n\n")
    assert choose_question([['1', 'What is the square of 13.', 'A: 167', 'B: 169', 'C: 196', 'D: 200'], ['2', 'What is the first prime number.', 'A: 0', 'B: 1', 'C: 2', 'D: 3'], ['3', 'Which is a factor of 8.', 'A: 3', 'B: 2', 'C: 5', 'D: 7'], ['4', 'Which is a composite number.', 'A: 2', 'B: 4', 'C: 3', 'D: 5'], ['5', 'What is the square root of 81.', 'A: 6', 'B: 19', 'C: 9', 'D: 2'], ['6', 'How many numbers are between 10 and 20.', 'A: 8', 'B: 9', 'C: 10', 'D: 11'], ['7', 'What is the first perfect number.', 'A: 4', 'B: 5', 'C: 6', 'D: 7']], 7) != {}
test_choose_question()
    