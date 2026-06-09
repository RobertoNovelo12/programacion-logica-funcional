:- dynamic respuesta/2.

% 1. BASE DE CONOCIMIENTOS: PERFILES DE LAS CARRERAS
% Cada carrera tiene asociado un perfil de intereses y habilidades clave.

% Ingeniería en Sistemas Computacionales
perfil(sistemas_Computacionales, [programacion, logica, tecnologia, resolver_problemas]).

% Ingeniería en Ciencia de Datos
perfil(ciencia_de_datos, [matematicas, estadistica, programacion, analisis_datos]).

% Licenciatura en Administración
perfil(administracion, [liderazgo, organizacion, finanzas, recursos_humanos]).

% Ingeniería Industrial
perfil(industrial, [procesos, optimizacion, logistica, manufactura]).

% Ingeniería en Industrias Alimentarias
perfil(industrias_alimentarias, [quimica, biologia, control_calidad, innovacion_alimentos]).

% Ingeniería en Desarrollo Comunitario
perfil(desarrollo_comunitario, [social, sustentabilidad, proyectos_sociales, trabajo_campo]).

% Ingeniería en Gestión Empresarial
perfil(gestion_empresarial, [negocios, innovacion, estrategias, liderazgo]).


% 2. MOTOR DE INFERENCIA
% Evalúa cuántas características de una carrera coinciden con las del alumno.

% contador_coincidencias(+ListaCarrera, +ListaAlumno, -Puntaje)
contador_coincidencias([], _, 0).
contador_coincidencias([H|T], ListaAlumno, Puntaje) :-
    member(H, ListaAlumno),
!,
    contador_coincidencias(T, ListaAlumno, SubPuntaje),
    Puntaje is SubPuntaje + 1.
contador_coincidencias([_|T], ListaAlumno, Puntaje) :-
    contador_coincidencias(T, ListaAlumno, Puntaje).

% Obtiene el puntaje de coincidencia para una carrera específica basado en el perfil del alumno.
obtener_puntaje_carrera(Carrera, ListaAlumno, Puntaje) :-
    perfil(Carrera, ListaCarrera),
    contador_coincidencias(ListaCarrera, ListaAlumno, Puntaje).

% sugerir_carrera(+ListaAlumno, -CarreraIdeal)
sugerir_carrera(ListaAlumno, CarreraIdeal) :-
    findall(Puntaje-Carrera, obtener_puntaje_carrera(Carrera, ListaAlumno, Puntaje), ListaResultados),
    keysort(ListaResultados, ListaOrdenada),
    reverse(ListaOrdenada, [MaxPuntaje-CarreraIdeal|_]),
    MaxPuntaje > 0.