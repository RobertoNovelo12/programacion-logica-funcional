 ## Instrucciones de Ejecución

Sigue estos pasos para configurar el entorno y ejecutar el Sistema de Recomendación en tu equipo.

### Prerrequisitos

Antes de iniciar, asegúrate de tener instalado lo siguiente:
1. *Python 3.x* (Instalado globalmente en el sistema).
2. *SWI-Prolog* (Es indispensable que el ejecutable de Prolog esté agregado a la variable de entorno PATH de tu sistema operativo para que la librería puente funcione correctamente).
3. Un editor de código (como *Visual Studio Code*).

### Configuración del Entorno e Instalación

1. *Estructura de Archivos* Asegúrate de tener los siguientes archivos en la misma carpeta de trabajo:
   * Recomendacion_Carrera.pl (Base de conocimientos y motor de inferencia en Prolog).
   * main.py (Script de Python con la interfaz gráfica en Tkinter) o el nombre que le hayas dado a tu archivo de Python.

2. *Instalación de Dependencias* Abre la terminal integrada en Visual Studio Code (o la consola de tu sistema) y ejecuta el siguiente comando para instalar la librería que conecta Python con Prolog:
   ```bash
   pip install pyswip