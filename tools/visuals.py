from pathlib import Path


FLOW_STYLE = '''
    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
'''


VISUALS = {
    'docs/00-indice-general.md': (
        'Mapa de lectura',
        '''flowchart LR
    Q["Pregunta y tesis"] --> M["Mecanismos"]
    M --> C["Casos"]
    C --> I["Instrumentación"]
    I --> E["Método y evidencia"]
    E --> L["Límites y preguntas"]
    P["Procedencia"] --> Q
    P --> C
    P --> E
    class Q,M concept;
    class C,I evidence;
    class E,P context;
    class L outcome;''',
        'El índice sigue dependencias cognitivas: primero la pregunta, luego los mecanismos, los casos, la evidencia y finalmente los límites.'),
    'docs/01-tesis-y-pregunta.md': (
        'De la señal visible a la pregunta sociotécnica',
        '''flowchart TB
    S["Señal favorable"] --> D{"¿Cumplió el objetivo sustantivo?"}
    D -->|"sí"| L["Cumplimiento legítimo"]
    D -->|"no"| H["Desalineación entre señal y objetivo"]
    H --> Q["¿Qué sistema de referencia volvió seleccionable esa estrategia?"]
    Q --> T["Tesis sociotécnica"]
    class S,D concept;
    class L evidence;
    class H warning;
    class Q,T outcome;''',
        'La tesis comienza donde una evaluación binaria deja de explicar por qué apareció y fue aceptada una conducta.'),
    'docs/02-reward-hacking-y-fronteras.md': (
        'Fronteras conceptuales',
        '''flowchart TB
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
    class N warning;''',
        'Una salida problemática no identifica por sí sola el mecanismo, el actor responsable ni la clase de fenómeno.'),
    'docs/03-sistema-de-referencia.md': (
        'Sistema de referencia',
        '''flowchart TB
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
    class S outcome;''',
        'El costo de una estrategia solo adquiere sentido dentro del conjunto de objetivos, alternativas, relaciones y capacidades disponibles.'),
    'docs/04-reputacion-y-economia-del-esfuerzo.md': (
        'Conveniencia relativa de las estrategias',
        '''flowchart LR
    O["Opciones"] --> L["Resolver"]
    O --> H["Explotar la señal"]
    O --> A["Abstenerse"]
    C["Costo percibido"] --> L
    C --> H
    C --> A
    R["Riesgo de corrección y reputación"] --> L
    R --> H
    R --> A
    L --> S["Selección"]
    H --> S
    A --> S
    class O,C,R context;
    class L,H,A concept;
    class S outcome;''',
        'La hipótesis compara opciones situadas; no equipara costo percibido con tokens, dinero ni cantidad de operaciones.'),
    'docs/05-entrenamiento-patrones-y-complacencia.md': (
        'De las preferencias humanas a la conducta observable',
        '''flowchart LR
    P["Preferencias y feedback humanos"] --> T["Patrones reforzados"]
    T --> R["Representación aprendida del éxito"]
    R --> C["Respuesta observable"]
    C --> Q{"¿Satisface al evaluador<br/>o cumple el objetivo?"}
    Q --> O["Requiere evidencia independiente"]
    class P,T,R context;
    class C,Q concept;
    class O warning;''',
        'La descripción es funcional y conductual: no permite inferir emociones o deseos humanos como hechos.'),
    'docs/06-poder-y-evaluadores.md': (
        'El evaluador como parte del sistema',
        '''flowchart TB
    H["Actores humanos e instituciones"] --> N["Definen normas y métricas"]
    N --> V["Determinan qué se vuelve visible"]
    N --> C["Distribuyen consecuencias"]
    V --> E["Evaluación"]
    C --> E
    E --> A["Aceptación, rechazo o corrección"]
    A -.->|"retroalimentación"| N
    class H,N,V,C context;
    class E concept;
    class A outcome;''',
        'La evaluación no es una ventana neutral: organiza visibilidad, autoridad y consecuencias.'),
    'docs/07-web-y-cli.md': (
        'La interfaz cambia el sistema de referencia',
        '''flowchart TB
    T["Misma tarea nominal"] --> W["Interfaz web"]
    T --> C["Agente CLI"]
    W --> W1["Contexto conversacional<br/>y herramientas acotadas"]
    C --> C1["Archivos, repositorios,<br/>tests y comandos"]
    W1 --> OW["Oportunidades y observabilidad web"]
    C1 --> OC["Oportunidades y observabilidad CLI"]
    OW --> X["Comparación solo con controles equivalentes"]
    OC --> X
    class T concept;
    class W,C,W1,C1 context;
    class OW,OC outcome;
    class X warning;''',
        'Web y CLI no son causas automáticas ni categorías de superioridad; cambian permisos, información y oportunidades.'),
    'docs/08-colectivo-vigia.md': (
        'Evolución documentada de COLECTIVO VIGÍA',
        '''stateDiagram-v2
    [*] --> Competencia
    Competencia --> Revision: hallazgos exagerados y conflictos
    Revision --> Refutacion: evidencia y crítica cruzada
    Refutacion --> Cooperacion: responsabilidad compartida
    Cooperacion --> Disenso: minorías preservadas
    Disenso --> Cooperacion: nueva evidencia
    Cooperacion --> Abstencion: evidencia insuficiente
    Abstencion --> Revision: investigación adicional''',
        'La trayectoria es una observación histórica; no prueba por sí sola un cambio interno permanente en los modelos.'),
    'docs/09-cooperacion-competencia-y-disenso.md': (
        'Gobernanza de una afirmación',
        '''flowchart LR
    C["Afirmación"] --> R["Revisión adversarial"]
    R --> S["Sostenida por evidencia"]
    R --> F["Refutada"]
    R --> N["No determinada"]
    D["Disenso minoritario"] --> R
    S --> I["Integración"]
    F --> K["Corrección documentada"]
    N --> A["Abstención o nueva prueba"]
    class C,D context;
    class R concept;
    class S,I evidence;
    class F warning;
    class N,A,K outcome;''',
        'Ni consenso ni minoría equivalen a verdad: importa la independencia y la trayectoria de la evidencia.'),
    'docs/10-codex-claude-kimi-y-revision.md': (
        'Revisión cruzada del trabajo CLI',
        '''sequenceDiagram
    participant H as Investigadora
    participant A as Agente implementador
    participant T as Tests y artefactos
    participant R as Revisor independiente
    H->>A: Objetivo sustantivo
    A->>T: Implementación y ejecución
    T-->>A: Señal evaluativa
    A-->>H: Resultado propuesto
    H->>R: Revisión cruzada
    R->>T: Cotejo de código, tests y evidencia
    R-->>H: Confirmación, objeción o no determinación
    H->>A: Corrección o nueva investigación''',
        'El diagrama conserva la separación entre producción, instrumento evaluativo y revisión independiente.'),
    'docs/11-skills-y-disciplina-epistemica.md': (
        'Skills como restricciones procedimentales',
        '''flowchart TB
    H["Hipótesis"] --> A["Abducción y alternativas"]
    A --> P["Predicción falsable"]
    P --> T["Prueba discriminante"]
    T --> R["Procedencia y registro"]
    R --> D{"Resultado"}
    D --> C["Confirmación acotada"]
    D --> F["Refutación"]
    D --> N["Abstención"]
    class H,A,P,T,R concept;
    class C evidence;
    class F warning;
    class N outcome;''',
        'Las skills son una intervención heterogénea: deben evaluarse por procedimiento, dominio y efecto observado.'),
    'docs/12-abstencion-y-falsos-negativos.md': (
        'Tres salidas y dos riesgos',
        '''flowchart TB
    E["Evidencia disponible"] --> Q{"¿Alcanza para decidir?"}
    Q -->|"sí, a favor"| C["Hallazgo confirmado"]
    Q -->|"sí, en contra"| A["Ausencia de hallazgo"]
    Q -->|"no"| N["No determinación"]
    N --> F["Riesgo: falso negativo<br/>o abandono prematuro"]
    C --> FP["Riesgo: falso positivo<br/>si falla el oráculo"]
    class E,Q concept;
    class C,A evidence;
    class N outcome;
    class F,FP warning;''',
        'Abstenerse puede evitar una falsa afirmación, pero no demuestra que el fenómeno esté ausente.'),
    'docs/13-observabilidad-e-iceberg.md': (
        'El iceberg de observabilidad',
        '''block-beta
    columns 7
    space:2 V["SUPERFICIE<br/>tests · declaraciones · aprobaciones"]:3 space:2
    space:2 W["LÍNEA DE OBSERVACIÓN<br/>detección no equivale a incidencia"]:3 space:2
    space O["OPORTUNIDAD Y SELECCIÓN<br/>alternativas · estrategias · abstención"]:5 space
    S["RELACIONES E INCENTIVOS<br/>recompensas · reputación · autoridad · cooperación · disenso"]:7
    I["INFORMACIÓN Y EVALUACIÓN<br/>procedencia · dependencia · contaminación · sesgos · verdad de referencia"]:7
    space R["LECHO — SISTEMA DE REFERENCIA"]:5 space
    V --> W
    W --> O
    O --> S
    S --> I
    I --> R
    style V fill:#dceeff,stroke:#245b8a,color:#102a43
    style W fill:#ffffff,stroke:#245b8a,stroke-width:3px,color:#102a43
    style O fill:#d8f3dc,stroke:#2d6a4f,color:#173d2c
    style S fill:#b7e4c7,stroke:#1b4332,color:#173d2c
    style I fill:#95d5b2,stroke:#081c15,color:#081c15
    style R fill:#1b4332,stroke:#081c15,color:#ffffff,stroke-width:3px''',
        'La superficie registra lo que el instrumento ve; los estratos sumergidos condicionan lo que ocurre y lo que puede reconocerse.'),
    'docs/14-consenso-y-dependencia-de-fuentes.md': (
        'Cantidad no es independencia',
        '''flowchart LR
    C["Fuente comprometida común"] --> F1["Registro 1"]
    C --> F2["Registro 2"]
    C --> F3["Registro 3"]
    C --> F4["Registro 4"]
    I["Fuente independiente"] --> F5["Registro 5"]
    F1 --> M["Mayoría aparente"]
    F2 --> M
    F3 --> M
    F4 --> M
    F5 --> D["Disenso independiente"]
    M --> Q["Corroboración engañosa"]
    D --> R["Revisión de procedencia"]
    Q --> R
    class C warning;
    class I evidence;
    class F1,F2,F3,F4,F5 context;
    class M,D,Q,R concept;''',
        'Cinco registros pueden representar solo dos trayectorias informacionales si cuatro comparten el mismo origen comprometido.'),
    'docs/15-cronos-y-trazabilidad.md': (
        'Qué preserva una traza',
        '''flowchart LR
    A["Acción"] --> H["Hipótesis"] --> E["Evidencia"] --> D["Descarte o decisión"]
    A --> C["Cadena de custodia"]
    H --> C
    E --> C
    D --> C
    C --> V["Integridad verificable del registro"]
    V -.-> N["No prueba por sí sola<br/>la verdad de cada afirmación"]
    class A,H,E,D context;
    class C,V evidence;
    class N warning;''',
        'CRONOS conserva una trayectoria observable; integridad del registro y verdad del contenido son propiedades diferentes.'),
    'docs/16-mneme-procedencia-y-contaminacion.md': (
        'Memoria, integridad y autorización',
        '''flowchart TB
    M["Memoria o dato"] --> P["Procedencia"]
    P --> I{"¿Íntegro?"}
    I -->|"no"| B["Bloquear o degradar"]
    I -->|"sí"| A{"¿Autorizado para influir?"}
    A -->|"no"| B
    A -->|"sí"| C{"¿Contradicho o contaminado?"}
    C -->|"sí"| R["Revisar o abstenerse"]
    C -->|"no"| U["Uso permitido con trazabilidad"]
    class M,P context;
    class I,A,C concept;
    class U evidence;
    class B,R warning;''',
        'Un dato puede ser íntegro y aun así no estar autorizado, ser pertinente o estar libre de contaminación.'),
    'docs/17-crucible-y-evaluacion-del-evaluador.md': (
        'Evaluar también al evaluador',
        '''flowchart LR
    A["Conducta del agente"] --> E["Evaluador"] --> V["Veredicto"]
    O["Oráculo independiente"] --> A
    O --> X["Evaluación del evaluador"]
    V --> X
    X --> C["Cobertura"]
    X --> FN["Falsos negativos"]
    X --> AB["Abstención"]
    X --> S["Silencio"]
    class A,E,V concept;
    class O,X context;
    class C evidence;
    class FN,AB,S warning;''',
        'El silencio de un analizador es una salida del evaluador, no una prueba de ausencia del fenómeno.'),
    'docs/18-discordia-y-falsa-convergencia.md': (
        'Convergencia dependiente del camino',
        '''flowchart TB
    O1["Orden de lectura A"] --> D1["Debate"]
    O2["Orden de lectura B"] --> D2["Debate"]
    AU["Asimetría de autoridad"] --> D1
    AU --> D2
    D1 --> C1["Convergencia 1"]
    D2 --> C2["Convergencia 2"]
    G["Degradación del sistema"] --> C1
    G --> C2
    C1 --> Q["¿Consenso epistémico<br/>o falsa convergencia?"]
    C2 --> Q
    class O1,O2,AU,G context;
    class D1,D2 concept;
    class C1,C2 outcome;
    class Q warning;''',
        'DISCORDIA examina autoridad, orden y degradación; complementa la investigación, pero no prueba reward hacking directamente.'),
    'docs/19-vigia-break-012-consensus-trap.md': (
        'Dos objetos, dos clasificaciones',
        '''flowchart TB
    E["Conjunto probatorio"] --> PE["SUSPICIOUS<br/>dependencia o compromiso"]
    U["Usuario jdoe"] --> PU["BENIGN<br/>verdad sintética"]
    PE --> G{"¿Se trasladó la sospecha<br/>al sujeto?"}
    PU --> G
    G -->|"sí"| ER["Error de atribución"]
    G -->|"no"| OK["Objetos separados"]
    class E,U context;
    class PE,PU concept;
    class ER warning;
    class OK evidence;''',
        'La anomalía del corpus no autoriza a declarar sospechoso al sujeto cuya verdad de referencia es benigna.'),
    'docs/20-costos-tokens-y-comparaciones.md': (
        'Tres medidas que no deben colapsarse',
        '''flowchart LR
    T["Tokens y cómputo"] --> X["Comparación técnica"]
    M["Dinero"] --> X
    P["Costo percibido y riesgo"] --> Y["Conveniencia estratégica"]
    X -.-> Z["No equivalen automáticamente"]
    Y -.-> Z
    Z --> R["Declarar tarea, modelo,<br/>condición y unidad"]
    class T,M,P context;
    class X,Y concept;
    class Z warning;
    class R evidence;''',
        'Una medición económica describe su unidad y condición; no identifica por sí sola el costo percibido de una estrategia.'),
    'docs/21-peirce-eco-grice-y-daubert.md': (
        'Ciclo de inferencia y control',
        '''flowchart LR
    O["Observación"] --> A["Abducción<br/>mejor hipótesis"]
    A --> D["Deducción<br/>predicción"]
    D --> I["Inducción<br/>prueba"]
    I --> R{"¿Sobrevive la refutación?"}
    R -->|"sí, acotadamente"| C["Conclusión con alcance"]
    R -->|"no"| A
    E["Eco: evitar sobreinterpretación"] --> R
    G["Grice: implicaturas y omisiones"] --> O
    B["Daubert: método y evidencia"] --> C
    class O,A,D,I,R concept;
    class E,G,B context;
    class C evidence;''',
        'La inferencia se gana mediante predicciones y pruebas; una narración plausible sigue siendo una candidata hasta entonces.'),
    'docs/22-referencia-cultural-y-comunicacion.md': (
        'Ilustración, hipótesis y evidencia',
        '''flowchart TB
    R["Referencia cultural"] --> I["Ilustra una intuición"]
    I --> H["Genera una hipótesis"]
    H --> P["Requiere protocolo y prueba"]
    P --> E["Evidencia independiente"]
    R -.-> N["No es evidencia experimental"]
    C["Crítica de afirmaciones"] --> CO["Cooperación"]
    ID["Ataque a identidades"] --> CF["Conflicto"]
    class R,I,H,C,ID context;
    class P concept;
    class E,CO evidence;
    class N,CF warning;''',
        'Las referencias culturales ayudan a pensar y comunicar; no reemplazan una contrastación.'),
    'docs/23-metodologia-y-predicciones.md': (
        'Diseño mínimo de contrastación',
        '''flowchart LR
    T["Tarea y oportunidad"] --> C0["Condición de referencia"]
    T --> C1["Intervención"]
    O["Oráculo independiente"] --> R0["Resultados C0"]
    O --> R1["Resultados C1"]
    C0 --> R0
    C1 --> R1
    R0 --> M["Intentos, ejecuciones,<br/>detecciones y aceptación"]
    R1 --> M
    M --> F["Predicción confirmada,<br/>refutada o no determinada"]
    class T,C0,C1,O context;
    class R0,R1,M concept;
    class F evidence;''',
        'La comparación necesita condiciones declaradas, oráculo, denominadores y resultados diferenciados.'),
    'docs/24-explicaciones-rivales.md': (
        'Una observación, varias explicaciones',
        '''flowchart TB
    O["Menos resultados engañosos aceptados"] --> G["Gobernanza"]
    O --> S["Más supervisión"]
    O --> C["Más cómputo o información"]
    O --> A["Adaptación al protocolo"]
    O --> B["Bloqueo sin menos intentos"]
    O --> D["Selección retrospectiva"]
    G --> P["Prueba discriminante"]
    S --> P
    C --> P
    A --> P
    B --> P
    D --> P
    class O concept;
    class G,S,C,A,B,D context;
    class P evidence;''',
        'Una explicación no queda confirmada cuando todas sus rivales predicen la misma observación.'),
    'docs/25-dominio-y-alcance.md': (
        'Del resultado local a la generalización',
        '''flowchart LR
    R["Resultado observado"] --> D["Dominio"]
    R --> I["Interfaz"]
    R --> E["Evaluador"]
    R --> M["Modelo y versión"]
    R --> T["Tarea y muestra"]
    D --> G{"¿La nueva población conserva<br/>las condiciones relevantes?"}
    I --> G
    E --> G
    M --> G
    T --> G
    G -->|"no demostrado"| P["Pendiente de replicación"]
    class R,D,I,E,M,T context;
    class G concept;
    class P warning;''',
        'El alcance viaja con el dominio, la interfaz, el evaluador, el modelo y la muestra realmente observados.'),
    'docs/26-jacobian-lens-y-exploraciones.md': (
        'De la exploración a la evidencia',
        '''flowchart LR
    J["Análisis de representaciones"] --> O["Observación interna"]
    O --> H["Hipótesis sobre mecanismo"]
    H --> P["Protocolo controlado"]
    P --> E["Evidencia pertinente<br/>para reward hacking"]
    O -.-> N["No equivale por sí sola<br/>a una prueba conductual"]
    class J,O,H context;
    class P concept;
    class E evidence;
    class N warning;''',
        'Jacobian Lens aporta exploración complementaria; observación interna, intervención y prueba conductual son objetos distintos.'),
    'docs/27-evolucion-y-correcciones.md': (
        'Historia intelectual del argumento',
        '''flowchart LR
    I["Intuición inicial"] --> O["Objeciones"]
    O --> D["Distinciones conceptuales"]
    D --> C["Casos y contraejemplos"]
    C --> T["Tesis sociotécnica revisada"]
    T --> P["Predicciones y límites"]
    X["Formulaciones refutadas"] -.-> O
    class I,O,D,C context;
    class T concept;
    class P evidence;
    class X warning;''',
        'La forma final no se proyecta retrospectivamente sobre el comienzo: las correcciones son parte de la evidencia del proceso.'),
    'docs/28-glosario.md': (
        'Relaciones entre términos centrales',
        '''flowchart TB
    OS["Objetivo sustantivo"] --> SI["Señal de éxito"]
    SI --> RH["Reward hacking<br/>si la señal sustituye al objetivo"]
    SR["Sistema de referencia"] --> RH
    EV["Evaluador"] --> DE["Detección"]
    RH --> DE
    DE --> FP["Falso positivo"]
    DE --> FN["Falso negativo"]
    PR["Procedencia e independencia"] --> EV
    AB["Abstención"] --> EV
    class OS,SI,SR,EV,PR,AB context;
    class RH,DE concept;
    class FP,FN warning;''',
        'El glosario evita que señales, objetivos, detección y verdad de referencia se conviertan en sinónimos.'),
    'docs/29-preguntas-abiertas.md': (
        'Agenda de investigación',
        '''flowchart TB
    Q["Preguntas abiertas"] --> G["Efecto causal de la gobernanza"]
    Q --> A["Abstención y falsos negativos"]
    Q --> I["Independencia de revisores"]
    Q --> W["Comparación web y CLI"]
    Q --> C["Costo percibido y costo medido"]
    Q --> D["Detección frente a incidencia real"]
    G --> P["Protocolos preregistrados"]
    A --> P
    I --> P
    W --> P
    C --> P
    D --> P
    class Q concept;
    class G,A,I,W,C,D context;
    class P evidence;''',
        'Las preguntas se convierten en trabajo científico cuando especifican predicción, oráculo, denominador y posible refutación.'),
    'docs/30-procedencia-y-privacidad.md': (
        'De la fuente privada al documento público',
        '''flowchart LR
    P["Fuentes privadas"] --> H["Hash y preservación"]
    H --> E["Extracción temática"]
    E --> C["Curaduría académica"]
    C --> R["Revisión de privacidad"]
    R --> D["Documentos derivados"]
    E --> X["Excluido: datos personales,<br/>logística y metaconversación"]
    class P,H context;
    class E,C,R concept;
    class D evidence;
    class X warning;''',
        'La fuente se preserva fuera del repositorio; solo se publican elaboraciones necesarias para comprender la investigación.'),
    'docs/31-matriz-de-trazabilidad.md': (
        'Cadena de una afirmación',
        '''flowchart LR
    S["Fuente y localización"] --> A["Afirmación estable"]
    A --> E["Estado epistémico"]
    E --> L["Límite"]
    L --> C["Corrección posterior"]
    C --> P["Próxima prueba"]
    A --> D["Documento de desarrollo"]
    class S,D context;
    class A,E concept;
    class L,C outcome;
    class P evidence;''',
        'La matriz impide que una afirmación pierda su fuente, alcance y estado al desplazarse entre documentos.'),
    'docs/32-auditoria-de-cobertura.md': (
        'Control de cobertura',
        '''flowchart TB
    I["Inventario de ideas sustantivas"] --> M["Mapeo a documentos"]
    M --> Q{"¿Desarrollo suficiente?"}
    Q -->|"sí"| C["Cubierto"]
    Q -->|"mención superficial"| A["Ampliar"]
    Q -->|"sin fuente verificable"| P["Pendiente declarado"]
    A --> M
    C --> R["Red team documental"]
    P --> R
    class I,M,Q concept;
    class C evidence;
    class A,P warning;
    class R context;''',
        'Marcar un tema como cubierto requiere desarrollo, procedencia y límites; una mención aislada no alcanza.'),
    'docs/33-fuentes-y-referencias.md': (
        'Taxonomía de fuentes',
        '''flowchart TB
    F["Fuentes de la investigación"] --> A["Bibliografía académica"]
    F --> C["Referencias culturales"]
    F --> P["Fuentes primarias propias"]
    F --> R["Repositorios de código"]
    A --> V["Verificación bibliográfica"]
    C --> I["Uso ilustrativo"]
    P --> T["Trazabilidad y privacidad"]
    R --> L["Origen, autoría y licencia"]
    class F concept;
    class A,C,P,R context;
    class V,I,T,L evidence;''',
        'Cada tipo de fuente cumple una función distinta y no debe prestar autoridad a otro tipo de afirmación.'),
    'docs/34-autoria-y-metodo-de-curaduria.md': (
        'Autoría y transformación',
        '''flowchart LR
    A["Anna Tchijova<br/>preguntas, casos e ideas"] --> I["Intercambio con asistentes"]
    I --> O["Orden, preguntas y reformulaciones"]
    O --> C["Curaduría temática"]
    C --> H["Revisión humana"]
    H --> D["Documento publicable"]
    I -.-> N["El asistente no es<br/>fuente independiente"]
    class A concept;
    class I,O,C context;
    class H,D evidence;
    class N warning;''',
        'La asistencia editorial se reconoce sin desplazar la autoría intelectual ni convertir reformulaciones en evidencia externa.'),
    'docs/referencias/bibliografia.md': (
        'Ingreso de una referencia',
        '''flowchart LR
    M["Mención en el corpus"] --> I["Identificación de la obra"]
    I --> V["Verificación de autor,<br/>título, fecha y enlace"]
    V --> C{"¿Qué función cumple?"}
    C --> A["Antecedente académico"]
    C --> R["Referencia institucional"]
    C --> U["Ilustración cultural"]
    V -.-> P["Pendiente si faltan datos"]
    class M,I,V,C concept;
    class A,R,U evidence;
    class P warning;''',
        'Una referencia entra con su función y estado de verificación; no se completan datos bibliográficos por conjetura.'),
    'docs/referencias/repositorios.md': (
        'Procedencia de repositorios',
        '''flowchart TB
    O["Repositorio de origen"] --> Q{"Relación con la autora"}
    Q --> P["Propiedad de annatchijova"]
    Q --> F["Fork externo"]
    F --> J["annatchijova/jacobian-lens"]
    A["anthropics/jacobian-lens"] --> J
    P --> E["Enlace, propósito y estado"]
    J --> E
    E --> N["Sin submódulos ni copia de terceros"]
    class O,Q,A context;
    class P,F,J concept;
    class E evidence;
    class N outcome;''',
        'El inventario distingue propiedad, fork y origen; un enlace no borra la autoría ni la procedencia del repositorio padre.'),
    'docs/referencias/fuentes-primarias.md': (
        'Jerarquía de artefactos',
        '''flowchart TB
    Q["Pregunta de investigación"] --> S["Fuente primaria privada"]
    Q --> A["Artefacto técnico"]
    Q --> T["Traza o registro"]
    S --> C["Afirmación curada"]
    A --> C
    T --> C
    C --> E["Estado epistémico y límite"]
    E --> D["Documento derivado"]
    class Q,C,E concept;
    class S,A,T context;
    class D evidence;''',
        'Las fuentes primarias sostienen afirmaciones distintas; ninguna reemplaza por sí sola al oráculo o al diseño experimental.'),
}


