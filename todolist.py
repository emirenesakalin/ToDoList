# Simple Bilingual To-Do List Application

# Store language texts
languages = {
    "en": {
        "menu_title": "--- To-Do List Menu ---",
        "view_tasks": "View To-Do List",
        "add_task": "Add a Task",
        "delete_task": "Delete a Task",
        "exit": "Exit",
        "empty_list": "Your to-do list is empty!",
        "task_added": "Task '{}' added to the list!",
        "task_deleted": "Task '{}' deleted!",
        "invalid_number": "Invalid task number!",
        "enter_number": "Please enter a valid number!",
        "invalid_choice": "Invalid choice! Please choose a number between 1 and 4.",
        "goodbye": "Exiting the To-Do List. Goodbye!",
        "enter_task": "Enter the task to add: ",
        "enter_task_number": "Enter the task number to delete: ",
    },
    "tr": {
        "menu_title": "--- Yapılacaklar Listesi Menüsü ---",
        "view_tasks": "Yapılacakları Görüntüle",
        "add_task": "Görev Ekle",
        "delete_task": "Görev Sil",
        "exit": "Çıkış",
        "empty_list": "Yapılacaklar listeniz boş!",
        "task_added": "'{}' görevi listeye eklendi!",
        "task_deleted": "'{}' görevi silindi!",
        "invalid_number": "Geçersiz görev numarası!",
        "enter_number": "Lütfen geçerli bir numara girin!",
        "invalid_choice": "Geçersiz seçim! Lütfen 1 ile 4 arasında bir sayı seçin.",
        "goodbye": "Yapılacaklar listesinden çıkılıyor. Güle güle!",
        "enter_task": "Eklemek istediğiniz görevi girin: ",
        "enter_task_number": "Silmek istediğiniz görevin numarasını girin: ",
    }
}

# Language Selection
def choose_language():
    print("Select your language / Dil seçiniz:")
    print("1. English")
    print("2. Türkçe")
    choice = input("Enter your choice (1-2) / Seçiminizi girin (1-2): ")
    return "en" if choice == "1" else "tr"

# Display Menu
def display_menu(lang):
    print(f"\n{lang['menu_title']}")
    print(f"1. {lang['view_tasks']}")
    print(f"2. {lang['add_task']}")
    print(f"3. {lang['delete_task']}")
    print(f"4. {lang['exit']}")

# Display Tasks
def view_tasks(tasks, lang):
    if not tasks:
        print(f"\n{lang['empty_list']}")
    else:
        print(f"\n{lang['view_tasks']}:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Add a Task
def add_task(tasks, lang):
    task = input(f"\n{lang['enter_task']}")
    tasks.append(task)
    print(lang['task_added'].format(task))

# Delete a Task
def delete_task(tasks, lang):
    view_tasks(tasks, lang)
    if tasks:
        try:
            task_number = int(input(f"\n{lang['enter_task_number']}"))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(lang['task_deleted'].format(removed_task))
            else:
                print(lang['invalid_number'])
        except ValueError:
            print(lang['enter_number'])

# Main Program
def main():
    tasks = []  # A list to store tasks
    lang_code = choose_language()  # Language selection
    lang = languages[lang_code]  # Texts from selected language

    while True:
        display_menu(lang)
        choice = input(f"\n{lang['enter_task_number'] if lang_code == 'tr' else 'Enter your choice (1-4): '}")

        if choice == "1":
            view_tasks(tasks, lang)
        elif choice == "2":
            add_task(tasks, lang)
        elif choice == "3":
            delete_task(tasks, lang)
        elif choice == "4":
            print(f"\n{lang['goodbye']}")
            break
        else:
            print(f"\n{lang['invalid_choice']}")

if __name__ == "__main__":
    main()