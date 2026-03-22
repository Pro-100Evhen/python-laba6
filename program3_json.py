import json


def create_students_data():
    """Створює словник з даними студентів."""
    return {
        "Шевченко": ["Іван", "Петрович", 2002],
        "Бондаренко": ["Марія", "Олександрівна", 2001],
        "Коваленко": ["Олена", "Ігорівна", 2003],
        "Ткаченко": ["Андрій", "Васильович", 2000],
        "Мельник": ["Софія", "Романівна", 2002],
        "Кравченко": ["Дмитро", "Сергійович", 2001],
        "Поліщук": ["Наталія", "Миколаївна", 2004],
        "Савченко": ["Оксана", "Юріївна", 2003],
        "Романюк": ["Володимир", "Степанович", 2000],
        "Лисенко": ["Катерина", "Андріївна", 2002]
    }


def write_to_json(data, file_name):
    """Записує словник у JSON-файл."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_from_json(file_name):
    """Зчитує дані з JSON-файлу."""
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    file_name = "students.json"
    students_data = create_students_data()

    write_to_json(students_data, file_name)
    print("Дані записано у файл students.json\n")

    loaded_data = read_from_json(file_name)

    print("Дані, зчитані з JSON-файлу:\n")
    for surname, info in loaded_data.items():
        name, patronymic, birth_year = info
        print(f"{surname} {name} {patronymic}, {birth_year} р.н.")


if __name__ == "__main__":
    main()