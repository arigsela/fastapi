"""
- Modules get used all the time throughout programming
- It helps with creating more files, with unique purposes
    clean maintainable code
"""

import grade_averages_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81
}

grade_service.calculate_homework(homework_assignment_grades)