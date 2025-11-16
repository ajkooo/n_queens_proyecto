# trabajo de programacion
a mí no me vengáis con que no sabéis hacer el código. le preguntáis a vuestra abuela o al panadero de la esquina. os buscáis la puta vida

Un archivo README sirve como documentación para describir un proyecto, conjunto de datos u otro conjunto de archivos, facilitando su comprensión, uso y colaboración. Proporciona información clave como el propósito del proyecto, cómo comenzar a usarlo, su estructura, los detalles de contacto de los autores y las licencias de uso. 

//chavales aquí podemos ir poniendo cómo va a ser la estructura del código y a las carpetas que se va a tener acceso. sé que hay mejores formas para hacerlo pero bueno se irá viendo, lo he usado 2 veces contadas.

https://www.youtube.com/watch?v=nsbHNy7yWic   (video yt)

objetivo: el jugador intrduce el tamaño del tablero. El programa a continuación imprimirá el número de commbinaciones posibles (p.e., siempre que el tiempod de espera sea menor a 20 s) y una solución aleatoria. Se utilizan diferentes métodos en función de la dimensión del tablero:


si N==1:
  una solucion

si N==2 o N==3:
  error
  
si 3 < N <= 20:
  usamos backctracking

si 20 < N <= 64:
  usamos bitwise; exigimos un tiempo menor a 20 segundos; si no, imprime una solución posible

si N > 64;
  usamos min-conflicts; una solución posible
