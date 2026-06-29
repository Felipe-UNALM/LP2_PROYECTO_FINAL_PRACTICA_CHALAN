Gino (API) → Billie (Datos):

Acuerdo: Gino no puede enviar un archivo de texto cualquiera. Debe entregar una Lista de Diccionarios (formato JSON), donde cada diccionario represente una medición.

Ejemplo de estructura: [{"fecha": "2026-06-28", "temperatura": 22.5, "humedad": 60}, ...]

Billie (Datos) → Fabricio (Visualización):

Acuerdo: Billie recibirá esa lista y la convertirá en un DataFrame de Pandas.

Por qué: Es el estándar en la industria. Fabricio, al usar Pandas, tendrá la vida mucho más fácil para graficar.
