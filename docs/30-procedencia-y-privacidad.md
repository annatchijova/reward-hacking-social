# Procedencia y privacidad

La fuente de trabajo es un archivo privado ubicado en `Downloads/reward_hacking.md`. No se incorpora al repositorio. Tampoco se incorporan `prompt.md` ni `discordia.md` como documentos crudos.

**SHA-256 de la fuente privada:** `c39b1956fd080e7f64cf3927c2fb045d207c359d4b9f8207620160a3b9a10487`

La curaduría conserva ideas, casos, hipótesis y correcciones relevantes para la investigación, pero excluye conversaciones personales, marcas de estilo conversacional, fechas logísticas, nombres afectivos, material privado no necesario y cualquier contenido que no aporte a la tesis.

La autoría intelectual de la investigación pertenece a la autora del material. La asistencia conversacional se reconoce como apoyo de organización y redacción, no como origen independiente de las ideas.

## De la fuente privada al documento público

```mermaid
flowchart LR
    P["Fuentes privadas"] --> H["Hash y preservación"]
    H --> E["Extracción temática"]
    E --> C["Curaduría académica"]
    C --> R["Revisión de privacidad"]
    R --> D["Documentos derivados"]
    E --> X["Excluido: datos personales,<br/>logística y metaconversación"]
    class P,H context;
    class E,C,R concept;
    class D evidence;
    class X warning;

    classDef concept fill:#e8e4f7,stroke:#55428a,color:#2b2149;
    classDef context fill:#e1f2f7,stroke:#266b7a,color:#163b43;
    classDef evidence fill:#e4f5e9,stroke:#247a3d,color:#143d22;
    classDef warning fill:#ffe5e5,stroke:#a61b1b,color:#5b1111;
    classDef outcome fill:#f5ead7,stroke:#8b6325,color:#4d3714;
```

La fuente se preserva fuera del repositorio; solo se publican elaboraciones necesarias para comprender la investigación.

## Regla de publicación

Una afirmación solo entra en los documentos derivados si puede expresarse de forma neutral, si su alcance está indicado y si no requiere publicar la conversación original para comprenderla. Cuando eso no es posible, queda como pendiente de revisión.

## Estado

**WARN:** la curaduría es derivada y necesita revisión humana contra la fuente privada antes de una publicación pública.
