# Visualizacion de datos - Fabricio Rodríguez
# Generación de gráficos a partir del DataFrame analizado por Billie

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizador:
    
    def __init__(self):
        sns.set_theme(style="whitegrid")
        plt.rcParams['figure.figsize'] = (11, 5)
        plt.rcParams['axes.titlesize'] = 14
        plt.rcParams['axes.labelsize'] = 11

    def graficar(self, dataframe: pd.DataFrame):

        if dataframe.empty:
            print("[Fabricio] ⚠ Error: El DataFrame está vacío. No hay nada que graficar.")
            return

        print("[Fabricio] Iniciando la generación de gráficos profesionales...")
        self.df = dataframe

        # Gráfico de Líneas: Evolución de la temperatura en el tiempo
        self._grafico_linea_temperatura()

        # Gráfico de Dispersión: Relación Temperatura vs Humedad (con matiz de viento)
        self._grafico_dispersion_clima()

        # Gráfico de Barras / Conteo: Resumen de eventos climatológicos críticos
        self._grafico_barras_riesgos()

        print("gráficos generados")

    def _grafico_linea_temperatura(self):
        plt.figure()
        
        sns.lineplot(
            data=self.df, 
            x='datetime', 
            y='temperatura', 
            color='royalblue', 
            linewidth=2, 
            marker='o', 
            markevery=4, # Evita saturar el gráfico con marcadores en cada hora
            label='Temperatura (°C)'
        )
        
        plt.title('Evolución y Tendencia de la Temperatura Temporal', fontweight='bold', pad=15)
        plt.xlabel('Fecha y Hora')
        plt.ylabel('Temperatura (°C)')
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig('gct_1_tendencia_temperatura.png', dpi=300)
        plt.show()

    def _grafico_dispersion_clima(self):
        plt.figure()
        # Evaluamos correlación Humedad vs Temperatura mapeando los vientos fuertes
        sns.scatterplot(
            data=self.df, 
            x='temperatura', 
            y='humedad', 
            hue='viento_fuerte', 
            palette={True: 'crimson', False: 'cadetblue'},
            s=100, 
            alpha=0.8,
            edgecolor='w'
        )
        
        plt.title('Análisis de Correlación: Temperatura vs Humedad', fontweight='bold', pad=15)
        plt.xlabel('Temperatura (°C)')
        plt.ylabel('Humedad Relativa (%)')
        plt.legend(title='¿Viento Fuerte?', labels=['Sí (>30 km/h)', 'No'])
        plt.tight_layout()
        plt.savefig('gct_2_correlacion_clima.png', dpi=300)
        plt.show()

    def _grafico_barras_riesgos(self):
        plt.figure()
        
        
        resumen_riesgos = {
            'Humedad Alta (>70%)': self.df['humedad_alta'].sum(),
            'Viento Fuerte': self.df['viento_fuerte'].sum(),
            'Horas de Lluvia': self.df['llovio'].sum()
        }
        
        # Crear DataFrame rápido para Seaborn
        df_alertas = pd.DataFrame(list(resumen_riesgos.items()), columns=['Métrica', 'Horas Registradas'])
        
        sns.barplot(
            data=df_alertas, 
            x='Métrica', 
            y='Horas Registradas', 
            hue='Métrica',
            palette='Set2',
            legend=False
        )
        
        plt.title('Monitoreo de Horas Críticas de Riesgo Operativo', fontweight='bold', pad=15)
        plt.xlabel('Indicadores de Riesgo Climático')
        plt.ylabel('Cantidad de Horas Acumuladas')
        plt.tight_layout()
        plt.savefig('gct_3_monitoreo_riesgos.png', dpi=300)
        plt.show()