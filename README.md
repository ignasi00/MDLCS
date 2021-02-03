# My Deep Learning Custom System

Se pretende realizar un sistema ineficiente pero claro. Cuyo flujo se pueda leer facilmente.  
Posteriormente, se mantendra una rama clara y se intentara optimizar trocitos (perfectamente intercambiables en la rama clara);
Ademas de la rama clara, cada optimizacion tendrá su rama y una rama contendrá la biblioteca más optimizada.

---

Filosofia básica:

* No se pretende escoder/forzar nada relevante en el estudio del Deep Learning
* Se pretende definir un sistema genérico que realmente facilite el estudio de las redes y entrenamientos
    * Se define la lógica que conecta las funciones de procesado, modelo, losses y entrenamiento
    * Se ajusta el sistema de entrenamiento al equipo, mediante configuracion del usuario

---

Elementos de un entrenamiento:


* Los modelos son ajenos a la biblioteca
* Los modelos estan descritos en pyTorch
* Los modelos únicamente devuelven resultados
    * Preferiblemente los resultados deben ser tensores directamente usables por alguna loss estándar. Possible clasificacion
    * Se aceptan modelos con resultados multiples pero, el usuario es responsable de su compatibilidad
* Ante el interés en resultados intermedios, se pretende usar una de las siguientes opciones:
    * Pedir un método propio del objeto modelo para extraer el resultado
    * Desarrollar un metodo propio del sistema

* Las losses son ajenas a la biblioteca
* Las losses son compatibles con pyTorch
* Las losses solo requieren un input y un output, elementos adicionales han de ser opcionales
    * Preferiblemente las losses definirán y se clasificarán por el tipo de input, preferiblemente simple. Estandarización
* Durante el entrenamiento solo se optimiza una loss

* Las regularizaciones son ajenas a la biblioteca
* Las regularizaciones son compatibles con pyTorch
* Las regularizaciones solo requieren un output, elementos adicionales han de ser opcionales (posible no regularizacion en detecciones correctas o loss < th)
    * Prederiblemente las regularizaciones definirán y se clasificarán por el tipo de input, preferiblemente simple. Estandarización
* Durante el entrenamiento solo se optimizara una regulrización

* Las métricas son ajenas a la biblioteca
* Las métricas preferiblemente son compatibles con pyTorch
* Las métricas no son losses aunque las losses pueden ser métricas
* Las métricas no sirven para entrena
* Las métricas aparecen en el informe junto a la loss usada

* Los algoritmos de entrenamiento son ajenos a la biblioteca
* Los algoritmos de entrenamiento son compatibles con pyTorch
* Se garantiza el acceso al objeto modelo durante su creación
    * El usuario debe ajustar el entrenamiento al modelo

* El pre y postprocesado son ajenos a la biblioteca
* Los preprocesados devuelven torch.Tensor y permiten torch.Tesnor como entrada
    * Son concatenables
    * Si se aplica data augmentation, es capaz de ir yielding elementos
* Los postprocesado son compatibles con pyTorch
    * Son concatenables
* Sería interesante que cada pre y post procesado tenga una linea que los describa (estilo str(modelo\_torch))

* Los dataloaders son parte de la biblioteca; pero, se pueden usar dataloaders ajenos
* Los dataloaders devuelven torch.Tensor

---

Elementos del sistema:

* El sistema es capaz de entrenar usando objetos que simplemente definan las funciones y modelos
* El sistema es capaz de gestionar I/O:
    * Usando diferentes convenios de entrada
    * Generando informes de salida
    * Guardando la descripción del modelo, preferiblemente tambien del pre y post proesado
    * Guardando el estado del modelo
    * Recuperando el estado modelo de un archivo
* El sistema permite el uso o no de regularización y permite ajustar su peso respecto a la loss
* El sistema da la utilidad para asignar distintas losses y regularizaciones ante resultados multiples o extraccion de resultados intermedios y definir como juntarlas, se considera 1 única loss
* El sistema da la utilidad de definir metricas para los resultados (simples o multiples) y para la extraccion de resultados intermedios, permitiendo usarlos en combinaciones o independientemente.
* El sistema gestiona los batches, mini-batches, etc
    * El usuario define los hiperparámetros
    * Depende de un estudio de la literatura posterior, es possible pase a ser un modulo reemplazable
* El sistema es inutil sin modelos o funciones, no obstane, es independiente; es decir, se pueden cambiar para facilitar la comparación
* El sistema es capaz de hacer particiones de la base de datos o usar una base ya particionada
* El sistema gestiona utilidades como la validación cruzada si el usuario lo prefiere así
* El sistema tiene la opcion VERBOSE; por defecto, VERBOSE esta activado (True)
* El sistema permite baterias de experimentos

---

Otras utilidades:

* El sistema contiene herramientas para representar los informes generados
* El sistema contiene herramientas para analizar el modelo
* Continene generadores de script bash, no se garantiza su funcionamiento: son modelos a completar
    * Un modelo permite baterias de experimentos desde bash; para casos de seridores con recursos limitados por tiempo
* El sistema permite comparar modelos

