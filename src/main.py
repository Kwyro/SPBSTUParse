import requests
from typing import List
from openpyxl import Workbook

from ORM import Student
from programs import get_list
from codes import codes

def parseStudents(quote) -> List[Student]:
    """Функция для парсинга данных студентов по категориям"""
    students = list()

    for student in quote:
        id = student["code"]
        disciplines_scores = {"Русский язык": student["russian"],
                              "Математика"  : student["math"],
                              "Информатика" : student["it"]}
        priority = student["priority"]
        ia_scores = student["counl_ind"]
        total_scores = student["sum"]
        agreement = student["approval"]

        student = Student(id, disciplines_scores, priority, ia_scores, total_scores, agreement)
        students.append(student)

    return students

def save_to_excel(students: List[Student], quote: int, program: str) -> None:
    quotes = {1: "Бюджетная основа",
              2: "Контракт",
              3: "Особое право",
              4: "Отдельная квота",
              5: "Целевая квота"}

    workbook = Workbook()

    sheet = workbook.active
    sheet.title = quotes[quote]

    sheet.append(["ID", "Общее количество баллов", "Сумма баллов за ЕГЭ", "Дополнительные баллы", "Приоритет", "Согласие"])

    for student in students:
        sheet.append([
            student.id,
            student.total_scores,
            sum(student.disciplines_scores.values()),
            student.ia_scores,
            student.priority,
            student.agreement
        ])

    workbook.save(f"Политех. {program}. {quotes[quote]}.xlsx")

def main() -> None:
    program = input("Напишите код программы: ")
    quote = int(input("Напишитие номер вашей квоты:\n1 (Бюджетная основа)\n2 (Контракт)\n3 (Особое право)\n4 (Отдельная квота)\n5 (Целевой приём)\n"))

    # Получаем необработанный массив с студентами из списка
    students = get_list(quote, program)

    # Получаем список уже с обработанными данными студентов
    students = parseStudents(students)

    # Сохраняем в табличку
    save_to_excel(students, quote, program)

if __name__ == "__main__":
    main()