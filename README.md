# Autómata Finito Determinista (AFD) en Python

## 1. Descripción General

Este proyecto implementa un **Autómata Finito Determinista (AFD)** en Python para el reconocimiento de un lenguaje formal sobre el alfabeto binario.

El sistema procesa cadenas binarias almacenadas en un archivo de texto y determina, para cada una, si pertenece o no al lenguaje definido por el autómata.

La implementación respeta la definición formal de un AFD como una 5-tupla:

M = (Q, Σ, δ, q0, F)

donde:

- Q  → Conjunto finito de estados  
- Σ  → Alfabeto  
- δ  → Función de transición  
- q0 → Estado inicial  
- F  → Conjunto de estados de aceptación  

---

## 2. Definición Formal del Autómata

### 2.1 Conjunto de Estados (Q)

Q = { q0, q1, qd }

- q0 → Estado inicial  
- q1 → Estado de aceptación  
- qd → Estado trampa  

---

### 2.2 Alfabeto (Σ)

Σ = { 0, 1 }

---

### 2.3 Estado Inicial

q0

---

### 2.4 Estados de Aceptación

F = { q1 }

---

### 2.5 Función de Transición (δ)

La función de transición está definida para todo Q × Σ, garantizando determinismo.

| Estado | 0   | 1   |
|--------|-----|-----|
| q0     | q1  | qd  |
| q1     | q1  | q1  |
| qd     | qd  | qd  |

---

## 3. Lenguaje Reconocido

El autómata reconoce el siguiente lenguaje:

L = { w ∈ {0,1}* | w comienza con 0 }

Condiciones formales:

1. La cadena no puede ser vacía (ε no pertenece al lenguaje).
2. El primer símbolo debe ser `0`.
3. Después del primer símbolo, puede aparecer cualquier combinación de `0` y `1`.

Expresión regular equivalente:


---

## 4. Funcionamiento del Programa

El programa realiza las siguientes operaciones:

1. Lee un archivo de texto recibido como argumento por línea de comandos.
2. Procesa cada línea como una cadena independiente.
3. Evalúa cada símbolo verificando que pertenezca al alfabeto Σ.
4. Aplica la función de transición δ símbolo por símbolo.
5. Determina aceptación si el estado final pertenece al conjunto F.

### Reglas de validación

- Si la cadena es vacía → se rechaza.
- Si contiene símbolos fuera del alfabeto → se rechaza.
- Si termina en un estado no perteneciente a F → se rechaza.

---

## 5. Estructura del Proyecto


---

## 6. Requisitos

- Python 3.x
- No requiere librerías externas

---

## 7. Formas de Ejecución

### 7.1 Ejecución básica

Desde la terminal:


o dependiendo del entorno:


---

### 7.2 Formato general


Si el archivo no existe, el programa mostrará:


Si no se proporciona el argumento:


---

## 8. Formato del Archivo de Entrada

El archivo debe contener:

- Una cadena por línea
- Solo símbolos `0` y `1`

Ejemplo:

1010
0110
0001
1110

Las líneas vacías se ignoran automáticamente.

---

## 9. Formato de Salida

Para cada cadena, el programa imprime:
<cadena> : ACEPTA

o

<cadena> : NO ACEPTA

Ejemplo:

0110 : ACEPTA
1010 : NO ACEPTA

---

## 10. Consideraciones Técnicas

- La función de transición está implementada mediante un diccionario que modela δ como una función total.
- El estado trampa (qd) garantiza que todas las combinaciones posibles estén definidas.
- El procesamiento es determinista: para cada estado y símbolo existe exactamente una transición posible.
- El algoritmo tiene complejidad O(n) por cadena, donde n es la longitud de la cadena.

---

## 11. Objetivo Académico

Este proyecto demuestra:

- Implementación computacional de un modelo formal de autómata.
- Aplicación práctica de teoría de lenguajes formales.
- Simulación determinista de reconocimiento de cadenas.
- Validación estructural de entradas mediante un AFD.

---

## 12. Descripción del Código

### 12.1 Clase `AFD`

La clase `AFD` encapsula la definición formal del autómata y su comportamiento.

#### Constructor (`__init__`)

En el constructor se definen los componentes de la 5-tupla:

- `self.Q` → Conjunto de estados  
- `self.Sigma` → Alfabeto  
- `self.q0` → Estado inicial  
- `self.F` → Estados de aceptación  
- `self.delta` → Función de transición  

La función de transición se implementa como un diccionario de Python donde:

(estado_actual, simbolo) → estado_siguiente

Esto garantiza acceso en tiempo constante O(1) por transición.

---

### 12.2 Método `procesar(cadena)`

Este método implementa la simulación del AFD.

Flujo de ejecución:

1. Se inicializa el estado actual en `q0`.
2. Si la cadena es vacía, se rechaza inmediatamente.
3. Se recorre la cadena símbolo por símbolo.
4. Se valida que cada símbolo pertenezca al alfabeto.
5. Se aplica la función de transición.
6. Al finalizar, se verifica si el estado actual pertenece al conjunto de aceptación.

