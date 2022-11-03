x = """Edificacion,Id,Tipo
       casa,         0, domestico
       departamento, 1, domestico
       departamento, 2, comercial
       departamento, 3, oficina
       casa,         4, oficina
    """

precios = {"oficina": 0.8, "comercial": 5.0, "domestico": 1.0}

def main(documento):
    lineas = documento.splitlines()
    total = 0
    for linea in lineas[1:]:
        if len(linea.strip()) > 0:
            fila = linea.split(",")
            ed,id,tipo = [e.strip() for e in fila ]
            print(f"ID:{id},{ed},{tipo}")
            if ed == "casa":
                total += 1.0 * precios[tipo]
            elif ed == "departamento":
                total += 0.5 * precios[tipo]
            else:
                print("desconocido")
    print(f"Consumo total: {total}")


if __name__ == "__main__":
    main(x)