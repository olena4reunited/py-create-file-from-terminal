from datetime import datetime
import os
import sys


def create_directory(directory_name: str) -> None:
    path = os.path.join(*directory_name)
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode) as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{current_time}\n")

        lines_count = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break

            f.write(f"{lines_count} {content}\n")
            lines_count += 1


def main() -> None:
    args = sys.argv

    if "-d" in args:
        d_index = args.index("-d")
        directory_name = args[d_index + 1:]
        if "-f" in args:
            f_index = args.index("-f")
            file_name = args[f_index + 1]

            directory_name = args[d_index + 1:f_index]
            create_directory(directory_name)

            file_path = os.path.join(*directory_name, file_name)
            create_file(file_path)
        else:
            create_directory(directory_name)
    elif "f" in args:
        f_index = args.index("-f")
        file_name - args[f_index + 1]
        create_file(file_name)


if __name__ == "__main__":
    main()
