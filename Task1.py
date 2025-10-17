"""
1.      У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

      Наприклад:

      Alex Korp,3000
      Nikita Borisenko,2000
      Sitarama Raju,1000

2.     Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників."""





def total_salary(path):
      total_salary_sum = 0
      developer_count = 0

      try:
            with open(path, "r", encoding="utf-8") as file:
                  for line in file:
                        line = line.strip()
                        if not line or "," not in line:  # skip empty or invalid lines
                              continue

                        try:
                              name, salary = line.strip().split(",")
                              salary = int(salary)
                              total_salary_sum += salary
                              developer_count += 1
                        except ValueError:
                              print(f"Skipped invalid line: {line}")
      except FileNotFoundError:
            print(f"File not found at path: {path}")
            return (0, 0)

      if developer_count > 0:
            average_salary = total_salary_sum / developer_count
      else:
            average_salary = 0

      return (total_salary_sum, average_salary)

total, average = total_salary("salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")


