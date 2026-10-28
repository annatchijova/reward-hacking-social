# Fuentes y referencias

## Taxonomía de fuentes

```mermaid
flowchart TB
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
    class V,I,T,L evidence;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

Cada tipo de fuente cumple una función distinta y no debe prestar autoridad a otro tipo de afirmación.

## Fuente primaria privada

- `Downloads/reward_hacking.md` — fuente de la extracción temática; no se publica en este repositorio.

## Inventarios navegables

- [Bibliografía](referencias/bibliografia.md)
- [Repositorios y forks](referencias/repositorios.md)
- [Fuentes primarias y artefactos](referencias/fuentes-primarias.md)

## Fuentes mencionadas que requieren verificación

- Repositorios de VIGÍA, CRONOS, MNEME, DISCORDIA y CRUCIBLE.
- Documentación de herramientas y experimentos citados en el corpus.
- Literatura sobre reward hacking, specification gaming, Goodhart, evaluación, abducción y epistemología social.

## Regla

No se agregan autores, DOI, fechas, resultados ni URLs como hechos hasta verificar la fuente correspondiente. Las referencias culturales se mantienen separadas de la bibliografía académica.
