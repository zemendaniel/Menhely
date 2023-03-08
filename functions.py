import os
def animals(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(animals(dirname))
    return subfolders


def animal_name(str): #'static/animals\\Buksi'
    a = 0
    for i in str[::-1]:
        a += 1
        if i == '\\':
            return str[-a+1:]

def get_the_data(animal_dirs):
    animal_dirs = animals(animal_dirs)
    animal_data = {}
    for animal_dir in animal_dirs:
        directory = animal_dir

        txt = ''
        imgs = []
        description = ''
        meta = ''

        img_formats = ['.png', 'webp', '.gif', '.jpeg', 'jpg']  # ezt ki lehet egészíteni
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".txt"):
                txt = (os.fsdecode(file))
            if filename.endswith(".csv"):
                csv = (os.fsdecode(file))
            for img_format in img_formats:
                if filename.endswith(img_format):
                    imgs.append(os.fsdecode(file))

        with(open(animal_dir + '/' + txt, 'r', encoding='utf-8') as a):
            description = (a.read())

        with(open(animal_dir + '/' + csv, 'r', encoding='utf-8') as a):
            csv = (a.read())
            csv = csv.strip()
            csv = csv.split('\n')
            del csv[0]
            for i in range(len(csv)):
                csv[i] = csv[i].split(';')
            csv = csv[0]

        animal_data[animal_name((animal_dir))] = [imgs,csv,description]

    return animal_data

