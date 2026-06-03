% Datos sobre empleados
empleado(juan, 35, ingeniero).
empleado(maria, 28, analista).
empleado(pedro, 40, gerente).

% Crear regla para consultar empleados menores a 30 años

joven(Persona):- empleado(Persona, Edad, _), Edad < 30.

% Pregunta y respuesta
saludo_respuesta(Saludo) :-
    member(Saludo, ["Hola", "Como estas", "Buenos dias", "Que tal"]),
    responder_saludo(Saludo).

responder_saludo("Hola") :-
    write('Hola! En que puedo ayudarte?'), nl.

responder_saludo("Como estas") :-
    write('Estoy bien, gracias por preguntar.'), nl.

responder_saludo("Buenos dias") :-
    write('Buenos dias! Como puedo ayudarte hoy?'), nl.

responder_saludo("Que tal") :-
    write('Todo bien, y tu?'), nl.