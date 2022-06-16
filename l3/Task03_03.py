file_names = ['file.rar', 'file.txt', 'gmail.rar', 'root.jpg', 'ajax.my.txt', 'ajax.file.rar', 'mail.png', 'task.txt']

def get_extensions(list):
    extensions = []
    for i in list:
        if not extensions.count(i.split('.')[-1]): extensions.append(i.split('.')[-1])
    return extensions

def sort_names(name):
    return(name.split('.')[0])

def names_sort(list):
    extensions = get_extensions(list)
    ext_count = 0
    first_file = 0
    files_count = 0
    i = 0
    while i < len(list):
        if list[i].endswith(extensions[ext_count]):
           files_count += 1
           i += 1
        else:
            if files_count > 1:
                new_list = list[first_file :: first_file + files_count]
                new_list.sort()

            ext_count += 1
            first_file += files_count
            files_count = 0
    return list

# Выше пыталась реализовать сортировку по имени вручную, но потом нашла такое решение.
# Как-то слишком просто получается...


def extension_sort(temp):
    return temp.split('.')[-1]

def sort_file_names(list_names):
    list_names.sort(key=extension_sort)
    list_names.sort(key=lambda x: (x.split('.')[-1], x))
    print(list_names)

sort_file_names(file_names)