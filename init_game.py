from pathlib import Path
save = Path("save")

if save.exists():
    print("папка збереження знайдена!")

else:
    save.mkdir()

count = 1
asset_folder = Path("Asset")
if asset_folder.is_dir():
    for file in asset_folder.iterdir():
        if file.suffix == ".png" or file.suffix == ".jpg":
            print(count,file)
            count += 1

