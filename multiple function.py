def average(scores):
    return sum(scores) / len(scores)

def letter_grade(avg):
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"

def main():
    scores = [85, 92, 78]   # example scores
    avg = average(scores)
    grade = letter_grade(avg)
    print("Scores:", scores)
    print("Average:", avg)
    print("Grade:", grade)

main()
