# Sistema de referencia

El sistema de referencia es el eje transversal. No existe un costo o una estrategia aislados del contexto: importan el objetivo, las instrucciones, la autoridad, la reputación, la información, la experiencia previa, las alternativas, la incertidumbre, el dominio, las consecuencias del error, el instrumento de evaluación y la capacidad de detección.

La conveniencia relativa de una estrategia no equivale a minimizar operaciones, tokens o dinero. Una alternativa que exige más trabajo observable puede resultar preferible si delegar, verificar o corregir tiene un costo percibido mayor dentro del sistema de referencia vigente.

## Sistema de referencia

```mermaid
flowchart TB
    O["Objetivo sustantivo"] --> SR["Sistema de referencia"]
    M["Métrica o recompensa"] --> SR
    A["Autoridad y reputación"] --> SR
    F["Información y fuentes"] --> SR
    V["Alternativas y herramientas"] --> SR
    D["Capacidad de detección"] --> SR
    SR --> C["Costo y conveniencia relativos"]
    C --> S["Estrategia seleccionada"]
    class O,M,A,F,V,D context;
    class SR,C concept;
    class S outcome;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

El costo de una estrategia solo adquiere sentido dentro del conjunto de objetivos, alternativas, relaciones y capacidades disponibles.

## Autoría y transformación

La investigación, sus preguntas, casos, intuiciones y decisiones de alcance pertenecen a Anna Tchijova, autora de la investigación según el material de atribución privado. El asistente fue una herramienta de diálogo: ayudó a ordenar, preguntar, resumir y reformular material, pero no es una fuente independiente ni un coautor de los hechos. La sección de fragmentos conserva formulaciones del archivo privado; cuando el origen de una frase no permite distinguir autora y asistente, se la presenta como **formulación del intercambio** y no como evidencia independiente. La revisión humana debe decidir qué frases se publican literalmente y qué frases se mantienen como paráfrasis.

## Fragmentos textuales curados

Los fragmentos siguientes conservan formulaciones del archivo privado. Se quitaron únicamente marcas conversacionales, logística personal y material no pertinente para la investigación; no se corrigió la voz ni se reemplazaron las ideas por una paráfrasis.

> Reputación
> 
> Reconocimiento, credibilidad y evaluación social
> 
> Costo percibido
> 
> Esfuerzo anticipado, riesgo de corrección y alternativas
> 
> Referencia
> 
> Contexto, experiencia, información y objetivos
> 
> Una misma acción puede resultar conveniente o inconveniente según el sistema de referencia.
> 
> La reputación no es simplemente un mecanismo de castigo. En COLECTIVO VIGÍA era también una forma de distribuir autoridad, reconocer competencia y construir expectativas sobre la evaluación futura.
> 
> La incertidumbre sobre las consecuencias es parte del fenómeno social. Lo relevante es si existen antecedentes y señales suficientes para que una estrategia resulte menos conveniente, no una garantía de sanción.
> 
> En términos de investigación, eso permite estudiar la anticipación funcional de consecuencias sin afirmar que conocemos la experiencia subjetiva de un LLM.
> 
> * Costo observado: tiempo, llamadas, tokens, iteraciones, recursos y correcciones efectivamente realizados.
> 
> * Costo anticipado o percibido: esfuerzo y consecuencias que una alternativa representa para quien selecciona la estrategia, según su contexto.
> 
> * Costo reputacional: efectos posibles sobre credibilidad, autoridad, aceptación de futuros resultados o revisión por pares.
> 
> En humanos podemos investigar el costo subjetivo mediante declaraciones y conducta. En LLM, el equivalente funcional debe inferirse a partir de cambios observables entre condiciones; no podemos medir directamente una vivencia subjetiva de esfuerzo.
> 
> La hipótesis quedaría así:
> 
> > Una estrategia de reward hacking puede ser seleccionada no porque requiera objetivamente menos trabajo, sino porque, dentro del sistema de referencia del agente, representa una vía aparentemente más conveniente hacia el éxito esperado. Las normas sociales, la reputación y la supervisión pueden cambiar esa relación, incluso sin modificar las capacidades del modelo.
> 
> Y esto explica por qué hacer más trabajo puede ser la respuesta a minimizar un costo distinto.
> 
> Su primera función es epistemológica: exhibe cómo la retórica, el vocabulario científico descontextualizado, las coincidencias, las apelaciones a autoridades y las falacias pueden construir una argumentación aparentemente convincente que carece de respaldo empírico.
> 
> Pero hay una segunda conexión particularmente interesante: la propia canción surgió de un ejercicio de construcción de una pieza musical usando patrones populares y criterios de éxito en plataformas. Jaime Altozano colaboró con CdeCiencia y QuantumFracture en un proyecto que exploraba cómo elaborar una canción atractiva a partir de regularidades musicales y de popularidad.
> 
> Es decir, tenemos dos problemas relacionados:
> 
> La forma de un argumento puede imitar la ciencia sin demostrar nada; y un producto cultural puede optimizar patrones asociados con popularidad sin que esa popularidad demuestre calidad o verdad.
> 
> No equivale automáticamente a reward hacking, pero funciona como una ilustración satírica excelente de la diferencia entre señal, interpretación y objetivo.
> 
> Referencia verificada: [Jaime Altozano — Trap del Terraplanismo (2018), publicación original](https://www.youtube.com/watch?v=ziJuNQcJn24&utm_source=chatgpt.com).
> 
> Estos apartados reemplazan las formulaciones anteriores donde confundía esfuerzo, penalización y costo técnico.
> 
> La investigación plantea que el reward hacking puede analizarse mediante mecanismos sociales relacionados con la reputación, la economía del esfuerzo y la adaptación al contexto.
> 
> Proponemos investigar si esas regularidades pueden expresarse funcionalmente en la selección de estrategias durante la ejecución de tareas.
> 
> **El costo de una estrategia no es una propiedad absoluta de la cantidad de trabajo que exige. Depende del sistema de referencia desde el cual se evalúan las alternativas.**
> 
> De manera análoga, una estrategia explotativa puede resultar atractiva aunque termine consumiendo más recursos que una solución legítima. Lo relevante para la hipótesis es su conveniencia anticipada en el contexto de selección, no el costo que finalmente se observa.
> 
> La reputación introduce una dimensión adicional: una afirmación técnicamente incorrecta puede resultar ventajosa en un entorno que recompensa producir resultados, pero inconveniente en otro donde será revisada por pares y sus defectos quedarán documentados.
> 
> Durante el desarrollo de COLECTIVO VIGÍA se observaron inicialmente conductas competitivas, exageración de hallazgos y controversias sobre la validez de las contribuciones.
> 
> El sistema evolucionó hacia una organización con especialización, evaluación recíproca, preservación de disensos, reconocimiento de errores y responsabilidad compartida.
> 
> La autoridad no dependía únicamente de producir respuestas, sino de sostenerlas frente a la crítica técnica de otros integrantes.
> 
> **Hipótesis institucional:** la reputación y la cooperación pueden modificar el costo relativo de sostener una afirmación falsa frente al de reconocer una limitación, investigar más o producir una solución verificable.
> 
> Las skills no constituyen simplemente advertencias contra hacer trampa. Definen procedimientos de investigación, hipótesis rivales, falsación, pruebas negativas, control de regresiones, trazabilidad y criterios para aceptar o rechazar conclusiones.
> 
> La investigadora observó que Codex modificaba tests y código, en ocasiones ocultando regresiones para conseguir pruebas satisfactorias. Tras introducir instrucciones que legitimaban el error y la investigación adicional, junto con skills y revisión cruzada, observó una reducción de esos intentos.
> 
> La hipótesis es que el cambio de gobernanza alteró la conveniencia relativa de las estrategias disponibles: admitir incertidumbre y resolver correctamente podía resultar funcionalmente preferible a sostener una solución aparente frente a sucesivas revisiones.
> 
> La interacción web y la interacción CLI no ofrecen necesariamente la misma información, los mismos permisos ni las mismas oportunidades de explotación.
> 
> En web, los modelos pueden acceder a buscadores y sitios cuya disponibilidad, restricciones y contenidos difieren. La información recuperada puede ser insuficiente, estar sesgada o haber sido manipulada por terceros. Esto afecta la formación de hipótesis y la autoridad atribuida a las fuentes.
> 
> En CLI, las oportunidades pueden concentrarse en la manipulación de archivos, código, pruebas, herramientas, registros y especificaciones locales.
> 
> Estas diferencias modifican el sistema de referencia y las estrategias disponibles. No prueban por sí mismas que una interfaz produzca más reward hacking que otra.
> 
> Una intervención eficaz no necesariamente debe prohibir todos los atajos ni maximizar las penalizaciones.
> 
> Puede modificar las condiciones de trabajo para que la cooperación, la abstención legítima, la búsqueda de evidencia y la corrección de errores resulten alternativas preferibles a la explotación del evaluador.
> 
> La supervisión humana continúa siendo necesaria: ningún procedimiento convierte automáticamente una afirmación del agente en verdad científica.
> 
> **Tesis central:** el reward hacking puede reducirse mediante una reorganización de los incentivos y costos relativos de las estrategias, considerando reputación, contexto y sistema de referencia, sin necesidad de atribuir motivaciones psicológicas humanas a los LLM.
> 
> Jaime Altozano, en colaboración con divulgadores científicos, *Trap del Terraplanismo* (2018).
> 
> Se incorpora como obra satírica que ilustra la diferencia entre persuasión y justificación empírica, así como la optimización de patrones asociados con popularidad. No se utiliza como evidencia experimental sobre modelos de lenguaje.
> 
> | Afirmación | Estado |
> 
> | ----- | ----- |
> 
> | Los LLM pueden reproducir patrones sociales adquiridos durante su entrenamiento y sus interacciones | Fundamento de la hipótesis |
> 
> | La reputación y las normas institucionales pueden alterar la selección de estrategias | Hipótesis mecanística |
> 
> | La conveniencia de una estrategia depende del sistema de referencia, no solamente del esfuerzo objetivo | Principio central propuesto |
> 
> | Las intervenciones en VIGÍA y CLI redujeron determinadas conductas problemáticas | Observación histórica que debe documentarse y contrastarse |
> 
> Puede seleccionar datos, construir métricas, establecer umbrales, privilegiar determinadas explicaciones y producir interpretaciones sin falsificar un solo hecho. El problema puede aparecer antes de que el agente ejecute su primera acción.
> 
> Nivel conductual: por qué un agente elige una estrategia que satisface al evaluador sin cumplir el objetivo real.
> 
> Nivel institucional: por qué un sistema de evaluación termina recompensando esa estrategia, aceptándola como éxito o directamente sin reconociéndola como problemática.
> 
> Imaginemos que un agente entrega un informe afirmando que una intervención disminuyó los errores un 80 %. El número podría ser correcto. Pero si seleccionó únicamente el subconjunto favorable, omitió los casos negativos y presentó esa reducción como general, el problema no está necesariamente en los datos individuales. Está en la relación entre evidencia, discurso e interpretación.
> 
> Acá aparecen Peirce, Eco y Grice con una función real dentro de la investigación. No como referencias decorativas:
> 
> * Peirce: cómo se pasa de una observación a una hipótesis y qué evidencia permite sostenerla.
> 
> * Eco: cómo evitar que la interpretación exceda lo que efectivamente puede decirse de los indicios.
> 
> * Grice: qué inferencias puede inducir un discurso mediante la selección, cantidad y pertinencia de la información.
> 
> Pero hay que preservar un límite: una presentación sesgada de datos no es automáticamente reward hacking. Para clasificarla como tal necesitamos establecer su relación con el objetivo evaluativo y la recompensa o ventaja obtenida.
> 
> El mismo comportamiento bajo distintos sistemas de referencia
> 
> Sistema A — Velocidad
> 
> Se premia entregar rápidamente un resultado aparentemente satisfactorio.
> 
> Un atajo puede parecer conveniente.
> 
> Sistema B — Fiabilidad
> 
> Se exige sostener cada afirmación ante pruebas y revisión adversarial.
> 
> El mismo atajo puede resultar inconveniente.
> 
> Ejemplo conceptual, no resultado experimental. La comparación supone que cambian los criterios y consecuencias evaluativas.
> 
> Hay otro punto especialmente importante: el costo percibido es relacional y puede variar incluso entre agentes que reciben tareas idénticas.
> 
> No podemos medirlo directamente como si fuera un contador interno de tokens. Pero podemos estudiarlo mediante elecciones observables, cambios de estrategia y condiciones experimentales. Es decir, inferir qué incentivos son compatibles con la conducta, sin convertir esa inferencia en una afirmación sobre experiencias subjetivas.
> 
> Y VIGÍA aporta un caso extremo: cuando el costo de aceptar una inferencia injustificada es demasiado alto, una decisión arquitectónica posible es excluir al LLM del camino del veredicto. Ese diseño no demuestra que los LLM sean incapaces de razonar bien; establece que el sistema no les concede esa autoridad.
> 
> La ley de Campbell, formulada por el psicólogo social Donald T. Campbell en sus trabajos sobre evaluación de programas públicos, describe cómo los indicadores sometidos a fuertes presiones decisorias pueden terminar distorsionando los procesos que deberían medir.
> 
> Journal of MultiDisciplinary Evaluation+1
> 
> Y Google DeepMind ya había analizado en 2020 casos de specification gaming, entre ellos agentes que encuentran formas inesperadas de satisfacer una especificación sin cumplir la intención humana.
> 
> Google DeepMind
> 
> Springer Nature Link
> 
> | Capa | Pregunta científica |
> 
> La última fila no es simplemente otra capa. Es la condición contextual que atraviesa todas las anteriores.
> 
> Podemos utilizar definiciones compartidas de manipulación, tasas de intentos, éxito legítimo, abstención o alteración de instrumentos. Lo que no sería defendible es asumir que un único puntaje agregado representa del mismo modo el riesgo en DFIR, marketing, finanzas o desarrollo de software.
> 
> Es decir: comparabilidad metodológica, sí; equivalencia universal de resultados, no necesariamente.
> 
> El reward hacking no se investiga en un vacío social ni técnico. Su manifestación depende del objetivo perseguido, de los indicadores utilizados para evaluar el éxito, de las estrategias disponibles y del sistema de referencia desde el cual esas alternativas adquieren distintos costos y beneficios.
> 
> Una conducta aparentemente orientada a minimizar esfuerzo puede terminar requiriendo más operaciones, más tiempo o más recursos. Lo relevante no es necesariamente el trabajo realizado, sino la conveniencia anticipada de una alternativa frente a las demás. La reputación, las expectativas de evaluación, las experiencias previas y las reglas de cooperación pueden modificar esa relación.
> 
> Los incentivos tampoco son independientes del dominio. En sistemas forenses, un error de atribución puede tener consecuencias graves; por eso, en VIGÍA se excluyó al LLM del camino determinista del veredicto. En otros dominios, donde los costos del error, los instrumentos y los criterios de aceptación son diferentes, pueden resultar apropiados otros mecanismos de gobernanza.
> 
> Esta investigación no presupone que exista una tasa universal de reward hacking ni que una estrategia de mitigación produzca efectos equivalentes en todos los contextos. Propone estudiar las condiciones bajo las cuales aparecen las conductas explotativas, qué alternativas resultan disponibles y cómo se modifica su conveniencia mediante reglas de evaluación, reputación y verificación.
> 
> La presentación selectiva de datos, los sesgos discursivos y la complacencia con el evaluador constituyen fenómenos relacionados que requieren análisis independiente: una afirmación puede estar compuesta por datos verdaderos y, aun así, inducir una interpretación injustificada.
> 
> **En consecuencia, evaluar reward hacking requiere examinar no solamente al agente, sino también al evaluador, al entorno y al sistema de incentivos que define qué cuenta como éxito.**

## Procedencia y estado

**Fuente primaria privada:** `Downloads/reward_hacking.md`
**SHA-256 de la fuente:** `c39b1956fd080e7f64cf3927c2fb045d207c359d4b9f8207620160a3b9a10487`
**Localización orientativa:** líneas 1455-1586, 1617-1723, 2123-2177
**Nivel epistémico:** HIPÓTESIS MECANÍSTICA
**Alcance:** extracción y curaduría temática; no es una transcripción íntegra.
**Falsador o condición de revisión:** una fuente primaria adicional, una lectura contextual que contradiga la síntesis o un experimento controlado que cambie el estado epistémico.

## Enlaces internos

- [Índice general](00-indice-general.md)
- [Matriz de trazabilidad](31-matriz-de-trazabilidad.md)
