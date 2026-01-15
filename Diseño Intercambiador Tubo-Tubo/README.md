# Diseño de un intercambiador de calor tipo tubo en tubo 

El propósito de este modelo iterador es facilitar el **prediseño de un intercambiador de calor tipo tubo en tubo**, muy usado en industrias en general (ej: bodegas en enfriamiento de mosto, petroquímca en calentamento de crudo, etc.), como criterio de metodo de diseño y calculo del tamaño necesario de un intercambiador, siguiendo la secuencia de cálculo propuesta por el Ing. Cao.

El programa permitirá al usuario introducir diversas variables para el prediseño del intercambiador, y luego ofrecerá la opción de modificar dichas variables. Esto permitirá observar de manera interactiva cómo las alteraciones en la geometría afectan los resultados del diseño, ofreciendo un criterio estandar de calculo para el dimensionamiento, seleccion y/o optimización final del equipo dado.

**POSIBLES MODULOS Y ORGANIZACION PROPUESTA**

a) Módulo de Datos de Entrada:

FUNCIÓN: Manejar todo lo que el usuario ingresa (temperaturas, fluidos, etc.).

CÓMO: Si falta un dato (ej: densidad), este módulo decide si usar CoolProp, una fórmula de gases ideales, o pedírselo al usuario.

EJEMPLO PRÁCTICO: Una lista de "datos obligatorios" y "datos opcionales". Si el usuario no pone la densidad, automáticamente se calcula.

b) Módulo de Simulación (Corazón del Cálculo):

FUNCIÓN: Contiene las fórmulas y cálculos del intercambiador (lo que ya tenés hecho).

DETALLE: Que sea independiente de cómo se ingresaron los datos. Solo recibe números y devuelve resultados.

c) Módulo de Optimización:

FUNCIÓN: Cuando el diseño no cumple, aquí se ajustan parámetros (diámetros, velocidades) y se reinicia la simulación.

TRUCO: Usá un bucle (como un "repetir hasta que funcione") que pruebe combinaciones. Guardá cada intento en una tabla (como un Excel interno) para mostrar después cómo evolucionó el diseño.

d) Módulo de Visualización/Historial:

FUNCIÓN: Graficar resultados y mostrar el histórico de optimizaciones.

EJEMPLO: Después de cada iteración, guardá los parámetros clave y los resultados en una lista. Luego, usá esa lista para hacer gráficos de "cómo mejoró el diseño".

e) Módulo de Interfaz Gráfica (GUI):

FUNCIÓN: Permite cargar datos en campos tipo formulario y elegir opciones (tuberías vs. caños, etc.).
