
#* El cuadrado de los primeros 100 numeros naturales 

# def run():
#     squares = []
#     for i in range(1, 101):
#         squares.append(i**2)
        
#         print(squares)
    
    
# if __name__ == '__main__':
#     run()
    
#* El cuadrado de los primeros 100 numeros naturales menos los que no son divisibles entre 3
def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    #* List Comprehensions
    
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    #* Reto
    
    squares = [i for i in range(1, 100000) if i % 3 == 0 and i % 4 == 0]
        
    print(squares)
    
    
if __name__ == '__main__':
    run()
    

# #Una forma eficiente de reasolver el reto
# squares = [ i for i in range(1, 100000) if i % 36 == 0]
# print(squares)