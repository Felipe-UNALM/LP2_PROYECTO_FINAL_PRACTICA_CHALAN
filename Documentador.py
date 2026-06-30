class Documentador:
    """
    Responsable: Dana
    Genera un resumen final del procesamiento de datos.
    """

    def generar_reporte(self, df):
        print("\n===== REPORTE FINAL =====")
        print(f"Total de registros: {len(df)}")

        if "temperatura" in df.columns:
            print(f"Temperatura promedio: {df['temperatura'].mean():.2f} °C")

        if "humedad" in df.columns:
            print(f"Humedad promedio: {df['humedad'].mean():.2f} %")

        print("\nDocumentación preparada:")
        print("✓ README")
        print("✓ Notebook")
        print("✓ Pitch de venta")