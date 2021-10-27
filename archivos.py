def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    
#* Agragando "a" en lugar de "w" si no queremos sobrescribir el archivos
    
# def write():
#     names = ["Gabriel", "Juan", "Jimmy", "Rocío"]
#     with open("./archivos/names.txt", "w", encoding="utf-8") as f:
#         for name in names:
#             f.write(name)
#             f.write("\n")

# def run():
#     write()
def run():
    read()


if __name__ == '__main__':
    run()