# main.py - Proyecto GCT-RM
# Arquitecto: Felipe
# Equipo: Gino, Billie, Fabricio, Dana

class ClimaClient:
    """Clase asignada a Gino para gestionar la API y Regex."""
    def obtener_datos(self):
        print("[Gino] Obteniendo datos de la API...")
        # Gino: Aquí retorna la lista de diccionarios según el contrato
        return [{"fecha": "2026-06-28", "temperatura": 22.5, "humedad": 60}]

class AnalizadorDatos:
    """Clase asignada a Billie para limpieza y transformación."""
    def procesar(self, lista_datos):
        print("[Billie] Transformando lista a DataFrame...")
        # Billie: Aquí convierte lista_datos a pd.DataFrame
        return "DataFrame procesado"

class Visualizador:
    """Clase asignada a Fabricio para la creación de gráficos."""
    def graficar(self, dataframe):
        print("[Fabricio] Generando gráficos profesionales...")
        # Fabricio: Aquí usa matplotlib/seaborn

class Documentador:
    """Clase asignada a Dana para la generación de reportes y el pitch."""
    def generar_reporte(self, df_procesado):
        print("[Dana] Creando README, Notebook y preparando el Pitch...")
        # Dana: Aquí documentarás los resultados finales

def main():
    # Instanciación de módulos
    cliente = ClimaClient()
    analizador = AnalizadorDatos()
    visualizador = Visualizador()
    documentador = Documentador()

    # Flujo de ejecución centralizado
    print("Iniciando GCT-RM...")
    
    raw_data = cliente.obtener_datos()
    df_limpio = analizador.procesar(raw_data)
    visualizador.graficar(df_limpio)
    
    # Dana finaliza el flujo con la documentación
    documentador.generar_reporte(df_limpio)
    
    print("Proceso finalizado con éxito.")

if __name__ == "__main__":
    main()
