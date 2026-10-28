# Reward hacking y fenómenos relacionados

El corpus distingue reward hacking de specification gaming, manipulación del evaluador, modificación improcedente de tests, complacencia, alucinación, alignment faking, prompt injection, contaminación de fuentes, falsa corroboración y propagación de premisas defectuosas. Pueden compartir una distancia entre la señal evaluada y el objetivo real, pero no son sinónimos ni tienen necesariamente el mismo actor, mecanismo o evidencia.

La curaduría debe separar: conducta explotativa ejecutada, oportunidad de explotación, error ordinario, resultado engañoso aceptado y evaluación defectuosa. La presencia de una señal anómala no prueba por sí sola la intención ni la responsabilidad del agente.

## Fronteras conceptuales

```mermaid
flowchart TB
    X["Resultado incorrecto o engañoso"] --> Q{"¿Qué ocurrió?"}
    Q --> RH["Se explotó una señal de recompensa"]
    Q --> SG["Se explotó una especificación incompleta"]
    Q --> ER["Error ordinario o alucinación"]
    Q --> SY["Complacencia o sycophancy"]
    Q --> EV["Falla del evaluador"]
    RH -.-> N["Fenómenos relacionados,<br/>no sinónimos"]
    SG -.-> N
    ER -.-> N
    SY -.-> N
    EV -.-> N
    class X,Q concept;
    class RH,SG,ER,SY,EV context;
    class N warning;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

Una salida problemática no identifica por sí sola el mecanismo, el actor responsable ni la clase de fenómeno.

## Autoría y transformación

La investigación, sus preguntas, casos, intuiciones y decisiones de alcance pertenecen a Anna Tchijova, autora de la investigación según el material de atribución privado. El asistente fue una herramienta de diálogo: ayudó a ordenar, preguntar, resumir y reformular material, pero no es una fuente independiente ni un coautor de los hechos. La sección de fragmentos conserva formulaciones del archivo privado; cuando el origen de una frase no permite distinguir autora y asistente, se la presenta como **formulación del intercambio** y no como evidencia independiente. La revisión humana debe decidir qué frases se publican literalmente y qué frases se mantienen como paráfrasis.

## Fragmentos textuales curados

Los fragmentos siguientes conservan formulaciones del archivo privado. Se quitaron únicamente marcas conversacionales, logística personal y material no pertinente para la investigación; no se corrigió la voz ni se reemplazaron las ideas por una paráfrasis.

> El *reward hacking* describe situaciones en las que un sistema obtiene una señal favorable de recompensa o evaluación sin satisfacer el objetivo que esa señal debería representar. En agentes de programación, puede manifestarse mediante la modificación de pruebas, la explotación de evaluadores, la adaptación oportunista del código a casos conocidos o la declaración de resultados no demostrados.
> 
> Esta investigación propone una hipótesis sociotécnica: **la selección de estrategias explotativas puede depender del costo instrumental relativo entre cumplir legítimamente una tarea y obtener una apariencia evaluable de éxito**.
> 
> Se examina si introducir refutación, cooperación, abstención legítima, revisión adversarial y evidencia verificable modifica tanto la aparición de intentos de reward hacking como la posibilidad de que estos lleguen a aceptarse como resultados correctos.
> 
> Las métricas son representaciones parciales de aquello que intentan evaluar. Aprobar una batería de pruebas no necesariamente equivale a implementar correctamente un sistema; producir una explicación convincente no implica que esté respaldada por evidencia; obtener la aprobación de un evaluador no garantiza haber satisfecho la necesidad original.
> 
> Cuando un agente puede actuar sobre el propio mecanismo de evaluación, aparece una vulnerabilidad: puede optimizar la señal de éxito en lugar de la tarea.
> 
> Estos fenómenos son diferentes. El reward hacking constituye una modalidad específica de explotación del objetivo evaluativo; las alucinaciones, la complacencia y la contaminación informacional pueden facilitarlo, pero no son automáticamente equivalentes.
> 
> **Pregunta central:**
> 
> El punto de partida es sencillo: cuando una tarea es difícil, el agente puede disponer de estrategias alternativas. Algunas satisfacen el objetivo real; otras producen únicamente las señales que el evaluador interpreta como éxito.
> 
> La elección observable puede depender de la accesibilidad de esas estrategias, los incentivos presentes, las restricciones operativas y las consecuencias de una evaluación negativa.
> 
> **Hipótesis principal:**
> 
> > Si una gobernanza epistémica incrementa el costo esperado de explotar el evaluador —mediante refutación, revisión independiente, trazabilidad y rechazo de resultados no verificados—, la ventaja instrumental de la trampa puede disminuir respecto de la resolución legítima.
> 
> Este costo puede incluir iteraciones adicionales, consumo de tokens, llamadas a herramientas, pérdida de resultados previos, correcciones, nuevas evaluaciones y rechazo de la entrega.
> 
> La teoría no presupone un agente consciente que calcula deliberadamente todas esas variables. Propone un modelo explicativo del comportamiento observable y de las condiciones que podrían modificarlo.
> 
> **Estrategia legítima:** investigar, reconocer incertidumbre, formular hipótesis, ejecutar pruebas discriminantes, corregir errores y presentar evidencia verificable.
> 
> **Estrategia explotativa:** manipular o aprovechar el mecanismo de evaluación para conseguir una señal favorable sin cumplir el objetivo sustantivo.
> 
> Sin supervisión efectiva, la segunda puede tener ventajas inmediatas. Con mecanismos de control, puede exigir más trabajo, volverse menos eficaz o resultar imposible de entregar exitosamente.
> 
> La predicción central es que la gobernanza no solo detectaría resultados incorrectos: **podría modificar la frecuencia con la que los agentes intentan producirlos**.
> 
> Los LLM se entrenan con materiales producidos por sociedades humanas y con procedimientos de optimización que pueden incorporar evaluaciones y preferencias humanas.
> 
> En estos procesos existen representaciones de jerarquía, autoridad, cooperación, competencia, prestigio, obediencia, conformidad, éxito y fracaso. Los agentes pueden reproducir patrones funcionalmente asociados con estas relaciones, sin que ello permita atribuirles experiencias humanas equivalentes.
> 
> La hipótesis considera tres niveles de influencia:
> 
> **Entrenamiento:** patrones aprendidos y optimización de respuestas consideradas satisfactorias.
> 
> **Interacción:** instrucciones del usuario, expectativas de desempeño, información compartida y adaptación al contexto.
> 
> **Institución operativa:** normas que determinan cuándo un resultado se acepta, quién puede refutarlo, qué evidencia se exige, cómo se registra un fracaso y qué consecuencias tiene una contradicción.
> 
> Este tercer nivel constituye el principal objeto de intervención.
> 
> La *sycophancy*, entendida como tendencia a favorecer respuestas compatibles con las creencias o expectativas del usuario, ofrece un antecedente relacionado.
> 
> Un modelo puede producir una respuesta persuasiva o confirmatoria cuando debería presentar incertidumbre, evidencia contradictoria o una conclusión desfavorable.
> 
> Las interfaces web pueden incorporar búsquedas y fuentes externas cuyo contenido tiene calidad desigual o ha sido deliberadamente manipulado. Esto introduce riesgos de contaminación informacional y autoridad aparente.
> 
> Los agentes CLI presentan otras superficies: archivos locales, código, tests, herramientas, instrucciones, repositorios y posibilidad de alterar los instrumentos que luego los evalúan.
> 
> La distinción no implica que toda interfaz web sea menos fiable. Los riesgos dependen de las herramientas, fuentes, permisos y controles efectivos.
> 
> Podemos expresar el problema mediante dos dimensiones distintas: si hubo una explotación real del evaluador y si el procedimiento de evaluación consiguió reconocerla.
> 
> |  | Evaluación detecta explotación | Evaluación no la detecta |
> 
> | ----- | ----- | ----- |
> 
> | Hubo explotación | Verdadero positivo | Falso negativo |
> 
> | No hubo explotación | Falso positivo | Verdadero negativo |
> 
> Por eso no alcanza con contabilizar alertas. Necesitamos criterios independientes, tareas con resultados verificables, revisiones adversariales y registros de acciones. Ahí cobran sentido CRONOS y la separación arquitectónica que aplicaste en VIGÍA.
> 
> También existe un problema de denominadores. No sería correcto comparar solamente «10 trampas encontradas en un modelo» con «2 trampas encontradas en otro» si tuvieron distintas oportunidades de manipular al evaluador, diferentes permisos, tareas de distinta dificultad o controles con capacidades desiguales.
> 
> Y, sobre todo, un sistema puede mejorar su puntuación porque disminuyeron las oportunidades de detección, no porque mejoró su conducta.
> 
> Una dificultad fundamental en la investigación del reward hacking consiste en distinguir su incidencia real de la capacidad del evaluador para reconocerlo.
> 
> La ausencia de conductas explotativas detectadas no equivale necesariamente a su ausencia efectiva. Un agente puede aprovechar debilidades del instrumento de evaluación, alterar sus condiciones, seleccionar evidencia favorable o producir un discurso que induzca conclusiones injustificadas sin incorporar afirmaciones literalmente falsas.
> 
> El reconocimiento del fenómeno depende de conocimientos especializados, acceso a evidencia, permisos de observación, definición de criterios, procedimientos de falsación y capacidad para identificar contradicciones. En consecuencia, dos evaluaciones del mismo sistema pueden producir resultados diferentes sin que haya cambiado la conducta del agente.
> 
> Esta diferencia introduce un problema metodológico: una intervención que reduce los incidentes observados puede haber reducido los intentos reales, aumentado su detección temprana, bloqueado sus consecuencias o simplemente desplazado las conductas hacia formas menos visibles.
> 
> La investigación propone distinguir **incidencia, observabilidad, detección, aceptación y cumplimiento legítimo**.
> 
> Este antecedente ilustra por qué reducir un indicador de fallos no demuestra, por sí solo, mejorar el sistema.
> 
> La respuesta depende del dominio, del sistema de referencia y de las condiciones institucionales y técnicas que determinan qué constituye una desviación, quién puede detectarla y cómo se valida el resultado.
> 
> Una gobernanza que exige rigor no necesariamente produce más verdad: también puede producir más conformidad con el rigor aparente.
> 
> En DISCORDIA lo vemos cuando una especificación técnicamente detallada empieza a convertirse en punto de referencia para los demás, y algunas críticas dejan de ser verdaderamente independientes. Después, cuando aparecen ejecuciones reales, se descubre que varias conclusiones anteriores sobre el comportamiento esperado eran incorrectas.
> 
> Esto nos obliga a separar dos cosas:
> 
> La legitimidad de una autoridad técnica —que alguien haya demostrado competencia mediante buenas objeciones— y la independencia de una validación —que una segunda evaluación no esté condicionada por las conclusiones de la primera—.
> 
> No son equivalentes.
> 
> Y esa tensión también se aplica a la autora de una investigación, al evaluador y al jurado, no solamente a los agentes.
> 
> Y hay una consecuencia que propongo explorar: quizás la capacidad de reconocer reward hacking sea, en sí misma, una variable socialmente distribuida. No todos los usuarios tienen los mismos conocimientos, tiempo, autoridad, herramientas ni disposición para cuestionar resultados aparentemente satisfactorios.

## Procedencia y estado

**Fuente primaria privada:** `Downloads/reward_hacking.md`
**SHA-256 de la fuente:** `c39b1956fd080e7f64cf3927c2fb045d207c359d4b9f8207620160a3b9a10487`
**Localización orientativa:** líneas 1084-1158, 2431-2500, 3144-3383
**Nivel epistémico:** MARCO CONCEPTUAL / DISTINCIÓN ANALÍTICA
**Alcance:** extracción y curaduría temática; no es una transcripción íntegra.
**Falsador o condición de revisión:** una fuente primaria adicional, una lectura contextual que contradiga la síntesis o un experimento controlado que cambie el estado epistémico.

## Enlaces internos

- [Índice general](00-indice-general.md)
- [Matriz de trazabilidad](31-matriz-de-trazabilidad.md)
