# Tarea 45
# Algoritmos de búsqueda

## Descripción
Tenemos una lista de números [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]. Luego de ordenar, tenemos que buscar el número 875 en esta lista usando los siguiente algoritmos: secuencial y binario.

## Solución:

La resolución lo he desarrollado en Python y R. A continuación explico los algoritmos y su complejidad en términos de Big O

En primer lugar, para ordenar la lista uso el algoritmo quick_sort que tiene complejidad n*log(n)

### Sequencial

1. Partimos con pasos = 0, pasos indicará el elemento a extraer de la lista
2. Extraemos el elemento de la ubicación "paso". Si el elemento es igual a 875 paramos y devolvemos True. Caso contrario vamos al paso 3.
3. Si no es igual, aumentamos pasos = pasos + 1 y repetimos el paso 2
4. Si pasos es igual al total de elementos, devolvemos False

En el peor de los casos, como este ejemplo, vamos a tener que verificar todos los elementos de la lista, por lo que su complejidad es O(n).

Por ejemplo, si n = 1, solo haremos una comprobación. Si n = 10, haremos como máximo 10 comprobaciones. Para n, haremos como máximo n comprobaciones.

### Binario

1. Empezamos eligiendo el primer y último elemento de la lista
2. Definimos punto_medio como (primer + último) // 2
3. Extraemos el elemento ubicado en el punto_medio
4. Si el elemento es igual a 875 paramos y devolvemos True. Caso contrario vamos al paso 5.
5. Si numero < elemento, actualizamos último = punto_medio - 1. Si numero > elemento, actualizamos primero = punto_medio + 1. Pasamos al paso 2.

Se puede ver, que si no encontramos el número en cada iteración, la lista se reduce a la mitad. En el peor de los casos, tendremos que dividir siempre por la mitad la lista, pero no será necesario comprobar en todos los elementos, ya que en cada iteración, hay elementos que se eliminarán. Esto nos indica que la complejidad es menor que O(n)

Por ejemplo, supongamos que la lista es de longitud 32. Si fallamos en el primer intento, en el segundo intento la lista tendrá longitud 16. Si fallamos en el segundo intento, en el tercer intento la lista tendrá longitud 8. Si fallamos el tercer intento, el cuarto intento tendrá longitud 4. Si fallamos el cuarto intento, el quinto tendrá longitud 2. Por último, si fallamos en el quinto intento, el sexto intento tendrá longitud 1. Los pasos serían: 32 -> 16 -> 8 -> 4 -> 2 -> 1, un total de 5 pasos (mucho menor que los 32 pasos en la búsqueda secuencial).

Si la lista tiene longitud 16, los pasos serían: 16 -> 8 -> 4 -> 2 -> 1, un total de 4 pasos.

Veamos en la siguiente tabla:

| Longitud | Número de pasos |
| 1 | 0 |
| 2 | 1 |
| 4 | 2 |
| 8 | 3 |
| 16 | 4 |
| 32 | 5 |
| 64 | 6 |
| 128 | 7 |
| 256 | 8 |
| 512 | 9 |
| 1024 | 10 |

Podemos ver de la tabla que este algoritmo tiene una complejidad logarítmica.
Por lo que este algoritmo se denota como complejidad O(log(n))