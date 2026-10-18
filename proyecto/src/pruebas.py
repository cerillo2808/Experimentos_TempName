
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
import plotnine


import data.loader as loader

df = loader.get_data()

print("DataFrame shape:", df.shape)
print(df.describe())
df.info()


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

# Tratar la distancia como un factor para obtener una caja por cada distancia.
df_boxplots = df.copy()
df_boxplots['Distancia de referencia (mm)'] = (
    df_boxplots['Distancia de referencia (mm)'].astype('category')
)



# grafico de boxplot con plotnine para 'Tipo de pared' y 'Error con signo (mm)'
boxplot_tipo_pared = (
    plotnine.ggplot(
        df_boxplots,
        plotnine.aes(x='Tipo de pared', y='Error con signo (mm)')
    ) +
    plotnine.geom_boxplot(fill='lightblue', alpha=0.7) +
    plotnine.stat_summary(
        fun_y=np.mean,
        fun_ymin=np.mean,
        fun_ymax=np.mean,
        geom='crossbar',
        width=0.5,
        color='red'
    ) +
    plotnine.stat_summary(
        fun_y=np.median,
        fun_ymin=np.median,
        fun_ymax=np.median,
        geom='crossbar',
        width=0.5,
        color='green'
    ) +
    plotnine.ggtitle('Error con signo según el tipo de pared') +
    plotnine.xlab('Tipo de pared') +
    plotnine.ylab('Error con signo (mm)') +
    plotnine.coord_cartesian(ylim=(-20, 80)) +
    plotnine.theme_minimal()
)
boxplot_tipo_pared.save('out/imgs/boxplot_tipo_pared.png')

# grafico de boxplot con plotnine para 'Distancia de referencia (mm)' y 'Error con signo (mm)'
box_distancia_referencia = (
    plotnine.ggplot(
        df_boxplots,
        plotnine.aes(
            x='Distancia de referencia (mm)',
            y='Error con signo (mm)'
        )
    ) +
    plotnine.geom_boxplot(fill='lightgreen', alpha=0.7) +
    plotnine.stat_summary(
        fun_y=np.mean,
        fun_ymin=np.mean,
        fun_ymax=np.mean,
        geom='crossbar',
        width=0.5,
        color='red'
    ) +
    plotnine.stat_summary(
        fun_y=np.median,
        fun_ymin=np.median,
        fun_ymax=np.median,
        geom='crossbar',
        width=0.5,
        color='green'
    ) +
    plotnine.ggtitle('Error con signo según la distancia de referencia') +
    plotnine.xlab('Distancia de referencia (mm)') +
    plotnine.ylab('Error con signo (mm)') +
    plotnine.coord_cartesian(ylim=(-20, 80)) +
    plotnine.theme_minimal()
)
box_distancia_referencia.save('out/imgs/box_distancia_referencia.png')

# grafico de densidad con plotnine para 'Error con signo (mm)' para la distancia de referencia de 10 mm
# hist_error_con_signo = (
#     plotnine.ggplot(
#         df_medicion_10,
#         plotnine.aes(x='Error con signo (mm)')
#     ) +
#     plotnine.geom_density(fill='orange', alpha=0.7) +
    
#     plotnine.ggtitle('Densidad de Error con signo (mm)') +
#     plotnine.xlab('Error con signo (mm)') +
#     plotnine.ylab('Frecuencia') +
#     plotnine.theme_minimal()
# )
# hist_error_con_signo.save('out/imgs/hist_error_con_signo.png')
plt.figure(figsize=(10, 6))
df_medicion_10['Error con signo (mm)'].plot(kind='density', bins=30, color='orange', alpha=0.7, linewidth=2)
plt.title('Histogram of Error con signo (mm) for Distancia de referencia = 10 mm')
plt.xlabel('Error con signo (mm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.savefig('out/imgs/hist_error_con_signo.png')