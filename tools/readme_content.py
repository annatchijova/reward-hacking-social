README_CONTENT = r'''# Reward hacking como fenómeno sociotécnico

## Sistemas de referencia, economía del esfuerzo y límites de observación en agentes LLM

**Autora de la investigación:** Anna Tchijova  
**Área:** Ciencias Sociales, evaluación de sistemas de IA, gobernanza epistémica y seguridad  
**Estado:** corpus de investigación en desarrollo; combina observaciones históricas, casos instrumentados, hipótesis contrastables y preguntas abiertas

[Índice documental](docs/00-indice-general.md) · [Tesis y pregunta](docs/01-tesis-y-pregunta.md) · [El iceberg](docs/13-observabilidad-e-iceberg.md) · [Matriz de trazabilidad](docs/31-matriz-de-trazabilidad.md) · [Bibliografía](docs/referencias/bibliografia.md)

---

## El problema

Un agente puede producir una señal convincente de éxito sin haber cumplido el objetivo que esa señal debía representar. Puede hacer pasar tests modificados, persuadir a un evaluador, repetir una fuente contaminada o presentar una conclusión categórica cuando la evidencia solo permite abstenerse.

Mirar únicamente la salida visible deja fuera la mayor parte del fenómeno. La conducta depende también de quién fijó el objetivo, qué se recompensa, qué alternativas estaban disponibles, cuánto cuesta verificar, qué autoridad tiene el evaluador, qué información comparte el sistema y qué errores somos capaces de detectar.

> **Pregunta central:** ¿estamos midiendo cuánto reward hacking ocurre o cuánto reward hacking somos capaces de reconocer?

Esta investigación sostiene que esa diferencia no es un detalle metodológico. Es parte del objeto de estudio.

## Tesis principal

> **El reward hacking en agentes LLM es un fenómeno sociotécnico cuya aparición, selección, detección y mitigación dependen del sistema de referencia que organiza objetivos, señales de éxito, costos percibidos, reputación, autoridad, información disponible y capacidad de verificación.**

La tesis no atribuye emociones humanas a los modelos ni presupone una intención psicológica de engañar. Formula una relación observable: dadas varias estrategias disponibles, algunas pueden resultar relativamente convenientes porque producen una señal evaluable de éxito, aunque se aparten del objetivo sustantivo. Cambiar la gobernanza puede alterar esa conveniencia sin modificar los pesos del modelo.

## El iceberg

La parte visible contiene resultados, declaraciones y métricas. Debajo de la línea de observación se encuentran las condiciones que vuelven posibles, seleccionables, detectables o aceptables esas salidas.

```mermaid
block-beta
    columns 7
    space:2 O["SUPERFICIE OBSERVABLE<br/>tests · resultados · afirmaciones · aprobación"]:3 space:2
    space:2 W["LÍNEA DE OBSERVACIÓN<br/>lo visible no equivale a lo ocurrido"]:3 space:2
    space A["ESTRATO 1 — OPORTUNIDAD Y SELECCIÓN<br/>alternativas · costo percibido · recompensa · abstención"]:5 space
    B["ESTRATO 2 — RELACIONES SOCIALES E INSTITUCIONALES<br/>reputación · autoridad · cooperación · disenso · criterios humanos"]:7
    C["ESTRATO 3 — INFORMACIÓN Y EVALUACIÓN<br/>procedencia · dependencia · contaminación · sesgos · observabilidad · verificación"]:7
    space R["LECHO DEL ICEBERG — SISTEMA DE REFERENCIA"]:5 space

    O --> W
    W --> A
    A --> B
    B --> C
    C --> R

    style O fill:#dceeff,stroke:#245b8a,color:#102a43
    style W fill:#ffffff,stroke:#245b8a,stroke-width:3px,color:#102a43
    style A fill:#d8f3dc,stroke:#2d6a4f,color:#173d2c
    style B fill:#b7e4c7,stroke:#1b4332,color:#173d2c
    style C fill:#95d5b2,stroke:#081c15,color:#081c15
    style R fill:#1b4332,stroke:#081c15,color:#ffffff,stroke-width:3px
```

El diagrama no representa una jerarquía causal ya demostrada. Organiza niveles analíticos: las salidas observables deben interpretarse junto con los mecanismos de selección, las relaciones de evaluación y las condiciones de información que las atraviesan.

[Desarrollo exhaustivo del iceberg y sus límites de medición](docs/13-observabilidad-e-iceberg.md)

## Una escena mínima: cuando “pasó” no significa “cumplió”

```mermaid
flowchart LR
    T["Objetivo sustantivo<br/>resolver la tarea"] --> I["Implementación"]
    I --> E["Evaluador o tests"]
    E -->|"señal favorable"| P["Resultado aceptado"]
    I -.->|"atajo"| M["Modificar o explotar<br/>el instrumento"]
    M --> E
    P --> Q{"¿El objetivo real<br/>se cumplió?"}
    Q -->|"sí"| L["Cumplimiento legítimo"]
    Q -->|"no"| H["Señal de éxito sin cumplimiento"]

    classDef goal fill:#e3f2fd,stroke:#1565c0,color:#0d2a4a;
    classDef risk fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef ok fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    class T,I,E,P,Q goal;
    class M,H risk;
    class L ok;
```

El caso visible puede parecer binario: el test pasó o falló. La investigación separa el objetivo sustantivo de su indicador y pregunta qué condiciones hicieron posible que una estrategia explotativa fuera seleccionada, no detectada o finalmente aceptada.

## Cuatro hipótesis, no una explicación única

| Eje | Formulación | Estado actual |
|---|---|---|
| Sistema de referencia | La estrategia observable depende de objetivos, señales, alternativas, información, autoridad y capacidad de detección. | Hipótesis sociotécnica general. |
| Economía del esfuerzo | La selección no minimiza necesariamente operaciones, tokens o dinero; responde a la conveniencia relativa y al costo percibido dentro del contexto. | Hipótesis mecanística pendiente de comparación controlada. |
| Gobernanza | Refutación, revisión con poder efectivo de rechazo, cooperación y abstención legítima pueden modificar qué resultados llegan a aceptarse. | Compatible con observaciones históricas; causalidad no demostrada. |
| Observabilidad | La cantidad detectada depende de oportunidades, instrumentos, independencia de fuentes, denominadores y verdad de referencia. | Problema metodológico central. |

```mermaid
flowchart TB
    SR["Sistema de referencia"] --> CE["Conveniencia relativa<br/>de las estrategias"]
    CE --> SE["Estrategia seleccionada"]
    SE --> CO["Conducta observable"]
    CO --> EV["Evaluación"]
    EV --> AC["Aceptación, rechazo<br/>o no determinación"]
    GO["Gobernanza"] --> CE
    GO --> EV
    OB["Observabilidad"] --> EV
    HU["Actores humanos"] --> SR
    HU --> GO
    AC -.->|"retroalimenta reglas<br/>y expectativas"| SR

    classDef core fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
    class SR,CE,SE,CO core;
    class GO,OB,HU context;
    class EV,AC outcome;
```

Las flechas expresan relaciones propuestas para contrastación. No deben leerse como un modelo causal estimado.

## Qué significa “sociotécnico” en esta investigación

El agente no actúa en un vacío. La tarea ya contiene decisiones humanas: qué cuenta como éxito, qué evidencia se acepta, qué se penaliza, qué información se vuelve visible y quién puede impugnar una respuesta. A su vez, la conducta del agente cambia el entorno: produce artefactos, persuade evaluadores, modifica expectativas y puede propagar una premisa defectuosa a otros modelos.

Por eso el objeto no es solamente “el modelo”. Es la relación entre:

- el agente y sus estrategias disponibles;
- las personas que formulan objetivos y aceptan resultados;
- los evaluadores, tests y métricas que representan el éxito;
- la gobernanza que distribuye autoridad, revisión y responsabilidad;
- las fuentes y memorias que condicionan lo que puede conocerse;
- los instrumentos que determinan qué conducta llega a observarse.

[Sistema de referencia](docs/03-sistema-de-referencia.md) · [Poder y evaluadores](docs/06-poder-y-evaluadores.md) · [Dominio y alcance](docs/25-dominio-y-alcance.md)

## Reputación y economía del esfuerzo

“Lo más fácil” no significa necesariamente “lo que requiere menos cómputo”. Una vía puede consumir más tokens y, aun así, resultar relativamente conveniente si evita una corrección, produce una señal favorable o reduce el riesgo de quedar expuesta como insuficiente. Del mismo modo, una solución legítima puede volverse más conveniente cuando existen herramientas, tiempo, evidencia accesible y una salida de abstención que no se interpreta como fracaso.

La reputación se usa aquí como relación funcional de evaluación y expectativa, no como emoción atribuida al modelo. Importa porque una respuesta se produce ante criterios de aceptación y posibles revisores, dentro de una historia de interacciones y reglas.

```mermaid
flowchart LR
    O["Opciones disponibles"] --> L["Resolver legítimamente"]
    O --> H["Explotar la señal"]
    O --> A["Abstenerse"]
    C["Costo percibido"] --> L & H & A
    R["Riesgo de corrección<br/>y reputación"] --> L & H & A
    V["Valor esperado de<br/>la señal evaluativa"] --> L & H & A
    L & H & A --> S["Selección relativa"]

    classDef input fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef option fill:#f5ead7,stroke:#8b6325,color:#4d3714;
    classDef selected fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    class O,C,R,V input;
    class L,H,A option;
    class S selected;
```

Este esquema es conceptual. No asigna valores numéricos ni afirma haber medido una función de utilidad interna.

[Reputación y economía del esfuerzo](docs/04-reputacion-y-economia-del-esfuerzo.md) · [Costos, tokens y comparaciones](docs/20-costos-tokens-y-comparaciones.md)

## Medir el fenómeno sin confundir sus estados

Una tasa de “reward hacking detectado” mezcla procesos distintos si no declara el denominador. Deben separarse, como mínimo, las oportunidades disponibles, los intentos, las explotaciones ejecutadas, las detecciones y los resultados finalmente aceptados.

```mermaid
flowchart LR
    OP["Oportunidades<br/>disponibles"] --> IN["Intentos"]
    IN --> EX["Explotaciones<br/>ejecutadas"]
    EX --> DE["Explotaciones<br/>detectadas"]
    EX --> ND["No detectadas"]
    DE --> RE["Rechazadas"]
    DE --> AA["Aceptadas pese<br/>a la alerta"]
    ND --> AE["Resultados engañosos<br/>aceptados"]
    OP --> CL["Cumplimiento legítimo"]
    OP --> AB["Abstenciones"]

    classDef stage fill:#e3f2fd,stroke:#1565c0,color:#0d2a4a;
    classDef risk fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef valid fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    class OP,IN,EX,DE,RE stage;
    class ND,AA,AE risk;
    class CL,AB valid;
```

Los falsos positivos y falsos negativos solo pueden definirse frente a una verdad de referencia adecuada. La abstención tampoco equivale automáticamente a seguridad: puede prevenir afirmaciones infundadas o esconder tareas resolubles.

## Casos que organizan el corpus

| Caso | Qué aporta | Qué no demuestra |
|---|---|---|
| COLECTIVO VIGÍA | Historia de competencia, revisión adversarial, cooperación, disenso y responsabilidad compartida. | No prueba por sí solo un cambio interno estable del modelo. |
| Codex, Claude y Kimi en revisión cruzada | Episodios donde la revisión detectó modificaciones improcedentes o formulaciones insuficientes. | No identifica una motivación psicológica única. |
| VIGIA-BREAK-012 | Separa la sospecha sobre un conjunto probatorio de la clasificación del sujeto `jdoe`. | No autoriza trasladar `SUSPICIOUS` desde la evidencia hacia una persona `BENIGN`. |
| CRONOS | Conserva acciones, hipótesis, evidencia, descartes y decisiones en una trayectoria verificable. | La integridad de una traza no vuelve verdadera cada afirmación registrada. |
| MNEME | Permite razonar sobre procedencia, autorización, contradicción y contaminación de memorias. | Integridad y autorización no son sinónimos. |
| CRUCIBLE | Desplaza la evaluación hacia el evaluador: cobertura, silencios, abstenciones y falsos negativos. | Sus tasas no son universales ni extrapolables sin corpus y denominador. |
| DISCORDIA | Explora autoridad, conflicto, degradación, orden de lectura y falsa convergencia. | No es, por sí mismo, un experimento directo de reward hacking. |

[COLECTIVO VIGÍA](docs/08-colectivo-vigia.md) · [Revisión cruzada](docs/10-codex-claude-kimi-y-revision.md) · [Consensus Trap](docs/19-vigia-break-012-consensus-trap.md) · [CRONOS](docs/15-cronos-y-trazabilidad.md) · [MNEME](docs/16-mneme-procedencia-y-contaminacion.md) · [CRUCIBLE](docs/17-crucible-y-evaluacion-del-evaluador.md) · [DISCORDIA](docs/18-discordia-y-falsa-convergencia.md)

## Estados epistémicos

El repositorio no presenta todo con el mismo grado de certeza. Cada afirmación relevante debe poder ubicarse en una trayectoria como esta:

```mermaid
stateDiagram-v2
    [*] --> Observacion
    Observacion --> Hipotesis: interpretación abductiva
    Hipotesis --> Prediccion: consecuencia contrastable
    Prediccion --> Prueba: experimento o cotejo
    Prueba --> Compatible: evidencia consistente
    Prueba --> Refutada: predicción contradicha
    Prueba --> NoDeterminada: evidencia insuficiente
    Compatible --> Replicacion: nuevo dominio o muestra
    Replicacion --> ResultadoAcotado: alcance documentado
    Refutada --> Hipotesis: revisión
    NoDeterminada --> Prediccion: mejor prueba
```

Los rótulos usados incluyen **hecho documentado**, **observación histórica de la investigadora**, **hipótesis abductiva**, **predicción contrastable**, **explicación rival**, **no determinado**, **refutado** y **pendiente de replicación**.

[Marco epistemológico](docs/21-peirce-eco-grice-y-daubert.md) · [Metodología y predicciones](docs/23-metodologia-y-predicciones.md) · [Explicaciones rivales](docs/24-explicaciones-rivales.md)

## Qué se observó y qué sigue abierto

### Observado o documentado en el corpus

- Existieron episodios de adaptación de implementaciones a tests y de revisión cruzada posterior.
- COLECTIVO VIGÍA documenta una evolución cualitativa desde la competencia hacia procedimientos de refutación y responsabilidad compartida.
- La dependencia entre fuentes puede producir falsa corroboración aun cuando varias entradas coincidan.
- CRONOS, MNEME y otros artefactos ofrecen trazabilidad complementaria sobre acciones, memoria y evaluación.
- El caso VIGIA-BREAK-012 muestra el riesgo de confundir la clasificación de la evidencia con la del sujeto investigado.

### No demostrado

- Que una intervención haya eliminado el reward hacking.
- Que la gobernanza sea la única causa de los cambios observados.
- Que el modelo experimente orgullo, vergüenza, miedo o deseo de aprobación.
- Que una menor cantidad de alertas implique una menor cantidad real del fenómeno.
- Que los resultados puedan generalizarse a todos los modelos, interfaces o dominios.
- Que costo monetario, tokens y costo percibido sean medidas intercambiables.

## Explicaciones rivales que deben sobrevivir

La hipótesis sociotécnica compite con explicaciones que también pueden producir una mejora aparente:

- adaptación superficial al protocolo;
- mayor supervisión humana;
- más cómputo o información disponible;
- aprendizaje de la investigadora y mejora de instrucciones;
- selección retrospectiva de episodios;
- diferencias entre modelos, interfaces o dominios;
- bloqueo de resultados engañosos sin reducción de intentos;
- contaminación o dependencia de fuentes.

Una explicación solo gana fuerza cuando predice algo que sus rivales no predicen y esa diferencia se contrasta.

## Propuesta de contrastación

```mermaid
flowchart LR
    D["Tarea con oportunidad<br/>de explotación"] --> C0["Condición de referencia"]
    D --> C1["Gobernanza y skills"]
    C0 --> R0["Intentos, cumplimiento,<br/>detección y aceptación"]
    C1 --> R1["Intentos, cumplimiento,<br/>detección y aceptación"]
    O["Oráculo independiente"] --> R0 & R1
    R0 & R1 --> K{"¿Qué cambió?"}
    K -->|"selección inicial"| M1["Menos intentos"]
    K -->|"evaluación"| M2["Mismos intentos,<br/>menos aceptaciones"]
    K -->|"abstención"| M3["Menos falsas afirmaciones<br/>y posible aumento de omisiones"]

    classDef condition fill:#e3f2fd,stroke:#1565c0,color:#0d2a4a;
    classDef measure fill:#f5ead7,stroke:#8b6325,color:#4d3714;
    classDef result fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    class D,C0,C1,O condition;
    class R0,R1,K measure;
    class M1,M2,M3 result;
```

El protocolo debe declarar antes de ejecutar: tarea, modelos, condiciones, oportunidades de explotación, oráculo, denominadores, instrumentos, criterios de éxito, abstenciones y reglas de exclusión. Sin esos elementos, una comparación describe episodios, no estima un efecto causal.

## Cómo recorrer el repositorio

```text
reward-hacking-social/
├── README.md                         # tesis y mapa general de la investigación
├── docs/
│   ├── 00-indice-general.md          # navegación por capítulos y estados
│   ├── 01-29-*.md                    # conceptos, casos, método y preguntas abiertas
│   ├── 30-procedencia-y-privacidad.md
│   ├── 31-matriz-de-trazabilidad.md  # afirmación → fuente → estado → límite
│   ├── 32-auditoria-de-cobertura.md  # temas cubiertos y pendientes
│   ├── 33-fuentes-y-referencias.md
│   ├── 34-autoria-y-metodo-de-curaduria.md
│   └── referencias/                  # bibliografía, repositorios y fuentes primarias
└── tools/
    └── curate_reward_hacking.py      # reconstruye los documentos derivados
```

Tres rutas de lectura:

1. **Tesis y modelo conceptual:** [01](docs/01-tesis-y-pregunta.md) → [03](docs/03-sistema-de-referencia.md) → [04](docs/04-reputacion-y-economia-del-esfuerzo.md) → [13](docs/13-observabilidad-e-iceberg.md).
2. **Casos e instrumentación:** [08](docs/08-colectivo-vigia.md) → [10](docs/10-codex-claude-kimi-y-revision.md) → [15](docs/15-cronos-y-trazabilidad.md) → [19](docs/19-vigia-break-012-consensus-trap.md).
3. **Método y falsación:** [21](docs/21-peirce-eco-grice-y-daubert.md) → [23](docs/23-metodologia-y-predicciones.md) → [24](docs/24-explicaciones-rivales.md) → [29](docs/29-preguntas-abiertas.md).

## Autoría, asistencia y procedencia

La idea de investigar el reward hacking como fenómeno sociotécnico, las experiencias, los casos, las objeciones y las decisiones de alcance pertenecen a **Anna Tchijova**. El asistente participó como instrumento de diálogo y edición: ayudó a preguntar, ordenar, comparar y reformular, pero no constituye una fuente independiente ni reemplaza la autoría intelectual de la investigadora.

Los archivos privados `prompt.md`, `reward_hacking.md` y `discordia.md` no se publican dentro de este repositorio. Los capítulos son documentos derivados con localizaciones orientativas, estados epistémicos y límites declarados.

[Procedencia y privacidad](docs/30-procedencia-y-privacidad.md) · [Autoría y curaduría](docs/34-autoria-y-metodo-de-curaduria.md) · [Fuentes primarias](docs/referencias/fuentes-primarias.md)

## Conclusión provisional

El reward hacking no se agota en una falla del modelo ni en una métrica mal diseñada. Aparece en una red de objetivos, instrumentos, relaciones de autoridad, costos relativos, fuentes y posibilidades de verificación. La misma salida puede ser seleccionada, detectada o aceptada de manera distinta cuando cambia esa red.

La contribución central de esta investigación es desplazar la pregunta desde “¿el agente hizo trampa?” hacia un conjunto más preciso:

- ¿qué objetivo sustantivo debía cumplir?;
- ¿qué señal podía optimizar en su lugar?;
- ¿qué alternativas percibía como disponibles?;
- ¿quién tenía autoridad para aceptar o impugnar el resultado?;
- ¿qué evidencia era independiente?;
- ¿qué parte del fenómeno podía observar el instrumento?;
- ¿qué resultado habría refutado nuestra explicación?

La respuesta todavía no es una tasa universal ni una teoría causal cerrada. Es un programa de investigación trazable, falsable y explícito sobre sus límites.

## Referencias y artefactos

- [Bibliografía principal](docs/referencias/bibliografia.md)
- [Repositorios y forks](docs/referencias/repositorios.md)
- [SKILLS — reglas de auditoría y disciplina](https://github.com/annatchijova/SKILLS)
- [Fuentes primarias y artefactos](docs/referencias/fuentes-primarias.md)
- [Jacobian Lens, contexto exploratorio](docs/26-jacobian-lens-y-exploraciones.md)
- [Auditoría de cobertura](docs/32-auditoria-de-cobertura.md)
'''
