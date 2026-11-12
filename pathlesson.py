from pathlib import Path



level_name = Path("level_1.txt")

folder_name = "levels"

filepath = folder_name / level_name


print(filepath)

# with open(filepath, "r")as file:
#     print(file.read())


path = Path().cwd()
print(path)

dir_iterator = path.iterdir()
for item in dir_iterator:
    if item.is_dir():
        print("папка",item)
    elif item.suffix == ".py" :
        print("виконуваний файл:", item.name, item.suffix)



save_folder = Path("save")
save_folder.mkdir(exist_ok=True)
if save_folder.exists():
    print("папка збереження знайдена!")
    dir_iterator = save_folder.iterdir()
    for file in dir_iterator:
        save_file_name = save_folder /file.name
        with open(save_file_name, "r") as f:print(f.read())

#linux /home/ubuntu/documents/report.txt
#windows E:\YO\Danil\Platformer\levels\level_1.txt