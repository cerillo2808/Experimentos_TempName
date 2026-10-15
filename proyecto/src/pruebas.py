
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
import plotnine


import data.loader as loader

df = loader.get_data()

print(df.describe())
print("DataFrame shape:", df.shape)


# plt.figure(figsize=(10, 6))
# plt.hist(df['Lectura del sensor (mm)'], bins=30, color='blue', alpha=0.7)
# plt.title('Histogram of Lectura del sensor (mm)')
# plt.xlabel('Lectura del sensor (mm)')
# plt.ylabel('Frequency')
# plt.grid(axis='y', alpha=0.75)
# plt.show()
# # plt.savefig('histogram.png')


# ggplot = (plotnine.ggplot(df, plotnine.aes(x='Lectura del sensor (mm)')) +
#           plotnine.geom_histogram(bins=30, fill='blue', alpha=0.7) +
#           plotnine.ggtitle('Histogram of Lectura del sensor (mm)') +
#           plotnine.xlab('Lectura del sensor (mm)') +
#           plotnine.ylab('Frequency') +
#           plotnine.theme_minimal())
# ggplot.show()
# ggplot.save('histogram_plotnine.png')


# df_dist = df['Lectura del sensor (mm)'].value_counts().sort_index()
# print("Distribution of 'Lectura del sensor (mm)':\n", df_dist)

# ggplot_dist = (plotnine.ggplot(df_dist.reset_index(), plotnine.aes(x='index', y='Lectura del sensor (mm)')) +
#                 plotnine.geom_bar(stat='identity', fill='blue', alpha=0.7) +
#                 plotnine.ggtitle('Distribution of Lectura del sensor (mm)') +
#                 plotnine.xlab('Lectura del sensor (mm)') +
#                 plotnine.ylab('Frequency') +
#                 plotnine.theme_minimal())
# ggplot_dist.show()


# dividir el DataFrame en Brillantes, Mates y en mediciones
df_brillantes = df[df['Tipo de pared'] == 'Brillante']
df_mates = df[df['Tipo de pared'] == 'Mate']
df_medicion_10 = df[df['Distancia de referencia (mm)'] == 10]
df_medicion_100 = df[df['Distancia de referencia (mm)'] == 100]
df_medicion_250 = df[df['Distancia de referencia (mm)'] == 250]


# 3 boxplots, uno para cada factor y otro de los dos factores
# df.boxplot(column='Error con signo (mm)', by='Tipo de pared', grid=False, figsize=(10, 8))
# plt.title('Boxplot of Error con signo (mm) by Tipo de pared')
# plt.xlabel('Tipo de pared')
# plt.ylim(-100, 100)
# plt.ylabel('Error con signo (mm)')
# plt.show()
boxplot_tipo_pared = (
    plotnine.ggplot(df, plotnine.aes(x='Tipo de pared', y='Error con signo (mm)')) +
    plotnine.geom_boxplot(fill='lightblue', alpha=0.7) +
    plotnine.stat_summary(
        fun_y='mean',
        geom='crossbar',
        width=0.5,
        color='red'
    ) +
    plotnine.stat_summary(
        fun_y='median',
        geom='crossbar',
        width=0.5,
        color='green'
    ) +
    plotnine.ggtitle('Boxplot of Error con signo (mm) by Tipo de pared') +
    plotnine.xlab('Tipo de pared') +
    plotnine.ylab('Error con signo (mm)') +
    plotnine.ylim(-100, 100) +
    plotnine.theme_minimal()
)

boxplot_tipo_pared.show()

df.boxplot(column='Error con signo (mm)', by='Distancia de referencia (mm)', grid=False, figsize=(10, 8))
plt.title('Boxplot of Error con signo (mm) by Distancia de referencia (mm)')
plt.xlabel('Distancia de referencia (mm)')
plt.ylim(-8, 8)
plt.ylabel('Error con signo (mm)')
plt.ylim(-100, 100)
plt.axhline(y=df['Error con signo (mm)'].mean(), color='r', linestyle='--', label='Media')
plt.legend()
plt.show()

box_distancia_referencia = (plotnine.ggplot(
            df, plotnine.aes(
                x='Distancia de referencia (mm)',
                y='Error con signo (mm)')
            ) +
           plotnine.geom_boxplot(fill='lightgreen', alpha=0.7, notch=True) +
           plotnine.ggtitle('Boxplot of Error con signo (mm) by Distancia de referencia (mm)') +
           plotnine.xlab('Distancia de referencia (mm)') +
           plotnine.ylab('Error con signo (mm)') +
           plotnine.ylim(-100, 100) +
           plotnine.theme_minimal())
box_distancia_referencia.show() 