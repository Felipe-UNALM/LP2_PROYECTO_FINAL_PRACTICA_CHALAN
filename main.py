# main.py - Proyecto GCT-RM
# Arquitecto: Felipe
# Equipo: Gino, Billie, Fabricio, Dana

from clima_client import ClimaClient
from src.analizador_datos import AnalizadorDatos
from src1.visualizador import Visualizador
from documentador import Documentador


def main():

    print("=== Global Climate Trends & Risk Monitor ===")

    cliente = ClimaClient()
    datos = cliente.obtener_datos()

    analizador = AnalizadorDatos()
    df = analizador.procesar(datos)

    visualizador = Visualizador()
    visualizador.graficar(df)

    documentador = Documentador()
    documentador.generar_reporte(df)

    print("Proceso finalizado correctamente.")


if __name__ == "__main__":
    main()
