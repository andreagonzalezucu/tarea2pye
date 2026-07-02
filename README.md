# Tarea 2 - Probabilidad y Estadística Aplicada

Este repositorio contiene los scripts utilizados para realizar el análisis estadístico descriptivo e inferencial sobre datos de Turismo Emisivo. El trabajo se realiza a partir de una muestra aleatoria de 2000 observaciones almacenada en el archivo `muestra2000.csv`.

## Integrantes

* Andrea González
* Nicolás Lenzuen
* Ramiro López
* Constantino López

## Requisitos

Para ejecutar el proyecto es necesario tener instalado Python 3. Se recomienda utilizar una versión reciente de Python 3.10 o superior.

Las librerías necesarias se encuentran en el archivo `requirements.txt`

## Instalación

1. Clonar o descargar el repositorio.

```
git clone https://github.com/andreagonzalezucu/tarea2pye.git
cd tarea2pye
```

2. Instalar las dependencias.

```
pip install -r requirements.txt
```

## Cómo ejecutar el proyecto

Todos los scripts deben ejecutarse desde la carpeta raíz del repositorio, donde se encuentra `muestra2000.csv`. Esto es importante porque los programas leen el archivo CSV usando una ruta relativa.

## Resultados generados

Al ejecutar los scripts se imprimen resultados en consola y, en algunos casos, se generan archivos de salida como gráficos `.png` o tablas `.csv`. Estos archivos se utilizan como apoyo para el informe final.

## Observaciones

* El archivo `muestra2000.csv` debe estar en la carpeta raíz del proyecto.
* Los scripts fueron desarrollados para ejecutarse de forma independiente.
* Si se ejecutan desde una carpeta distinta, puede aparecer un error de archivo no encontrado (`FileNotFoundError`). En ese caso, se debe verificar que la terminal esté ubicada en la carpeta raíz del repositorio.
* En caso de usar Windows, se recomienda ejecutar los comandos desde PowerShell, CMD o la terminal integrada de Visual Studio Code.

## Librerías utilizadas

* `pandas`: lectura, manipulación y resumen de datos.
* `numpy`: operaciones numéricas auxiliares.
* `matplotlib`: generación de gráficos.
* `scipy`: cálculo de intervalos de confianza, tests de hipótesis, Chi-Cuadrado y regresión lineal.

