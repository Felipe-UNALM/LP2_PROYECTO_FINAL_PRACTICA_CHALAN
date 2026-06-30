class Documentador:

    def generar_reporte(self, df):

        print("\n===== REPORTE FINAL =====")

        print(f"Registros analizados : {len(df)}")
        print(f"Temperatura promedio : {df['temperatura'].mean():.2f} °C")
        print(f"Humedad promedio     : {df['humedad'].mean():.2f} %")
        print(f"Días con lluvia      : {df.groupby('fecha')['llovio'].any().sum()}")

        print("\nREADME ✓")
        print("Notebook ✓")
        print("Pitch ✓")