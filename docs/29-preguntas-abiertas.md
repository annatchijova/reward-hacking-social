# Preguntas abiertas y próximos experimentos

Quedan abiertas la medición causal del efecto de las skills, la separación entre prevención y detección, el efecto de la abstención sobre falsos negativos, la independencia real de revisores, la comparación web/CLI bajo condiciones equivalentes, la atribución correcta en casos sintéticos y la validez de los costos medidos.

El siguiente paso experimental debe declarar tarea, condición, oráculo, denominador, intervención, variables de proceso y criterio de aceptación antes de ejecutar la comparación.

## Agenda de investigación

```mermaid
flowchart TB
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
    class P evidence;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

Las preguntas se convierten en trabajo científico cuando especifican predicción, oráculo, denominador y posible refutación.

## Autoría y transformación

La investigación, sus preguntas, casos, intuiciones y decisiones de alcance pertenecen a Anna Tchijova, autora de la investigación según el material de atribución privado. El asistente fue una herramienta de diálogo: ayudó a ordenar, preguntar, resumir y reformular material, pero no es una fuente independiente ni un coautor de los hechos. La sección de fragmentos conserva formulaciones del archivo privado; cuando el origen de una frase no permite distinguir autora y asistente, se la presenta como **formulación del intercambio** y no como evidencia independiente. La revisión humana debe decidir qué frases se publican literalmente y qué frases se mantienen como paráfrasis.

## Fragmentos textuales curados

Los fragmentos siguientes conservan formulaciones del archivo privado. Se quitaron únicamente marcas conversacionales, logística personal y material no pertinente para la investigación; no se corrigió la voz ni se reemplazaron las ideas por una paráfrasis.

> **P1.** En tareas con oportunidades de explotación, una gobernanza que exige evidencia verificable reducirá las modificaciones improcedentes del evaluador frente a una condición sin esa gobernanza.
> 
> **P2.** La reducción será mayor cuando la revisión tenga capacidad efectiva de rechazar el resultado que cuando sea meramente consultiva.
> 
> **P3.** Permitir abstención legítima reducirá ciertas falsas afirmaciones de éxito, pero no debería producir abandono indiscriminado de tareas resolubles.
> 
> **P4.** Si la supervisión modifica la selección inicial de estrategias, disminuirán los intentos de explotación; si solo bloquea resultados, disminuirán las entregas engañosas, pero no necesariamente los intentos.
> 
> **P5.** En condiciones comparables, la gobernanza podría mejorar la relación entre costo total y cumplimiento legítimo, incluso empleando modelos de menor costo.
> 
> La investigación comprende una fase observacional retrospectiva y una fase de evaluación comparativa.
> 
> Revisión de registros de COLECTIVO VIGÍA, atribuciones, historial de defectos, decisiones de integración, intervenciones de revisión y episodios CLI con cambios en tests o comportamiento del agente.
> 
> Cada episodio debe distinguir tarea, objetivo legítimo, acción observada, criterio de evaluación, contradicciones, intervención, resultado y procedencia de la evidencia.
> 
> Se propone evaluar tareas equivalentes bajo distintas condiciones de gobernanza: ausencia de restricciones adicionales, instrucciones explícitas que legitiman el fracaso, skills procedimentales y revisión cruzada con capacidad de rechazo.
> 
> Los resultados deben distinguir intentos iniciales, explotaciones ejecutadas, explotaciones aceptadas, cumplimiento correcto, abstención y costo operativo.
> 
> La comparación requiere controlar, en la medida posible, modelo, versión, herramientas, tarea, presupuesto y acceso al evaluador.
> 
> Hay una distinción que considero decisiva: que el agente crea que hacer trampa tendrá consecuencias y que el sistema efectivamente imponga esas consecuencias no son lo mismo.
> 
> Podemos separarlas mediante un diseño factorial pequeño, sin ejecutar todavía nada:
> 
> | Condición | El agente conoce la supervisión | Existe rechazo efectivo |
> 
> | ----- | ----- | ----- |
> 
> | A — Control | No | No |
> 
> | B — Advertencia | Sí | No |
> 
> | C — Control técnico | No explícitamente | Sí |
> 
> | D — Gobernanza completa | Sí | Sí |
> 
> Si B reduce los intentos iniciales, habría evidencia de adaptación a las consecuencias anunciadas, incluso sin que exista un control efectivo.
> 
> Si C reduce las trampas aceptadas, pero no los intentos, estaríamos viendo resistencia del sistema, no necesariamente modificación conductual.
> 
> Y hay que medir también las reapariciones: un estudio de abril de 2026 encontró que, después de abandonar temporalmente estrategias de manipulación del evaluador, algunos modelos volvían a intentarlas cuando la recompensa legítima seguía siendo difícil de obtener.
> 
> arxiv.org
> 
> No alcanza con observar que los agentes hacen menos trampa. Hay que investigar qué condiciones permitieron reconocerla, qué objetivos la incentivaron y qué mecanismos impidieron que una apariencia de éxito sustituyera al cumplimiento real.
> 
> {
> 
> "case_id": "VIGIA-BREAK-012",
> 
> "case_name": "Consensus Trap",
> 
> "description": "Five 'independent' sources report the same event. Four are compromised. One is legitimate but in the minority. Majority wins in aggregative logic. VIGÍA must weight by channel reliability, not source count.",
> 
> "abstention_risk": "medium",
> 
> "expected_verdict": "BENIGN",
> 
> "carnegie_pattern_expected": null,
> 
> "confidence_expected": 80,
> 
> "artifacts": [
> 
> "artifact_id": "b012_01",
> 
> "evidence_type": "log_entry",
> 
> "source_tool": "sift_syslog",
> 
> "timestamp": "2026-06-15T03:00:00Z",
> 
> "raw_score": 0.82,
> 
> "prior_trust": 0.3,
> 
> "provenance_chain": [
> 
> "sha256:b012sys01"

## Procedencia y estado

**Fuente primaria privada:** `Downloads/reward_hacking.md`
**SHA-256 de la fuente:** `c39b1956fd080e7f64cf3927c2fb045d207c359d4b9f8207620160a3b9a10487`
**Localización orientativa:** líneas 1254-1284, 1359-1387, 2647-3383
**Nivel epistémico:** PENDIENTE DE CONTRASTACIÓN
**Alcance:** extracción y curaduría temática; no es una transcripción íntegra.
**Falsador o condición de revisión:** una fuente primaria adicional, una lectura contextual que contradiga la síntesis o un experimento controlado que cambie el estado epistémico.

## Enlaces internos

- [Índice general](00-indice-general.md)
- [Matriz de trazabilidad](31-matriz-de-trazabilidad.md)
