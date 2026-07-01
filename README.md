# 🌍 Global Climate Trends & Risk Monitor (GCT-RM)

## Descripción

Global Climate Trends & Risk Monitor (GCT-RM) es un proyecto desarrollado en Python cuyo propósito es recopilar, procesar y analizar datos meteorológicos para identificar tendencias climáticas, detectar anomalías y facilitar la toma de decisiones basada en evidencia.

El sistema transforma datos climáticos crudos en información útil mediante procesos automáticos de extracción, limpieza, análisis estadístico y visualización.

---

## Problema

Actualmente existe una gran cantidad de datos meteorológicos disponibles; sin embargo, gran parte de esta información se encuentra en formato crudo y resulta difícil de interpretar para usuarios no especializados.

Esta situación dificulta la identificación de tendencias, la detección de anomalías climáticas y la anticipación de riesgos en sectores como:

* Agricultura
* Logística
* Salud pública

---

## Solución

GCT-RM automatiza el análisis de datos climáticos para:

* Obtener información desde una API meteorológica.
* Limpiar y transformar los datos.
* Detectar tendencias y anomalías.
* Generar visualizaciones claras.
* Facilitar decisiones basadas en evidencia estadística.

---

## Objetivo General

Desarrollar una herramienta que permita monitorear tendencias climáticas mediante el análisis automatizado de datos meteorológicos.

### Objetivos Específicos

* Obtener datos desde una API confiable.
* Validar y limpiar la información.
* Analizar tendencias climáticas.
* Detectar posibles anomalías.
* Visualizar los resultados mediante gráficos.
* Generar información útil para apoyar la toma de decisiones.

---

## Tecnologías utilizadas

* Python 3
* Pandas
* NumPy
* Matplotlib
* Requests
* Jupyter Notebook

---

## Estructura del proyecto

```text
GCT-RM/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── clima_client.py
│   ├── analizador_datos.py
│   ├── visualizador.py
│   └── main.py
│
├── notebooks/
│   └── analisis_final.ipynb
│
├── README.md
└── requirements.txt
```

---

## Flujo de trabajo

1. Obtención de datos desde la API.
2. Validación y limpieza de datos.
3. Procesamiento y análisis estadístico.
4. Generación de visualizaciones.
5. Interpretación de resultados.

---

## Equipo de desarrollo

| Rol                        | Integrante | Responsabilidades                                                                                          |
| -------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------- |
| Arquitecto                 | Felipe     | Diseño de la arquitectura POO, orquestación de `main.py`, gestión del repositorio y `requirements.txt`.    |
| Especialista API/Redes     | Gino       | Implementación de `ClimaClient`, solicitudes HTTP y validación de formatos mediante expresiones regulares. |
| Analista de Datos          | Billie     | Limpieza, transformación y análisis de datos utilizando Pandas.                                            |
| Visualizador               | Fabricio   | Desarrollo de gráficos y visualizaciones para representar los resultados del análisis.                    |
| Documentador               | Dana       | Elaboración del README, Notebook final y `main.py`                 |

---

## Resultados esperados

* Identificación de tendencias climáticas.
* Detección de anomalías meteorológicas.
* Visualizaciones claras para apoyar la toma de decisiones.
* Un flujo automatizado para el análisis de datos climáticos.

---

## Integrantes

* Farro Ochoa, Felipe Roberto
* Dávalos Escalante, Billie Sebastian
* Herrada Peche, Gino Andres
* Alva Guzman, Dana Luciana
* Rodriguez Lopez, Fabricio

## Licencia

Proyecto desarrollado con fines académicos.

## Link del  video 

https://drive.google.com/drive/folders/1wAPzpG-fBQcoalmPnUU9T13WUeJ1mjuD