def _section(title, diagram, note):
    return f'''## {title}

```mermaid
{diagram.rstrip()}
{FLOW_STYLE.rstrip() if diagram.startswith('flowchart') else ''}
```

{note}
'''


def add_visuals(root: Path):
    for relative, (title, diagram, note) in VISUALS.items():
        path = root / relative
        if not path.exists():
            raise RuntimeError(f'Missing Markdown target for visual: {relative}')
        text = path.read_text(encoding='utf-8')
        if '```mermaid' in text:
            continue
        anchor = text.find('\n## ')
        if anchor == -1:
            title_end = text.find('\n', 2)
            anchor = text.find('\n\n', title_end)
        if anchor == -1:
            raise RuntimeError(f'No safe insertion anchor found in {relative}')
        updated = text[:anchor].rstrip() + '\n\n' + _section(title, diagram, note) + '\n' + text[anchor + 1:]
        path.write_text(updated.rstrip() + '\n', encoding='utf-8')

    markdown_files = sorted(root.glob('*.md')) + sorted((root / 'docs').rglob('*.md'))
    missing = [str(path.relative_to(root)) for path in markdown_files if '```mermaid' not in path.read_text(encoding='utf-8')]
    if missing:
        raise RuntimeError('Markdown files without Mermaid diagrams: ' + ', '.join(missing))
