documento_agua = """Edificacion, Id,      Tipo, Consumo
casa,         0, domestico, 3.1
departamento, 1, domestico, 11.4
departamento, 2, comercial, 0.1
departamento, 3,   oficina, 10.0
casa,         4,   oficina, 1.0
"""

documento_luz = """Edificacion, Id,      Tipo, Consumo
        casa, A0, domestico, 6.1
departamento, A1, domestico, 22.4
departamento, A2, comercial, 0.2
departamento, A3,   oficina, 20.0
        casa, A4,   oficina, 2.0
    edificio, A5,   oficina, 123.0
"""

precios = {"oficina": 0.8, "comercial": 5.0, "domestico": 1.0}

def main(documento):
    lineas = documento.splitlines()
    total = 0
    headers = [ e.strip() for e in lineas[0].split(",") ]
    for linea in lineas[1:]:
        if len(linea.strip()) > 0:
            fila = linea.split(",")
            values = [ e.strip() for e in fila ]
            ed, id_, tipo, consumo = values
            consumo = float(consumo)
            print(f"ID:{id_},{ed},{tipo},{consumo}")
            escala = 1.0
            if ed == "casa":
                if consumo > 1.0:
                    escala = 5.0
                else:
                    escala = 1.1

                total += 1.0 * escala * precios[tipo] * consumo
            elif ed == "departamento":
                if consumo > 1.0:
                    escala = 3.0
                else:
                    escala = 1.2

                total += 0.5 * escala * precios[tipo] * consumo
            else:
                print("desconocido")
    print(f"Consumo total: {total}")
    return total

if __name__ == "__main__":
    main(documento_agua)
    main(documento_luz)