## Instrucciones de Ejecución

Sigue estos pasos para configurar el entorno y ejecutar el sistema en tu equipo.

### Prerrequisitos

Antes de iniciar, asegúrate de tener instalado lo siguiente:
1. **Python 3.x** instalado globalmente en el sistema.
2. **SWI-Prolog** instalado. **Importante:** El ejecutable de Prolog debe estar agregado a la variable de entorno `PATH` de tu sistema operativo para que la librería puente funcione correctamente.
3. Un editor de código como **Visual Studio Code**.

### Configuración del Entorno e Instalación

1. **Estructura de Archivos:** Asegúrate de colocar los siguientes archivos dentro de la misma carpeta de trabajo:
   * `Recomendacion_Carrera.pl` (Base de conocimientos y motor de inferencia).
   * `main.py` (Script de Python con la interfaz gráfica de Tkinter).

2. **Instalación de Dependencias:** Abre la terminal integrada de Visual Studio Code (o la consola de tu sistema) y ejecuta el siguiente comando para instalar la librería de conexión:
   ```bash
   pip install pyswip

# Sistema de Recomendación Vocacional

Este proyecto es un sistema experto interactivo diseñado para ayudar a los usuarios a descubrir qué carrera universitaria se adapta mejor a su perfil de intereses, habilidades y aptitudes. El sistema evalúa el perfil del usuario frente a 7 carreras específicas: **Sistemas Computacionales, Ciencia de Datos, Administración, Industrial, Alimentarias, Desarrollo Comunitario y Gestión Empresarial**.

El proyecto utiliza una arquitectura híbrida:
* **Frontend / Interfaz:** Desarrollada en **Python** utilizando **Tkinter** para ofrecer una experiencia visual moderna, limpia e interactiva.
* **Backend / Motor de Inferencia:** Desarrollado en **Prolog** para gestionar la base de conocimientos y realizar las reglas de deducción lógica por medio de conteo de coincidencias.

---

## ¿Cómo Funciona el Sistema?

El flujo de información y procesamiento de datos entre ambos lenguajes funciona de la siguiente manera:

1. **Captura de Datos con Enfoque Funcional (Python):** La interfaz presenta secuencialmente un cuestionario de **6 preguntas**. Cada opción seleccionada por el usuario tiene asociado un grupo de palabras clave o *tokens* (por ejemplo: `["programacion", "tecnologia"]`). Al finalizar, el script unifica todas las selecciones en una lista limpia de características manteniendo principios de inmutabilidad.
2. **El Puente de Comunicación (`pyswip`):** Python transforma esa lista en una estructura compatible con la sintaxis de Prolog (ej. `[programacion, tecnologia, logica]`) y, mediante la librería `pyswip`, ejecuta la consulta dinámica: `sugerir_carrera(ListaUsuario, Carrera)`.
3. **Motor de Inferencia (Prolog):** * El archivo `.pl` contiene los perfiles ideales de las carreras en su base de conocimientos.
   * La regla `contador_coincidencias` compara de forma recursiva los intereses del usuario con los de cada carrera, sumando 1 punto por cada coincidencia exacta.
   * Mediante `findall/3`, `keysort` y `reverse`, Prolog ordena las carreras de mayor a menor puntaje y devuelve a Python únicamente la opción con la máxima compatibilidad (siempre que el puntaje sea mayor a 0).
4. **Despliegue de Resultados:** Python recibe la respuesta, limpia el formato (remueve guiones bajos y añade mayúsculas iniciales) y despliega dinámicamente una tarjeta con las aptitudes detectadas y la carrera recomendada.
