import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(BASE_DIR):
    if root == BASE_DIR:
        continue

    for file in files:
        origin = os.path.join(root, file)
        destination = os.path.join(BASE_DIR, file)

        if os.path.exists(destination):
            name, extension = os.path.splitext(file)
            counter = 1
            while True:
                new_name = f"{name}_{counter}{extension}"
                new_destination = os.path.join(BASE_DIR, new_name)
                if not os.path.exists(new_destination):
                    destination = new_destination
                    break
                counter += 1

        shutil.move(origin, destination)
        print(f"Moved: {origin} -> {destination}")

print("Finished.")
