import pandas as pd

class AnalizadorDatos:
    """Clase asignada a Billie para limpieza y transformación."""

    def procesar(self, lista_datos):
        print("Transformando lista a DataFrame...")

        # Convertir la lista de diccionarios a DataFrame
        df = pd.DataFrame(lista_datos)

        # Convertir la columna fecha a tipo datetime
        df["fecha"] = pd.to_datetime(df["fecha"])

        # Eliminar filas con valores nulos
        df = df.dropna()

        # Resetear el índice
        df = df.reset_index(drop=True)

        # Agregar columna con temperatura en Fahrenheit
        df["temperatura_f"] = df["temperatura"] * 9/5 + 32

        # Agregar columna indicando si la humedad es alta
        df["humedad_alta"] = df["humedad"] > 70

        print("DataFrame listo.")
        print(df)
        return df