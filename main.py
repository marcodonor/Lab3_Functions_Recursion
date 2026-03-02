# main.py

import grades

# Student Identity Configuration
LAST_NAME = "DONOR"
STUDENT_ID = "TUPM-25-0294"


SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

# Generate student-unique scores
scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark (grade)

print("=" * 40)
print (f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print (f"Generated Scores: {scores}")
print(f"Average: {round(average, 2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)

from access_control import compute_access_level, validate_access, audit_log

SEED_NUM = 4 # Example: use your actual last digit
FAVORITE_ARTIST = "LAUFEY"
CONTROL_NUM = max(1, SEED_NUM)

@audit_log
def run_authorization():
    level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    threshold = CONTROL_NUM * 5
    decision = validate_access(level, threshold)
    
    # Printing for your Assessment Data table
    print(f"CONTROL_NUM Used: {CONTROL_NUM}")
    print(f"FAVORITE_ARTIST Length: {len(FAVORITE_ARTIST)}")
    print(f"Computed Access Level: {level}")
    print(f"Threshold Applied: {threshold}")
    print(f"Final Decision: {decision}")

if __name__ == "_main_":
    run_authorization()