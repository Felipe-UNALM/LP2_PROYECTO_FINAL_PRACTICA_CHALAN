# clima_client.py - Módulo GCT-RM
# Responsable: Gino
# Rol: Gestión de API (Open-Meteo) + Regex para validación y extracción

import urllib.request
import urllib.parse
import json
import re
from datetime import datetime, timedelta


# ─────────────────────────────────────────────
#  Patrones Regex centralizados
# ─────────────────────────────────────────────
REGEX_FECHA      = re.compile(r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$")
REGEX_COORDENADA = re.compile(r"^-?\d{1,3}\.\d+$")
REGEX_TEMP       = re.compile(r"^-?\d{1,3}(?:\.\d+)?$")   # filtra valores numéricos válidos
REGEX_ISO_TS     = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}$")  # "2026-06-28T14:00"


class ClimaClient:
    """
    Responsable: Gino
    Gestiona la comunicación con la API Open-Meteo y aplica
    regex para validar coordenadas, fechas y limpiar respuestas.

    Contrato de salida → lista de dict con claves:
        fecha        (str)   "YYYY-MM-DD"
        hora         (str)   "HH:MM"
        temperatura  (float) °C
        humedad      (int)   %
        viento       (float) km/h
        precipitacion(float) mm
    """

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    # Ciudad por defecto: Lima, Perú (puede sobreescribirse en __init__)
    DEFAULT_LAT  = -12.0464
    DEFAULT_LON  = -77.0428
    DEFAULT_DIAS = 7          # rango de días a consultar

    def __init__(self, latitud: float = DEFAULT_LAT,
                 longitud: float = DEFAULT_LON,
                 dias: int = DEFAULT_DIAS):
        """
        Args:
            latitud  – latitud decimal  (ej. -12.0464)
            longitud – longitud decimal (ej. -77.0428)
            dias     – cuántos días hacia adelante consultar (1-16)
        """
        self._validar_coordenadas(latitud, longitud)
        self.latitud  = latitud
        self.longitud = longitud
        self.dias     = max(1, min(dias, 16))

    # ──────────────────────────────────────────
    #  Método público principal
    # ──────────────────────────────────────────
    def obtener_datos(self) -> list[dict]:
        """
        Descarga datos horarios de Open-Meteo y los devuelve
        como lista de diccionarios listos para Billie (AnalizadorDatos).

        Returns:
            List[dict]: registros horarios con claves normalizadas.
        """
        print("[Gino] Construyendo URL y consultando Open-Meteo...")
        url       = self._construir_url()
        respuesta = self._hacer_peticion(url)
        datos     = self._parsear_respuesta(respuesta)
        print(f"[Gino] {len(datos)} registros obtenidos y validados. ✓")
        return datos

    # ──────────────────────────────────────────
    #  Construcción de URL
    # ──────────────────────────────────────────
    def _construir_url(self) -> str:
        from datetime import timezone
        ahora        = datetime.now(timezone.utc)
        fecha_inicio = ahora.strftime("%Y-%m-%d")
        fecha_fin    = (ahora + timedelta(days=self.dias - 1)).strftime("%Y-%m-%d")

        params = {
            "latitude":        self.latitud,
            "longitude":       self.longitud,
            "hourly":          "temperature_2m,relativehumidity_2m,windspeed_10m,precipitation",
            "timezone":        "auto",
            "start_date":      fecha_inicio,
            "end_date":        fecha_fin,
            "wind_speed_unit": "kmh",
        }
        url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"
        print(f"[Gino] URL → {url}")
        return url

    # ──────────────────────────────────────────
    #  Petición HTTP (sin dependencias externas)
    # ──────────────────────────────────────────
    def _hacer_peticion(self, url: str) -> dict:
        try:
            with urllib.request.urlopen(url, timeout=10) as resp:
                if resp.status != 200:
                    raise ConnectionError(f"HTTP {resp.status} al consultar Open-Meteo.")
                raw = resp.read().decode("utf-8")
                return json.loads(raw)
        except Exception as exc:
            raise RuntimeError(f"[Gino] Error de red: {exc}") from exc

    # ──────────────────────────────────────────
    #  Parseo + Regex de validación
    # ──────────────────────────────────────────
    def _parsear_respuesta(self, json_resp: dict) -> list[dict]:
        """
        Convierte la respuesta de Open-Meteo en la lista de dicts
        que espera Billie.  Aplica regex para filtrar timestamps
        y valores mal formados.
        """
        hourly = json_resp.get("hourly", {})
        tiempos       = hourly.get("time",                   [])
        temperaturas  = hourly.get("temperature_2m",         [])
        humedades     = hourly.get("relativehumidity_2m",    [])
        vientos       = hourly.get("windspeed_10m",          [])
        precipitacion = hourly.get("precipitation",          [])

        registros = []
        omitidos  = 0

        for i, ts in enumerate(tiempos):
            # ── Regex 1: validar formato timestamp ISO "YYYY-MM-DDTHH:MM" ──
            if not REGEX_ISO_TS.match(str(ts)):
                omitidos += 1
                continue

            fecha, hora = ts.split("T")

            # ── Regex 2: validar formato de fecha ──
            if not REGEX_FECHA.match(fecha):
                omitidos += 1
                continue

            # ── Regex 3: validar que temperatura sea numérica ──
            temp = temperaturas[i] if i < len(temperaturas) else None
            if temp is None or not REGEX_TEMP.match(str(temp)):
                omitidos += 1
                continue

            registros.append({
                "fecha":         fecha,
                "hora":          hora,
                "temperatura":   float(temp),
                "humedad":       int(humedades[i])       if i < len(humedades)      else None,
                "viento":        float(vientos[i])       if i < len(vientos)        else None,
                "precipitacion": float(precipitacion[i]) if i < len(precipitacion) else 0.0,
            })

        if omitidos:
            print(f"[Gino] ⚠ {omitidos} registros omitidos por regex (formato inválido).")

        return registros

    # ──────────────────────────────────────────
    #  Validaciones internas con Regex
    # ──────────────────────────────────────────
    @staticmethod
    def _validar_coordenadas(lat: float, lon: float) -> None:
        """Comprueba que lat/lon sean decimales válidos."""
        for nombre, valor in (("latitud", lat), ("longitud", lon)):
            if not REGEX_COORDENADA.match(str(abs(valor))):
                raise ValueError(
                    f"[Gino] {nombre} inválida: '{valor}'. "
                    "Debe ser un decimal como -12.0464."
                )