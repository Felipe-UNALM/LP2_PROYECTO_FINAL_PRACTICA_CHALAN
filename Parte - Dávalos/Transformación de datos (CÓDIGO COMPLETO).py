import pandas as pd

class AnalizadorDatos:
    """Clase asignada para limpieza y transformación."""

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

        # Agregar columna indicando si hubo lluvia
        df["llovio"] = df["precipitacion"] > 0

        # Agregar columna indicando si el viento es fuerte
        df["viento_fuerte"] = df["viento"] > 30

        print("DataFrame listo.")
        print(df)
        return df