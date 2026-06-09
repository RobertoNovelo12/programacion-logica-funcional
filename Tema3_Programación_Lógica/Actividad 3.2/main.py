# Alan Alberto Colli Ake - 8B
# Jorge Roberto Novelo Poot - 8B

from tkinter import *
from pyswip import Prolog

# -------------------- PROLOG --------------------
prolog = Prolog()
prolog.consult("Recomendacion_Carrera.pl")

AZUL_PRINCIPAL = "#003366"    
AZUL_HOVER = "#0052a3"       
GRIS_TEXTO = "#4A5568"        
FONDO_APP = "#F7FAFC"        
BLANCO = "#FFFFFF"
VERDE_EXITO = "#2F855A"     

# -------------------- PREGUNTAS --------------------
preguntas = (
    (
        "¿Qué área te llama más la atención?",
        [
            ("Programación y tecnología", ["programacion", "tecnologia"]),
            ("Matemáticas y análisis", ["matematicas", "estadistica"]),
            ("Negocios y administración", ["negocios", "liderazgo"]),
            ("Química y biología", ["quimica", "biologia"])
        ]
    ),
    (
        "¿Qué actividad disfrutas más?",
        [
            ("Resolver problemas lógicos", ["logica", "resolver_problemas"]),
            ("Analizar información", ["analisis_datos"]),
            ("Organizar personas y recursos", ["organizacion"]),
            ("Optimizar procesos", ["optimizacion"])
        ]
    ),
    (
        "¿Qué tipo de trabajo prefieres?",
        [
            ("Oficina y gestión", ["finanzas", "recursos_humanos"]),
            ("Industria y manufactura", ["procesos", "manufactura"]),
            ("Laboratorio y control de calidad", ["control_calidad"]),
            ("Trabajo con comunidades", ["social", "trabajo_campo"])
        ]
    ),
    (
        "¿Qué tema te interesa más?",
        [
            ("Logística", ["logistica"]),
            ("Innovación empresarial", ["innovacion", "estrategias"]),
            ("Innovación en alimentos", ["innovacion_alimentos"]),
            ("Proyectos sociales", ["proyectos_sociales"])
        ]
    ),
    (
        "¿Te interesa la sustentabilidad?",
        [
            ("Sí", ["sustentabilidad"]),
            ("No", [])
        ]
    ),
    (
        "¿Cómo te describirías?",
        [
            ("Líder", ["liderazgo"]),
            ("Analítico", ["analisis_datos"]),
            ("Creativo", ["innovacion"]),
            ("Práctico", ["procesos"])
        ]
    )
)

# -------------------- VARIABLES --------------------
indice = 0
respuestas = []

# -------------------- VENTANA PRINCIPAL --------------------
ventana = Tk()
ventana.title("Sistema de Recomendación Vocacional")
ventana.geometry("850x550")
ventana.configure(bg=FONDO_APP)

# --- CONTENEDORES PRINCIPALES ---
# Encabezado
encabezado = Label(
    ventana,
    text="Sistema de Recomendación de Carrera",
    bg=AZUL_PRINCIPAL,
    fg=BLANCO,
    font=("Segoe UI", 16, "bold"),
    pady=18
)
encabezado.pack(fill="x")

cuerpo_frame = Frame(ventana, bg=FONDO_APP)
cuerpo_frame.pack(fill="both", expand=True, pady=20)

# -------------------- EFECTOS HOVER --------------------
def on_enter(e):
    e.widget.config(bg=AZUL_HOVER)

def on_leave(e):
    e.widget.config(bg=AZUL_PRINCIPAL)

# -------------------- LÓGICA DE FLUJO --------------------
def reiniciar_test():
    global indice, respuestas
    indice = 0
    respuestas = []
    mostrar_pregunta()

def siguiente(opcion):
    global indice
    respuestas.append(opcion)
    indice += 1

    if indice < len(preguntas):
        mostrar_pregunta()
    else:
        mostrar_resultado()

