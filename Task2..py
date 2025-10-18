"""
; У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

; 60b90c1c13067a15887e1ae1,Tayson,3
; 60b90c2413067a15887e1ae2,Vika,1
; 60b90c2e13067a15887e1ae3,Barsik,2
; 60b90c3b13067a15887e1ae4,Simon,12
; 60b90c4613067a15887e1ae5,Tessi,5

; Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
"""
def get_cats_info(path):
    cats = []  # список для всех котов
    try:
        with open(path, "r", encoding="utf-8") as file:  
            for line in file:
                line = line.strip()  
                if not line or "," not in line:
                    continue
                try:
                    cat_id, name, age = line.split(",")  
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    print(f"Skipped invalid line: {line}")
    except FileNotFoundError:
        print(f"File not found at path: {path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return cats


# Приклад використання функції
cats_info = get_cats_info("cats.txt")
print(cats_info)

# cats_info = get_cats_info("cats.txt")

# print("[")
# for cat in cats_info:
#     print(f'    {{"id": "{cat["id"]}", "name": "{cat["name"]}", "age": "{cat["age"]}"}},')
# print("]")



