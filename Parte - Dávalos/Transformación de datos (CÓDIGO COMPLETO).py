import pandas as pd

class AnalizadorDatos:
    """
    Responsable: Billie
    Limpieza, transformación y enriquecimiento del DataFrame de clima.
    Recibe la lista de dicts de ClimaClient y entrega un DataFrame
    listo para Fabricio (Visualizador).
    """

    def __init__(self, umbral_humedad: int = 70, umbral_viento: float = 30.0):
        self.umbral_humedad = umbral_humedad  # % — humedad considerada "alta"
        self.umbral_viento  = umbral_viento   # km/h — viento considerado "fuerte"

    def procesar(self, lista_datos: list[dict]) -> pd.DataFrame:

        # ── 1. Validar entrada ──────────────────────────────────────────
        if not lista_datos:
            raise ValueError("[Billie] lista_datos está vacía. Verificar ClimaClient.")

        columnas_requeridas = {"fecha", "hora", "temperatura", "humedad",
                               "viento", "precipitacion"}
        columnas_recibidas  = set(lista_datos[0].keys())
        faltantes = columnas_requeridas - columnas_recibidas
        if faltantes:
            raise KeyError(f"[Billie] Columnas faltantes en los datos: {faltantes}")

        # ── 2. Construir DataFrame ──────────────────────────────────────
        df = pd.DataFrame(lista_datos)
        total_original = len(df)
        print(f"[Billie] Registros recibidos: {total_original}")

        # ── 3. Índice temporal combinando fecha + hora ──────────────────
        df["datetime"] = pd.to_datetime(df["fecha"] + "T" + df["hora"])
        df = df.sort_values("datetime").reset_index(drop=True)

        # ── 4. Tipos correctos ──────────────────────────────────────────
        df["fecha"]         = pd.to_datetime(df["fecha"]).dt.date
        df["temperatura"]   = pd.to_numeric(df["temperatura"],   errors="coerce")
        df["humedad"]       = pd.to_numeric(df["humedad"],       errors="coerce")
        df["viento"]        = pd.to_numeric(df["viento"],        errors="coerce")
        df["precipitacion"] = pd.to_numeric(df["precipitacion"], errors="coerce").fillna(0.0)

        # ── 5. Limpieza selectiva (solo columnas críticas) ──────────────
        criticas = ["temperatura", "humedad", "viento"]
        antes    = len(df)
        df = df.dropna(subset=criticas).reset_index(drop=True)
        eliminados = antes - len(df)
        if eliminados:
            print(f"[Billie] ⚠ {eliminados} filas eliminadas por nulos en columnas críticas.")

        # ── 6. Columnas derivadas ───────────────────────────────────────
        df["temperatura_f"] = (df["temperatura"] * 9 / 5 + 32).round(1)
        df["humedad_alta"]  = df["humedad"]       > self.umbral_humedad
        df["llovio"]        = df["precipitacion"] > 0
        df["viento_fuerte"] = df["viento"]        > self.umbral_viento

        # ── 7. Resumen de limpieza ──────────────────────────────────────
        print(f"[Billie] Registros finales : {len(df)} / {total_original}")
        print(f"[Billie] Rango temporal    : {df['datetime'].min()} → {df['datetime'].max()}")
        print(f"[Billie] Temperatura       : {df['temperatura'].min()}°C – {df['temperatura'].max()}°C")
        print(f"[Billie] Días con lluvia   : {df.groupby('fecha')['llovio'].any().sum()}")
        print("[Billie] DataFrame listo. ✓")

        return df