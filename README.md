# Análisis de la Deforestación en la Selva Amazónica

Este proyecto tiene como objetivo cuantificar y analizar la deforestación en el Bosque Nacional Jamanxim mediante el procesamiento de imágenes satelitales. Se implementan y comparan múltiples técnicas de visión artificial para la segmentación de áreas deforestadas a lo largo de una secuencia temporal (2000-2019).

## Descripción

El núcleo del proyecto es el notebook `solution.ipynb`, donde se desarrollan los siguientes métodos de segmentación para identificar la pérdida de cobertura forestal:

*   **Métodos Clásicos:** Umbralización de Otsu, Segmentación por Color (HSV).
*   **Basados en Regiones:** Crecimiento de Regiones (Region Growing).
*   **Clustering:** K-Means.
*   **Superpíxeles:** SLIC (Simple Linear Iterative Clustering).
*   **Basados en Grafos:** GrabCut.
*   **Morfológicos:** Watershed.
*   **Detección de Movimiento:** Sustracción de fondo (MOG2) para análisis temporal.

El análisis permite obtener métricas objetivas sobre la evolución de la deforestación y evaluar la eficacia de cada algoritmo.

## Estructura del Proyecto

*   `solution.ipynb`: Cuaderno principal con todo el código de procesamiento, visualización y análisis.
*   `requirements.txt`: Lista de librerías necesarias para ejecutar el proyecto.
*   `extract_images.py`: Script que extrae la secuencia de imágenes (GIF) desde el documento original (`.docx`).
*   `data.docx`: Documento fuente que contiene las imágenes satelitales originales.
*   `extracted_frames/`: Directorio donde se almacenan las imágenes extraídas para su procesamiento (generado por `extract_images.py`).
*   `out/`: Directorio de salida con los resultados de las máscaras de segmentación.

## Instalación

1.  Clona este repositorio o descarga los archivos.
2.  Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Las principales dependencias son `opencv-python`, `numpy`, `matplotlib`, `scipy` y `Pillow`.

## Uso

1.  **Preparación de datos:** Si no tienes las imágenes en una carpeta, ejecuta `extract_images.py` para extraerlas del documento `.docx` original.
2.  **Ejecución del análisis:** Abre y ejecuta el notebook `solution.ipynb` en un entorno Jupyter (Jupyter Lab, VS Code, Google Colab, etc.).
    *   El notebook cargará las imágenes, aplicará los algoritmos de segmentación y generará gráficas comparativas de las áreas deforestadas.

## Resultados

El proyecto genera visualizaciones comparativas de las máscaras de segmentación obtenidas por cada método, así como gráficas de la evolución temporal del área deforestada estimada en kilómetros cuadrados.
