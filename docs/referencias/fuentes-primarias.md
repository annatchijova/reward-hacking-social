# Fuentes primarias y artefactos

## Jerarquía de artefactos

```mermaid
flowchart TB
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
    class D evidence;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

Las fuentes primarias sostienen afirmaciones distintas; ninguna reemplaza por sí sola al oráculo o al diseño experimental.

## Material privado

- `Downloads/reward_hacking.md` — fuente primaria privada de la extracción; no publicada.
- `Downloads/prompt.md` — instrucciones privadas de trabajo; no publicada.
- `Downloads/discordia.md` — material privado complementario; no publicado como documento crudo.

## Artefactos externos

- [VIGÍA](https://github.com/annatchijova/vigia-intent-analysis)
- [CRONOS](https://github.com/annatchijova/cronos)
- [MNEME](https://github.com/annatchijova/mneme)
- [CRUCIBLE](https://github.com/annatchijova/crucible) — pendiente de confirmar el repositorio exacto.
- [DISCORDIA](https://github.com/annatchijova/discordia)
- [Jacobian Lens](https://github.com/anthropics/jacobian-lens)
