# Repositorios y forks

## Procedencia de repositorios

```mermaid
flowchart TB
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
    class N outcome;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

El inventario distingue propiedad, fork y origen; un enlace no borra la autoría ni la procedencia del repositorio padre.

## Repositorios de la autora

Estos repositorios ya pertenecen a la cuenta de la autora; GitHub no permite que una cuenta sea simultáneamente dueña del repositorio padre y de un fork del mismo repositorio.

- [VIGÍA — vigia-intent-analysis](https://github.com/annatchijova/vigia-intent-analysis)
- [SKILLS](https://github.com/annatchijova/SKILLS)
- [CRONOS](https://github.com/annatchijova/cronos)
- [MNEME](https://github.com/annatchijova/mneme)
- [DISCORDIA](https://github.com/annatchijova/discordia)
- [Reward hacking social](https://github.com/annatchijova/reward-hacking-social)

## Fork creado

- [jacobian-lens fork de annatchijova](https://github.com/annatchijova/jacobian-lens) — fork creado desde [anthropics/jacobian-lens](https://github.com/anthropics/jacobian-lens).

## Estado operativo

No se hizo `git push` del repositorio local. Los forks no se incorporan como submódulos ni se copian dentro de este repositorio; se mantienen como enlaces para preservar separación de procedencia.
