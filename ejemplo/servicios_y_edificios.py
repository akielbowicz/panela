x = """Edificacion,Id,Tipo
       casa,         0, domestico
       departamento, 1, domestico
       departamento, 2, comercial
       departamento, 3, oficina
       casa,         4, oficina
    """

def main(documento):
    lineas = documento.splitlines()
    for linea in lineas[1:]:
        if len(linea.strip()) > 0:
            fila = linea.split(',')
            ed,id,tipo = [e.strip() for e in fila ]
            print(f"ID:{id},{ed},{tipo}")
            if ed == 'casa':
                print("casa")
            elif ed == 'departamento':
                print("depto")
            else:
                print("desconocido")


if __name__ == "__main__":
    main(x)