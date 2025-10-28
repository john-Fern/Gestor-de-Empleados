# �� Actividad Grupal – “Gestor de Empleados con Funciones”

### �� **Objetivo**

Aplicar todo lo aprendido sobre **funciones**, **operadores**, **tipos de datos** (`int`, `float`, `str`), y **estructuras de control** (`while`, `if`) creando un pequeño programa en equipo.

---

## �� **Contexto del ejercicio**

Imagina que trabajas en una empresa llamada **PyCompany**, y el jefe te pide un mini programa en Python para **registrar empleados** y calcular **bonos salariales**.

El programa deberá ejecutarse desde consola y mostrar un **menú interactivo** que permita:

1. Registrar la información de un empleado
2. Calcular su bono
3. Mostrar el resumen del trabajador
4. Salir del programa

---

## �� **Instrucciones del desafío**

El programa debe:

1. **Tener al menos 4 funciones:**

   - `ingresar_datos()`: pide al usuario nombre, edad, cargo, sueldo base y porcentaje de bono.
   - `calcular_bono(sueldo, porcentaje)`: calcula el bono y devuelve el total.
   - `mostrar_resumen(nombre, edad, cargo, total)`: imprime los datos del empleado y su sueldo con bono.
   - `mostrar_mensaje_despedida()`: muestra un mensaje final al salir del programa.

2. **Usar conversiones de tipos:**

   - Nombre y cargo → `str`
   - Edad y sueldo → `int`
   - Porcentaje del bono → `float`

3. **Incluir un menú dentro de un `while`** que se repita hasta que el usuario decida salir.  
   Ejemplo de opciones:

   ```
   1. Ingresar datos del empleado
   2. Calcular bono
   3. Mostrar resumen
   4. Salir
   ```

4. **Mostrar mensajes amigables y claros.**
5. **Evitar `try/except`:** deben aprender a usar correctamente `int()`, `float()`, `str()`.

---

## �� **Trabajo en equipo**

Cada integrante será responsable de **una parte del programa**:

| Integrante | Tarea                                          | Archivo sugerido |
| ---------- | ---------------------------------------------- | ---------------- |
| 1️⃣         | Función `ingresar_datos()`                     | `datos.py`       |
| 2️⃣         | Función `calcular_bono()`                      | `bono.py`        |
| 3️⃣         | Función `mostrar_resumen()`                    | `resumen.py`     |
| 4️⃣         | Menú principal + `mostrar_mensaje_despedida()` | `main.py`        |

Luego deberán **subir sus archivos a GitHub** y unificarlos en un mismo repositorio colaborativo.

---

## �� **Criterios de evaluación**

| Criterio                         | Ponderación | Descripción                                         |
| -------------------------------- | ----------- | --------------------------------------------------- |
| ✅ Uso correcto de funciones     | 25%         | Cada función cumple un propósito y devuelve datos.  |
| 🔢 Conversiones de tipo          | 20%         | Se aplican `str`, `int`, `float` donde corresponde. |
| 🔁 Uso de `while` y menú         | 20%         | El menú se repite correctamente y permite salir.    |
| 🗣️ Mensajes claros y formateados | 15%         | El programa es legible y agradable.                 |
| 💬 Mensaje final personalizado   | 10%         | Incluye el mensaje de cierre solicitado.            |
| 🧑‍💻 Trabajo en equipo (GitHub)    | 10%         | Subida colaborativa y commits de cada integrante.   |

---

## �� **Mensaje final para los alumnos**

> “Este ejercicio no es solo para programar: es para trabajar en equipo, coordinarse, revisar código y aprender de los errores.
>
> La clave no es hacerlo perfecto, sino **hacerlo juntos** y **entender cómo se arma un programa completo paso a paso.** ��”