def mostrar_pregunta():

    for widget in cuerpo_frame.winfo_children():
        widget.destroy()

    pregunta, opciones = preguntas[indice]

    # Contador 
    contador = Label(
        cuerpo_frame,
        text=f"PREGUNTA {indice + 1} DE {len(preguntas)}",
        bg=FONDO_APP,
        fg=GRIS_TEXTO,
        font=("Segoe UI", 10, "bold")
    )
    contador.pack(pady=(10, 5))

    # Texto de la pregunta
    pregunta_label = Label(
        cuerpo_frame,
        text=pregunta,
        bg=FONDO_APP,
        fg="#1A202C",
        font=("Segoe UI", 15, "bold"),
        wraplength=700
    )
    pregunta_label.pack(pady=(0, 25))

    # Botones para centrar
    frame_opciones = Frame(cuerpo_frame, bg=FONDO_APP)
    frame_opciones.pack()

    # Botones 
    for texto, caracteristicas in opciones:
        boton = Button(
            frame_opciones,
            text=texto,
            width=42,
            bg=AZUL_PRINCIPAL,
            fg=BLANCO,
            font=("Segoe UI", 11),
            bd=0,
            relief="flat",
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda c=caracteristicas: siguiente(c)
        )
        boton.pack(pady=8)
        
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

def mostrar_resultado():
    for widget in cuerpo_frame.winfo_children():
        widget.destroy()

    # Procesamiento de características de Prolog
    caracteristicas_usuario = [car for grupo in respuestas for car in grupo if car != ""]
    lista_prolog = "[" + ",".join(caracteristicas_usuario) + "]"
    consulta = f"sugerir_carrera({lista_prolog}, Carrera)"
    
    resultado = list(prolog.query(consulta))

    # --- PANTALLA DE RESULTADOS
    tarjeta_resultado = Frame(cuerpo_frame, bg=BLANCO, bd=1, relief="solid", highlightbackground="#E2E8F0", padx=40, pady=30)
    tarjeta_resultado.pack(pady=10, ipady=10)

    if resultado:
        carrera = str(resultado[0]["Carrera"]).replace("_", " ").title()
        
        titulo_res = Label(tarjeta_resultado, text="¡Análisis Concluido!", bg=BLANCO, fg=AZUL_PRINCIPAL, font=("Segoe UI", 16, "bold"))
        titulo_res.pack(pady=(0, 15))

        # Sección de Aptitudes detectadas
        sub_aptitudes = Label(tarjeta_resultado, text="Aptitudes y rasgos detectados:", bg=BLANCO, fg=GRIS_TEXTO, font=("Segoe UI", 10, "bold"))
        sub_aptitudes.pack(anchor="w")

        texto_tags = " • ".join(c.replace("_", " ").title() for c in caracteristicas_usuario)
        tags_label = Label(tarjeta_resultado, text=texto_tags, bg=BLANCO, fg=GRIS_TEXTO, font=("Segoe UI", 11, "italic"), wraplength=550, justify="center")
        tags_label.pack(pady=(5, 25))

        # Sección de Recomendación
        sub_carrera = Label(tarjeta_resultado, text="CARRERA RECOMENDADA:", bg=BLANCO, fg=GRIS_TEXTO, font=("Segoe UI", 10, "bold"))
        sub_carrera.pack()

        carrera_label = Label(tarjeta_resultado, text=carrera, bg=BLANCO, fg=VERDE_EXITO, font=("Segoe UI", 20, "bold"), wraplength=550)
        carrera_label.pack(pady=(5, 10))

    else:
        error_label = Label(tarjeta_resultado, text="No se encontró una carrera que coincida exactamente con tu perfil de respuestas.", bg=BLANCO, fg="#C53030", font=("Segoe UI", 13, "bold"), wraplength=500)
        error_label.pack(pady=30)

    # Botón de reinicio 
    btn_reinicio = Button(
        cuerpo_frame,
        text="Volver a realizar el test",
        bg="#EDF2F7",
        fg=AZUL_PRINCIPAL,
        font=("Segoe UI", 11, "bold"),
        bd=0,
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
        command=reiniciar_test
    )
    btn_reinicio.pack(pady=20)
    
    # Botón secundario de reiniciar
    btn_reinicio.bind("<Enter>", lambda e: e.widget.config(bg="#E2E8F0"))
    btn_reinicio.bind("<Leave>", lambda e: e.widget.config(bg="#EDF2F7"))

# -------------------- INICO
mostrar_pregunta()
ventana.mainloop()