Retorna:

- `True`  → si la cadena es aceptada.
- `False` → si la cadena es rechazada.

---

### 12.3 Función `main()`

La función principal:

1. Verifica que se haya pasado exactamente un argumento.
2. Intenta abrir el archivo proporcionado.
3. Lee cada línea del archivo.
4. Elimina espacios en blanco con `strip()`.
5. Evalúa cada cadena con el método `procesar`.
6. Imprime el resultado correspondiente.

Incluye manejo básico de errores para:

- Argumentos incorrectos.
- Archivo no encontrado.

---

## 13. Propiedades Formales del Autómata

Este AFD cumple con las propiedades fundamentales:

- Determinismo:  
  Para cada par (estado, símbolo) existe exactamente una transición.

- Función de transición total:  
  Está definida para todo Q × Σ gracias al estado trampa.

- Cerrado bajo concatenación interna posterior al primer símbolo válido.

---

## 14. Ejemplo de Trazado de Ejecución

Cadena: `0110`

Secuencia de estados:

Estado inicial: q0
Lee '0' → q1
Lee '1' → q1
Lee '1' → q1
Lee '0' → q1
Estado final: q1 ∈ F → ACEPTA

---

Cadena: `1010`

Estado inicial: q0
Lee '1' → qd
Lee '0' → qd
Lee '1' → qd
Lee '0' → qd
Estado final: qd ∉ F → NO ACEPTA

---

## 15. Complejidad Computacional

Sea n la longitud de la cadena:

- Tiempo: O(n)
- Espacio: O(1)

El autómata no utiliza memoria adicional proporcional a la entrada, únicamente mantiene el estado actual.

---

## 16. Posibles Extensiones

El diseño permite:

- Modificar el lenguaje cambiando la función δ.
- Añadir más estados.
- Convertir el AFD en AFN.
- Implementar minimización de estados.
- Generar representación gráfica del autómata.

---

## 17. Conclusión

El proyecto implementa correctamente un Autómata Finito Determinista conforme a su definición matemática formal.

Se demuestra la correspondencia entre:

- Modelo teórico (lenguajes formales)
- Representación formal (5-tupla)
- Implementación computacional (simulación determinista)

El sistema es estructuralmente correcto, determinista y completamente definido sobre su dominio.

---

## 18. Validación del Lenguaje Reconocido

Sea M el autómata definido como:

M = (Q, Σ, δ, q0, F)

Se demuestra que el lenguaje reconocido por M es:

L(M) = { w ∈ {0,1}* | w comienza con 0 }

### Demostración informal

1. Desde el estado inicial q0:
   - Si el primer símbolo es `0`, se transita a q1.
   - Si el primer símbolo es `1`, se transita a qd.

2. El único estado de aceptación es q1.

3. Desde q1:
   - Con `0` o `1`, se permanece en q1.

4. Desde qd:
   - Toda transición permanece en qd.

Por lo tanto:

- Toda cadena que comience con `1` es rechazada.
- Toda cadena que comience con `0` y tenga longitud ≥ 1 es aceptada.
- La cadena vacía es rechazada.

Queda demostrado que:

L(M) = 0(0|1)*

---

## 19. Ejemplo de Archivo de Prueba

Archivo `entrada.txt`:

1010
0110
1101
0001
1110
0011
1011
0101
1001
0111
0000
1100
10101
01010
11111
00010
10110
01101
10000
11101
000

Al ejecutar el programa:

python AFD.py entrada.txt

Se obtendrán resultados indicando aceptación o rechazo para cada cadena.

---

## 20. Manejo de Errores

El sistema contempla los siguientes casos:

### 20.1 Archivo inexistente

Salida:

Error: archivo no encontrado.

### 20.2 Argumentos incorrectos

Salida:

Uso: python afd.py <archivo.txt>

### 20.3 Símbolos fuera del alfabeto

Si una cadena contiene símbolos distintos de `0` o `1`, será automáticamente rechazada.

---

## 21. Garantías del Modelo

El autómata implementado garantiza:

- Determinismo absoluto.
- Transiciones definidas para todo el dominio Q × Σ.
- Reconocimiento correcto del lenguaje especificado.
- Independencia entre cadenas procesadas.
- Simulación fiel al modelo matemático formal.

---

## 22. Aplicaciones Académicas

Este proyecto puede utilizarse para:

- Introducción a teoría de autómatas.
- Comprensión práctica de lenguajes regulares.
- Simulación computacional de modelos formales.
- Base para proyectos más avanzados en compiladores o teoría de la computación.

---

## 23. Licencia

Proyecto académico con fines educativos.

---

## 24. Autor

Proyecto desarrollado como implementación práctica de Autómatas Finitos Deterministas en el contexto de Ciencia de la Computación.

---
