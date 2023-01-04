"""  
    Autor: Rayo Rodriguez
    Problema: Escribe un código, en Python, que aplane un arreglo de enteros o arreglos de enteros 
              (que puede estar anidado arbitrariamente) a un arreglo plano de enteros.
    Por ej. para el arreglo: 
        [1, [2, [3, [4, 5]]]] 
    Tu código debe devolver:
        [1, 2, 3, 4, 5].
"""

#--- Función principal ---#
def main():
    # Variable para solicitar el valor del array a traves de la consola
    oldArray = input("Coloca el Array que deseas formatear: ")
    response = sortIntegerArray(oldArray)
    if response['statusCode'] != 200:
        print(response['message'])
        main()
    else:
        print(response['message'])

#--- Función donde se ordena el arreglo ---#
def sortIntegerArray(oldArray):
    newArray = []
    # Se valida el tipo de variable que se recibió, esto para no tener ningun problema al momento de hacer el formateo
    if (type(oldArray) == list or type(oldArray) == str):
        # Se convierte la variable recibida a tipo String para poder hacer uso de los metodos de replace y poder
        # eliminar los [], espacios y comillas que existan, despues se utiliza la funcion split para poder separar cada valor por comas.
       
        # Se itera el resultado que obtubimos y se empiezan agregar a la que variable de salida  asi como tambien se convierten nuevamente a enteros
        formatArray = str(oldArray).replace("[", '').replace("]", '').replace("'", '').replace(" ", '').split(",")
        for i in formatArray:
            try:
              newArray.append(int(i))
            except ValueError as VE:
              return ({
                'statusCode': 500,
                'message': f" El siguiente argumento: {str(VE).split(':')[1]} no se puede convertir a entero"
              })
        return ({
            'statusCode': 200, 
            'message': newArray
            })
    return {
      'statusCode': 400,
      'message': "Array no valido. Ejemplo de Array valido: [1,2,3]"
    }


if __name__ == "__main__":
  main()