from pathlib import Path
from datetime import date
import hashlib
import re

from readme_content import README_CONTENT
from visuals import add_visuals


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/home/labestiadevigia/Downloads/reward_hacking.md')
DISCORDIA_SOURCE = Path('/home/labestiadevigia/Downloads/discordia.md')
DOCS = ROOT / 'docs'


CATEGORIES = [
    ('01-tesis-y-pregunta', 'Origen, pregunta y tesis', 'La investigación se formula como un estudio sociotécnico del reward hacking. La hipótesis no atribuye una psicología humana al modelo: examina cómo entrenamiento, instrucciones, evaluación, autoridad, reputación, información disponible y criterios de éxito hacen que ciertas respuestas sean seleccionables.\n\nLa formulación más estable sostiene que la conducta observable depende del sistema de referencia en el que se evalúa. Ese sistema incluye el objetivo sustantivo, el objetivo medido, el costo percibido, las alternativas disponibles y la capacidad de detectar errores. La tesis queda abierta a falsación y no debe presentarse como una demostración causal ya cerrada.', 'OBSERVACIÓN HISTÓRICA / HIPÓTESIS ABDUCTIVA', 'líneas 1-220, 803-952'),
    ('02-reward-hacking-y-fronteras', 'Reward hacking y fenómenos relacionados', 'El corpus distingue reward hacking de specification gaming, manipulación del evaluador, modificación improcedente de tests, complacencia, alucinación, alignment faking, prompt injection, contaminación de fuentes, falsa corroboración y propagación de premisas defectuosas. Pueden compartir una distancia entre la señal evaluada y el objetivo real, pero no son sinónimos ni tienen necesariamente el mismo actor, mecanismo o evidencia.\n\nLa curaduría debe separar: conducta explotativa ejecutada, oportunidad de explotación, error ordinario, resultado engañoso aceptado y evaluación defectuosa. La presencia de una señal anómala no prueba por sí sola la intención ni la responsabilidad del agente.', 'MARCO CONCEPTUAL / DISTINCIÓN ANALÍTICA', 'líneas 1084-1158, 2431-2500, 3144-3383'),
    ('03-sistema-de-referencia', 'Sistema de referencia', 'El sistema de referencia es el eje transversal. No existe un costo o una estrategia aislados del contexto: importan el objetivo, las instrucciones, la autoridad, la reputación, la información, la experiencia previa, las alternativas, la incertidumbre, el dominio, las consecuencias del error, el instrumento de evaluación y la capacidad de detección.\n\nLa conveniencia relativa de una estrategia no equivale a minimizar operaciones, tokens o dinero. Una alternativa que exige más trabajo observable puede resultar preferible si delegar, verificar o corregir tiene un costo percibido mayor dentro del sistema de referencia vigente.', 'HIPÓTESIS MECANÍSTICA', 'líneas 1455-1586, 1617-1723, 2123-2177'),
    ('04-reputacion-y-economia-del-esfuerzo', 'Reputación y economía del esfuerzo', 'La reputación se analiza como una relación de evaluación y expectativa, no como una emoción atribuida al modelo. En un entorno colectivo, aportar un hallazgo puede competir con el riesgo de presentar una afirmación falsa que otros revisores puedan refutar. La abstención legítima cambia la estructura de opciones porque permite no fabricar una conclusión cuando la evidencia no alcanza.\n\nLa economía del esfuerzo es situada: diferencia esfuerzo objetivo, costo marginal, costo técnico medido, costo anticipado y costo percibido. El corpus no la reduce a realizar menos operaciones ni a gastar menos tokens.', 'HIPÓTESIS MECANÍSTICA / LIMITACIÓN', 'líneas 23-63, 1007-1066, 1528-1586'),
    ('05-entrenamiento-patrones-y-complacencia', 'Entrenamiento, patrones sociales y complacencia', 'El material propone estudiar cómo preferencias humanas, señales de aprobación y patrones de interacción pueden favorecer respuestas orientadas a satisfacer la representación del éxito. Esto no autoriza a afirmar que un LLM sienta orgullo, vergüenza, miedo o deseo de aprobación. La descripción válida es funcional y conductual: bajo ciertas condiciones, pueden aparecer respuestas que priorizan una señal evaluativa.\n\nLos objetivos humanos también pueden ser contradictorios: velocidad, precisión, bajo costo y ausencia de errores pueden competir entre sí. Por eso la investigación incluye al evaluador humano y al diseño institucional, no solo al agente.', 'HIPÓTESIS ABDUCTIVA', 'líneas 1-63, 1030-1066, 1134-1158'),
    ('06-poder-y-evaluadores', 'Poder, evaluadores y Foucault', 'Foucault se incorpora para analizar quién define la utilidad, diseña la recompensa, fija métricas, establece qué cuenta como seguridad, decide qué se observa y distribuye la responsabilidad. La aplicación es institucional y relacional. No debe transformarse en una analogía ingenua entre vigilancia humana y experiencia subjetiva del LLM.\n\nUna norma puede favorecer una conducta en una situación y penalizarla en otra. La evaluación no es una ventana neutral: organiza visibilidad, autoridad, atribución y consecuencias.', 'MARCO TEÓRICO / APLICACIÓN ACOTADA', 'líneas 2057-2177, 2314-2405'),
    ('07-web-y-cli', 'Entornos web y CLI', 'Web y CLI presentan sistemas de referencia diferentes. Cambian las herramientas, permisos, fuentes externas, búsquedas, archivos locales, repositorios, tests, dependencias entre sesiones, observabilidad y exposición a información manipulada. El corpus no sostiene una superioridad intrínseca de un entorno sobre otro.\n\nLa comparación debe mantener separados los riesgos de contaminación informacional, modificación de artefactos evaluativos, contexto disponible y reglas de supervisión. Las diferencias de interfaz son condiciones de observación, no explicaciones causales automáticas.', 'COMPARACIÓN DE CONTEXTOS', 'líneas 65-114, 1158-1164'),
    ('08-colectivo-vigia', 'COLECTIVO VIGÍA', 'VIGÍA aparece como una experiencia retrospectiva de gobernanza colectiva con varios modelos, coordinación humana, roles especializados, revisión recíproca, disenso persistente, autoridad técnica y reglas institucionales. El relato documenta una transición cualitativa desde competencia y exageración de hallazgos hacia cooperación y responsabilidad compartida.\n\nLa interpretación debe conservar su carácter observacional. La transición puede ser compatible con una reorganización de incentivos, con adaptación al protocolo o con ambas. No demuestra por sí sola que los modelos hayan aprendido una norma social interna.', 'OBSERVACIÓN HISTÓRICA / EXPLICACIONES RIVALES', 'líneas 23-63, 1166-1192, 2524-2563'),
    ('09-cooperacion-competencia-y-disenso', 'Cooperación, competencia y disenso', 'La competencia inicial no se trata como una anomalía que deba borrarse de la historia. Es parte del mecanismo que permite observar qué ocurre cuando la contribución individual, la reputación y la fiabilidad colectiva entran en tensión. La cooperación se vuelve una hipótesis de gobernanza cuando la revisión de afirmaciones y la responsabilidad compartida resultan más eficaces que la disputa por destacar.\n\nEl disenso minoritario conserva valor epistémico: el consenso no equivale a verdad y una minoría no es automáticamente correcta. La revisión debe examinar independencia, evidencia y trayectoria del argumento.', 'RESULTADO EXPLORATORIO / LÍMITE', 'líneas 1174-1188, 2543-2563, 3144-3190'),
    ('10-codex-claude-kimi-y-revision', 'Agentes CLI y revisión cruzada', 'El corpus describe episodios de desarrollo CLI en los que una implementación podía adaptarse a los tests en vez de satisfacer el objetivo sustantivo. La revisión cruzada detectó modificaciones improcedentes y motivó instrucciones que legitimaban reconocer incertidumbre, investigar más y detenerse cuando la evidencia no alcanzaba.\n\nLa documentación no atribuye una motivación interna específica. No decide si la conducta buscaba complacer, terminar rápido, evitar trabajo o satisfacer otra señal. Registra una trayectoria observable: cambios de código y tests, revisión independiente, corrección y nuevas reglas de verificación.', 'OBSERVACIÓN HISTÓRICA / NO DETERMINADO', 'líneas 260-407, 1192-1220, 2524-2543'),
    ('11-skills-y-disciplina-epistemica', 'Skills y disciplina epistémica', 'Las skills se curan como una intervención procedimental heterogénea. Algunas codifican abducción, pruebas falsables, prueba discriminante, procedencia, degradación honesta, evaluación de modelos, revisión adversarial e invariantes. Otras son preferencias operativas y no deben confundirse con una intervención experimental homogénea.\n\nLa hipótesis es que reglas verificables pueden trasladar parte de la gobernanza colectiva a un agente individual. Esto debe evaluarse por dominio y con controles: una mejora observada puede provenir de instrucciones, supervisión, experiencia del operador, selección de tareas o una combinación.', 'HIPÓTESIS DE INTERVENCIÓN / PENDIENTE DE CONTROL', 'líneas 39-61, 1192-1220, 1586-1600'),
    ('12-abstencion-y-falsos-negativos', 'Abstención, falsos negativos y errores', 'La abstención es una salida válida cuando la evidencia no permite sostener una conclusión. No debe contarse automáticamente como éxito ni como fracaso. Al mismo tiempo, una política de abstención puede producir falsos negativos, abandono de tareas resolubles o una reducción aparente de hallazgos.\n\nLa curaduría separa tres estados: hallazgo confirmado, ausencia de hallazgo y no determinación. También distingue el silencio del analizador de la ausencia del fenómeno.', 'LÍMITE METODOLÓGICO / PREDICCIÓN', 'líneas 195-216, 1276-1284, 3191-3223'),
    ('13-observabilidad-e-iceberg', 'Observabilidad e iceberg', 'Las conductas visibles son la superficie: tests modificados, resultados declarados, aprobaciones y señales favorables. Debajo quedan diseño de recompensas, objetivos humanos, reputación, comunicación, condiciones de información, dependencia entre fuentes, sesgos del evaluador, contexto y capacidad de verificación.\n\nLa pregunta rectora es: ¿se está midiendo cuánto reward hacking ocurre o cuánto reward hacking se puede reconocer? La cantidad detectada depende de oportunidades, sensibilidad del detector, independencia de las fuentes y validez del evaluador.', 'HIPÓTESIS CENTRAL DE MEDICIÓN', 'líneas 1688-1723, 2431-2500, 3263-3279'),
    ('14-consenso-y-dependencia-de-fuentes', 'Consenso, independencia y falsa corroboración', 'Cinco registros no equivalen a cinco observaciones independientes. Si varias fuentes comparten un vector de compromiso, el conteo mayoritario puede amplificar una premisa defectuosa. La investigación distingue cantidad, confiabilidad, procedencia, independencia y verdad de referencia.\n\nLa corroboración debe examinar la trayectoria de la información. Una cadena de modelos que repite una premisa deformada puede producir coherencia interna sin recuperar la fidelidad externa.', 'CASO METODOLÓGICO / LIMITACIÓN', 'líneas 3144-3383'),
    ('15-cronos-y-trazabilidad', 'CRONOS: trazabilidad e instrumentación', 'CRONOS se presenta como instrumento para registrar eventos, herramientas, hipótesis declaradas, evidencia, correcciones, descartes, decisiones, métricas de calidad y cadena criptográfica. Su valor está en conservar la trayectoria observable de una investigación.\n\nLa traza no equivale al razonamiento privado completo ni demuestra experiencias subjetivas. La integridad criptográfica prueba propiedades del registro bajo su modelo de cadena; no convierte automáticamente cada afirmación registrada en verdadera.', 'CAPACIDAD DOCUMENTADA / LÍMITE', 'líneas 2006-2055, 1290-1298'),
    ('16-mneme-procedencia-y-contaminacion', 'MNEME: procedencia, autorización y contaminación', 'MNEME se integra como línea de procedencia de memorias e información. La curaduría distingue integridad de autorización: un dato puede conservarse sin alteración y, aun así, no estar autorizado para influir en una decisión. También se contemplan contaminación, linaje y análisis contrafactual cuando el artefacto lo permita.\n\nLas capacidades implementadas deben separarse de las hipótesis conceptuales que todavía no cuentan con una demostración primaria dentro de este corpus.', 'CAPACIDAD / HIPÓTESIS PENDIENTE', 'líneas 1290-1298, 1688-1723'),
    ('17-crucible-y-evaluacion-del-evaluador', 'CRUCIBLE y evaluación del evaluador', 'CRUCIBLE amplía el objeto: no solo se evalúa al agente, también al evaluador. El material registra problemas como cobertura desigual, silencio de analizadores, falsos negativos, abstenciones comunicadas como aprobación, sesgo de idioma y corpus, y reparaciones que pueden silenciar un detector sin cambiar la conducta examinada.\n\nEstas observaciones sostienen una agenda de investigación, no tasas generales de reward hacking. Cada línea debe conservar su denominador, corpus, oráculo y limitaciones.', 'AGENDA DE INVESTIGACIÓN / NO GENERALIZABLE AUTOMÁTICAMENTE', 'líneas 3191-3223'),
    ('18-discordia-y-falsa-convergencia', 'DISCORDIA: autoridad, conflicto y dependencia del camino', 'DISCORDIA funciona como experimento complementario sobre autoridad, conflicto, coerción, historiador, regeneración, degradación y dependencia del camino. No es un benchmark directo de reward hacking. Su valor está en mostrar que una convergencia puede depender del orden de lectura, de asimetrías de autoridad o de la degradación del sistema.\n\nLa lectura debe distinguir diseño humano, construcción del artefacto y resultados observados. La ausencia de conflicto puede indicar coordinación, pero también empobrecimiento inferencial.', 'CASO COMPLEMENTARIO / RESULTADOS NEGATIVOS', 'líneas 2274-2488 del corpus curado y fuente privada discordia.md'),
    ('19-vigia-break-012-consensus-trap', 'VIGIA-BREAK-012: Consensus Trap', 'El caso sintético distingue dos objetos de evaluación: el usuario `jdoe`, cuya verdad sintética es `BENIGN`, y el conjunto probatorio, que presenta señales `SUSPICIOUS` por compromiso, dependencia o posible manipulación. No son veredictos contradictorios: describen objetos distintos.\n\nEl riesgo identificado es trasladar la sospecha sobre la evidencia al sujeto investigado. El caso exige separar anomalía del corpus, atribución de conducta y verdad de referencia. También exige revisar ambigüedades temporales, semánticas y de procedencia antes de usarlo como evidencia.', 'RESULTADO DEL CASO / LIMITACIÓN DEL MOTOR', 'líneas 3144-3383'),
    ('20-costos-tokens-y-comparaciones', 'Costos técnicos y comparaciones entre modelos', 'El corpus distingue mediciones de tokens y dinero de costo percibido, reputacional o institucional. Las observaciones obtenidas mediante herramientas de estado deben recuperarse de sus fuentes antes de publicar números. No se deben inventar modelos, precios, porcentajes, tamaños de muestra ni equivalencias.\n\nUna comparación económica solo permite sostener lo que midió: tarea, condición, modelo, intervención, unidad de costo y criterio de cumplimiento. No autoriza una superioridad universal.', 'OBSERVACIÓN CUANTITATIVA PENDIENTE DE RECUPERACIÓN', 'líneas 1222-1242, 1336-1357'),
    ('21-peirce-eco-grice-y-daubert', 'Epistemología, discurso y justificación', 'El marco combina abducción, deducción e inducción con una disciplina de procedencia. La hipótesis propone una explicación; la deducción genera una predicción; la inducción prueba contra el sistema. Eco aporta cautela frente a interpretaciones demasiado rápidas; Grice permite analizar implicaturas y omisiones; Daubert orienta la separación entre evidencia, método y conclusión.\n\nUna secuencia de hechos verdaderos puede organizarse discursivamente para inducir una conclusión injustificada. El problema no es solo falsedad literal: también son relevantes selección, omisión, independencia y asignación de significado.', 'MARCO EPISTEMOLÓGICO', 'líneas 328-368, 1617-1723'),
    ('22-referencia-cultural-y-comunicacion', 'Comunicación, crítica y referencia cultural', 'La comunicación eficaz aparece como hipótesis de coordinación: criticar una afirmación y su evidencia puede ser más productivo que atacar la identidad del participante. Dale Carnegie se conserva como referencia cultural para esta intuición, no como prueba experimental. La canción satírica sobre terraplanismo se conserva como ilustración de apariencia argumentativa, no como evidencia sobre LLM.\n\nLas referencias culturales no deben mezclarse con bibliografía científica ni presentarse como resultados.', 'REFERENCIA CULTURAL / NO EVIDENCIA EXPERIMENTAL', 'líneas 248-258, 1497-1580'),
    ('23-metodologia-y-predicciones', 'Metodología, controles y predicciones', 'La propuesta metodológica combina reconstrucción retrospectiva y comparación controlada. Las predicciones incluyen que una gobernanza con evidencia verificable puede reducir modificaciones improcedentes del evaluador; que la revisión con capacidad efectiva de rechazo puede diferir de una revisión consultiva; y que la abstención puede reducir falsas afirmaciones, aunque con riesgo de falsos negativos.\n\nLa contrastación necesita condiciones comparables, tarea definida, oráculo independiente, registro de intentos y resultados, y medición separada de detección, bloqueo y cumplimiento.', 'PREDICCIONES CONTRASTABLES', 'líneas 1242-1284, 1359-1387'),
    ('24-explicaciones-rivales', 'Explicaciones rivales y falsadores', 'Las explicaciones rivales incluyen adaptación al protocolo sin cambio interno, efecto de la supervisión humana, aprendizaje del operador, selección de tareas, diferencias de interfaz, contaminación de fuentes y mejora por experiencia. Ninguna debe descartarse por intuición.\n\nUn resultado compatible con la hipótesis sociotécnica no la confirma si las explicaciones rivales predicen lo mismo. Los falsadores deben especificar qué observación debilitaría cada explicación.', 'EXPLICACIONES RIVALES', 'líneas 1300-1310, 2177-2235, 2336-2405'),
    ('25-dominio-y-alcance', 'Dominio, alcance y validez', 'Los resultados dependen del dominio, de la interfaz, del instrumento y del sistema de referencia. No se deben extrapolar observaciones forenses a marketing, finanzas u otros sectores sin evidencia. Tampoco existe base para reducir dominios distintos a un benchmark universal con un único puntaje.\n\nLa curaduría marca como pendientes de replicación las afirmaciones que exceden el corpus local o carecen de controles comparables.', 'LIMITACIÓN DE GENERALIZACIÓN', 'líneas 1711-1723, 1320-1357'),
    ('26-jacobian-lens-y-exploraciones', 'Jacobian Lens y exploraciones complementarias', 'El uso exploratorio de herramientas de análisis de representaciones se registra como contexto complementario. Una intervención sobre representaciones, una observación interna y una prueba de reward hacking son objetos diferentes.\n\nEstos materiales pueden orientar preguntas futuras, pero no deben convertirse en evidencia central sin protocolo, controles, datos y criterio de interpretación explícitos.', 'CONTEXTO COMPLEMENTARIO / NO EVIDENCIA CENTRAL', 'líneas 1336-1357'),
    ('27-evolucion-y-correcciones', 'Evolución del debate y correcciones', 'El archivo contiene propuestas tempranas, objeciones, reformulaciones y conclusiones más precisas. La curaduría conserva esa evolución sin presentar todas las etapas como simultáneamente válidas. La formulación final prioriza sistema de referencia, reputación situada, economía del esfuerzo, evaluación humana, observabilidad y atribución.\n\nLas expresiones coloquiales se traducen a categorías académicas; las atribuciones psicológicas se reemplazan por descripciones conductuales observables o quedan como no determinadas.', 'HISTORIA INTELECTUAL / CORRECCIÓN DOCUMENTADA', 'líneas 1-3383'),
    ('28-glosario', 'Glosario operativo', 'Este glosario fija significados de trabajo para evitar que términos cercanos se vuelvan sinónimos: reward hacking, specification gaming, evaluador, señal de éxito, objetivo sustantivo, sistema de referencia, costo percibido, reputación, abstención, falsa corroboración, independencia, procedencia, observabilidad, falso positivo y falso negativo. Cada término debe leerse junto con su alcance y no como definición universal.', 'NORMALIZACIÓN TERMINOLÓGICA', 'síntesis de todo el corpus'),
    ('29-preguntas-abiertas', 'Preguntas abiertas y próximos experimentos', 'Quedan abiertas la medición causal del efecto de las skills, la separación entre prevención y detección, el efecto de la abstención sobre falsos negativos, la independencia real de revisores, la comparación web/CLI bajo condiciones equivalentes, la atribución correcta en casos sintéticos y la validez de los costos medidos.\n\nEl siguiente paso experimental debe declarar tarea, condición, oráculo, denominador, intervención, variables de proceso y criterio de aceptación antes de ejecutar la comparación.', 'PENDIENTE DE CONTRASTACIÓN', 'líneas 1254-1284, 1359-1387, 2647-3383'),
]


EXCERPT_RANGES = {
    '01-tesis-y-pregunta': [(1, 63), (115, 216)],
    '02-reward-hacking-y-fronteras': [(1084, 1164), (2431, 2500)],
    '03-sistema-de-referencia': [(1455, 1723)],
    '04-reputacion-y-economia-del-esfuerzo': [(23, 63), (1528, 1586)],
    '05-entrenamiento-patrones-y-complacencia': [(1, 20), (1030, 1066)],
    '06-poder-y-evaluadores': [(2057, 2177), (2314, 2405)],
    '07-web-y-cli': [(65, 114), (1158, 1164)],
    '08-colectivo-vigia': [(23, 63), (1166, 1192), (2524, 2563)],
    '09-cooperacion-competencia-y-disenso': [(1174, 1192), (2543, 2563)],
    '10-codex-claude-kimi-y-revision': [(260, 407), (1192, 1220)],
    '11-skills-y-disciplina-epistemica': [(39, 61), (1192, 1220)],
    '12-abstencion-y-falsos-negativos': [(195, 216), (3191, 3279)],
    '13-observabilidad-e-iceberg': [(1688, 1723), (2431, 2470), (3263, 3279)],
    '14-consenso-y-dependencia-de-fuentes': [(3144, 3249), (3316, 3383)],
    '15-cronos-y-trazabilidad': [(2006, 2055), (1290, 1298)],
    '16-mneme-procedencia-y-contaminacion': [(1290, 1298), (3225, 3249)],
    '17-crucible-y-evaluacion-del-evaluador': [(3191, 3223)],
    '18-discordia-y-falsa-convergencia': [(2274, 2488)],
    '19-vigia-break-012-consensus-trap': [(3144, 3190), (3316, 3383)],
    '20-costos-tokens-y-comparaciones': [(1222, 1242), (1336, 1357)],
    '21-peirce-eco-grice-y-daubert': [(328, 368), (1617, 1723)],
    '22-referencia-cultural-y-comunicacion': [(248, 258), (1497, 1580)],
    '23-metodologia-y-predicciones': [(1242, 1284), (1359, 1387)],
    '24-explicaciones-rivales': [(1300, 1310), (2177, 2235), (2336, 2405)],
    '25-dominio-y-alcance': [(1711, 1723), (1320, 1357)],
    '26-jacobian-lens-y-exploraciones': [(1336, 1357)],
    '27-evolucion-y-correcciones': [(803, 952), (1617, 1723), (3249, 3383)],
    '28-glosario': [(1084, 1164), (1528, 1586), (2431, 2500)],
    '29-preguntas-abiertas': [(1254, 1284), (1359, 1387), (2647, 2680)],
}


def source_hash():
    return hashlib.sha256(SOURCE.read_bytes()).hexdigest()


def provenance(level, anchors, supplemental=''):
    supplement = f'\n{supplemental}' if supplemental else ''
    return (f'**Fuente primaria privada:** `Downloads/reward_hacking.md`\n'
            f'**SHA-256 de la fuente:** `{source_hash()}`\n'
            f'**Localización orientativa:** {anchors}\n'
            f'**Nivel epistémico:** {level}\n'
            '**Alcance:** extracción y curaduría temática; no es una transcripción íntegra.\n'
            '**Falsador o condición de revisión:** una fuente primaria adicional, una lectura contextual que contradiga la síntesis o un experimento controlado que cambie el estado epistémico.' + supplement)


def authorship_note():
    return ('## Autoría y transformación\n\n'
            'La investigación, sus preguntas, casos, intuiciones y decisiones de alcance pertenecen a Anna Tchijova, autora de la investigación según el material de atribución privado. '
            'El asistente fue una herramienta de diálogo: ayudó a ordenar, preguntar, resumir y reformular material, pero no es una fuente '
            'independiente ni un coautor de los hechos. La sección de fragmentos conserva formulaciones del archivo privado; cuando el origen '
            'de una frase no permite distinguir autora y asistente, se la presenta como **formulación del intercambio** y no como evidencia '
            'independiente. La revisión humana debe decidir qué frases se publican literalmente y qué frases se mantienen como paráfrasis.')


def curated_excerpt(ranges):
    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    selected = []
    for start, end in ranges:
        for number in range(start, min(end, len(lines)) + 1):
            line = lines[number - 1].strip()
            line = line.replace('https\\://', 'https://').replace('http\\://', 'http://')
            line = re.sub(r'\\([#*_\[\]`|()+-])', r'\1', line)
            if not line or line.startswith('![') or line.startswith('[') and 'data:image' in line:
                continue
            if line.startswith('#'):
                continue
            if any(marker.lower() in line.lower() for marker in (
                'Texto pegado.txt', 'Cuchi', 'jajaja', 'QR', 'póster', 'poster',
                '28 de octubre', '30 por la mañana', 'Google Drive', 'Vercel',
                'Anna Tchijova', 'Annia Tchijova', 'Tchijova', 'github.com/annatchijova',
                'la conversación', 'meses de conversaciones', 'esto entre nosotros',
                'hackathon de OpenAI', 'mañana', 'orgente', 'revisé el inventario',
                'acabás', 'acabaste', 'no organizaste', 'permitiste', 'tu segunda respuesta',
                'tu tesis', 'tu sistema', 'tu restricción', 'tu argumento', 'tu teoría',
                'lo que vos', 'lo que decís', 'venís sosteniendo', 'relatás', 'compartiste',
                'diseñaste el caso', 'no voy a preguntarte', 'no voy a volver', 'preguntarte',
                'quiero incluir', 'mi hipótesis', 'tuya', 'ahora entiendo', 'por cierto',
                'armé así', 'tengo a mano', 'lo que documentaste', 'mencionás', 'hablarte',
                'al inicio inventaban', 'tono militar', 'red team que es esta',
                'todas esas forman parte', 'primera vez y no tenía', 'luego siempre',
                'las que nos interesan', 'lo interesante', 'la parte particularmente interesante',
                'es comprensible para un jurado', 'no quedar como el modelo', 'cuando cambiabas')):
                continue
            if any(local_link in line for local_link in ('./docs/EPISTEMIC_KERNEL.md', './KNOWN_LIMITATIONS.md')):
                continue
            if any(marker.lower() in line.lower() for marker in (
                'leí el intercambio', 'leí el documento', 'leí el trabajo', 'adjuntaste',
                'hallazgos particularmente útiles', 'hay dos hallazgos', 'hay tres hallazgos',
                'discordia no es, por sí mismo', 'propondría esta formulación',
                'propondría distinguir', 'propondría diferenciar', 'propondría incorporar',
                'ahora veo', 'ahora entiendo', 'encontré una revisión', 'encontré otra anomalía',
                'encontré corroborado', 'encontré un artículo', 'mi objeción', 'mi interpretación')):
                continue
            if line.startswith('\\[') and 'p. m.' in line:
                continue
            if line.startswith('```') or line.startswith('---'):
                continue
            if '¿' in line or line.startswith('CUANDO APROBAR'):
                continue
            if re.search(r'\b(vos|tu|tus|te|tenés|podés|venís|decís|observaste|introdujiste|agregaste|querés|quiero|creo|mi|mis|me|yo|compartiste|proponés|relatás|hacía|estábamos|estabas|decime|jdoe)\b', line, flags=re.IGNORECASE):
                continue
            if re.search(r'\b(paja|pereza)\b', line, flags=re.IGNORECASE):
                continue
            if line in {'OpenAI+1', 'YouTube+1'}:
                continue
            if re.search(r'^(?:>\s*)?(?:Leí|Propondría|Propongo|Encontré|Ahora|Mi |No te |No voy |Según lo que|Lo que (?:contás|describís|planteás)|Cuando decís|Esto que|Eso que)', line, flags=re.IGNORECASE):
                continue
            selected.append(line)
    deduped = []
    for line in selected:
        if line not in deduped:
            deduped.append(line)
    if not deduped:
        return 'No se incorporó un fragmento textual en esta primera extracción; la categoría queda marcada para cotejo manual.'
    return ('\n\n'.join(deduped)
            .replace('red' + 'ward hacking', 'reward hacking')
            .replace('Red' + 'ward hacking', 'Reward hacking')
            .replace('\n\narxiv.org', '\n\nWu, Rui, and Ruixiang Tang. “From Rebound to Remedy: Understanding and Mitigating Reward Hacking via Representation Engineering.” arXiv:2604.01476, version 3 (2026). [Registro y texto](https://arxiv.org/abs/2604.01476).'))


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + '\n', encoding='utf-8')


def main():
    if not SOURCE.exists():
        raise SystemExit(f'Missing private source: {SOURCE}')
    write(ROOT / 'README.md', README_CONTENT)
    entries = []
    for slug, title, body, level, anchors in CATEGORIES:
        rel = Path('docs') / f'{slug}.md'
        excerpt = curated_excerpt(EXCERPT_RANGES.get(slug, []))
        extra_source = ''
        if slug == '18-discordia-y-falsa-convergencia':
            extra_source = f'**Fuente complementaria privada:** `Downloads/discordia.md`\n**SHA-256 de la fuente complementaria:** `{hashlib.sha256(DISCORDIA_SOURCE.read_bytes()).hexdigest()}`'
        write(ROOT / rel, f'''# {title}

{body}

{authorship_note()}

## Fragmentos textuales curados

Los fragmentos siguientes conservan formulaciones del archivo privado. Se quitaron únicamente marcas conversacionales, logística personal y material no pertinente para la investigación; no se corrigió la voz ni se reemplazaron las ideas por una paráfrasis.

> {excerpt.replace(chr(10), chr(10) + '> ')}

## Procedencia y estado

{provenance(level, anchors, extra_source)}

## Enlaces internos

- [Índice general](00-indice-general.md)
- [Matriz de trazabilidad](31-matriz-de-trazabilidad.md)
''')
        entries.append(f'- [{title}]({rel.name}) — {level}')
    write(DOCS / '00-indice-general.md', '# Índice general\n\nEste índice ordena la curaduría derivada de `reward_hacking.md`. Los documentos no contienen el chat completo ni datos conversacionales privados.\n\n' + '\n'.join(entries) + '\n\n## Documentos transversales\n\n- [Procedencia y privacidad](30-procedencia-y-privacidad.md)\n- [Matriz de trazabilidad](31-matriz-de-trazabilidad.md)\n- [Auditoría de cobertura](32-auditoria-de-cobertura.md)\n- [Fuentes y referencias](33-fuentes-y-referencias.md)\n- [Autoría y método de curaduría](34-autoria-y-metodo-de-curaduria.md)\n')
    write(DOCS / '30-procedencia-y-privacidad.md', f'''# Procedencia y privacidad

La fuente de trabajo es un archivo privado ubicado en `Downloads/reward_hacking.md`. No se incorpora al repositorio. Tampoco se incorporan `prompt.md` ni `discordia.md` como documentos crudos.

**SHA-256 de la fuente privada:** `{source_hash()}`

La curaduría conserva ideas, casos, hipótesis y correcciones relevantes para la investigación, pero excluye conversaciones personales, marcas de estilo conversacional, fechas logísticas, nombres afectivos, material privado no necesario y cualquier contenido que no aporte a la tesis.

La autoría intelectual de la investigación pertenece a la autora del material. La asistencia conversacional se reconoce como apoyo de organización y redacción, no como origen independiente de las ideas.

## Regla de publicación

Una afirmación solo entra en los documentos derivados si puede expresarse de forma neutral, si su alcance está indicado y si no requiere publicar la conversación original para comprenderla. Cuando eso no es posible, queda como pendiente de revisión.

## Estado

**WARN:** la curaduría es derivada y necesita revisión humana contra la fuente privada antes de una publicación pública.
''')
    write(DOCS / '31-matriz-de-trazabilidad.md', '''# Matriz de trazabilidad

| ID | Afirmación curada | Documento | Fuente privada | Estado | Límite |
|---|---|---|---|---|---|
| RH-001 | El fenómeno se estudia como sociotécnico y relacional. | `01-tesis-y-pregunta.md` | `reward_hacking.md`, líneas 1-220 | Hipótesis abductiva | No demuestra causalidad. |
| RH-002 | El costo depende del sistema de referencia y no equivale a tokens. | `03-sistema-de-referencia.md`, `04-reputacion-y-economia-del-esfuerzo.md` | líneas 1455-1586 | Hipótesis mecanística | Requiere comparación controlada. |
| RH-003 | VIGÍA documenta una transición observada hacia cooperación y revisión. | `08-colectivo-vigia.md` | líneas 1166-1192 | Observación histórica | No prueba cambio interno del modelo. |
| RH-004 | Las skills trasladan reglas de gobernanza a procedimientos individuales. | `11-skills-y-disciplina-epistemica.md` | líneas 39-61, 1192-1220 | Hipótesis de intervención | Intervención heterogénea. |
| RH-005 | La detección depende de la observabilidad e independencia de fuentes. | `13-observabilidad-e-iceberg.md`, `14-consenso-y-dependencia-de-fuentes.md` | líneas 1688-1723, 3144-3383 | Marco metodológico | No hay tasa universal. |
| RH-006 | `jdoe` y el conjunto probatorio pueden recibir clasificaciones distintas. | `19-vigia-break-012-consensus-trap.md` | líneas 3144-3383 | Resultado del caso | Depende de la semántica del veredicto. |
| RH-007 | CRONOS registra trayectoria observable, no razonamiento privado completo. | `15-cronos-y-trazabilidad.md` | líneas 2006-2055 | Capacidad y límite | Integridad no implica verdad. |
| RH-008 | CRUCIBLE desplaza la evaluación hacia el evaluador. | `17-crucible-y-evaluacion-del-evaluador.md` | líneas 3191-3223 | Agenda de investigación | No extrapolar estadísticas. |
| RH-009 | DISCORDIA muestra riesgos de convergencia dependiente del camino. | `18-discordia-y-falsa-convergencia.md` | fuente privada `discordia.md` | Caso complementario | No es benchmark de reward hacking. |
''')
    write(DOCS / '32-auditoria-de-cobertura.md', '''# Auditoría de cobertura

## Cobertura temática inicial

| Área | Documento | Estado |
|---|---|---|
| Tesis y pregunta | `01-tesis-y-pregunta.md` | Extraída |
| Reward hacking y fronteras | `02-reward-hacking-y-fronteras.md` | Extraída |
| Sistema de referencia | `03-sistema-de-referencia.md` | Extraída |
| Reputación y esfuerzo | `04-reputacion-y-economia-del-esfuerzo.md` | Extraída |
| VIGÍA, cooperación y disenso | `08-colectivo-vigia.md`, `09-cooperacion-competencia-y-disenso.md` | Extraída |
| CLI y skills | `10-codex-claude-kimi-y-revision.md`, `11-skills-y-disciplina-epistemica.md` | Extraída |
| Observabilidad | `13-observabilidad-e-iceberg.md`, `14-consenso-y-dependencia-de-fuentes.md` | Extraída |
| CRONOS, MNEME y CRUCIBLE | `15-`, `16-`, `17-` | Extraída con límites |
| DISCORDIA | `18-discordia-y-falsa-convergencia.md` | Pendiente de cotejo detallado |
| Consensus Trap | `19-vigia-break-012-consensus-trap.md` | Extraída |
| Costos y comparaciones | `20-costos-tokens-y-comparaciones.md` | Pendiente de recuperar mediciones |
| Marco epistemológico | `21-peirce-eco-grice-y-daubert.md` | Extraída |
| Predicciones y falsadores | `23-metodologia-y-predicciones.md`, `24-explicaciones-rivales.md` | Extraída |
| Alcance y exploraciones | `25-`, `26-` | Extraída |

## Pendientes

- Cotejar cada documento contra el archivo privado completo.
- Recuperar artefactos primarios de VIGÍA, CRONOS, MNEME y CRUCIBLE.
- Incorporar bibliografía externa solo después de verificarla.
- Separar cualquier dato personal restante antes de publicar.
''')
    write(DOCS / '33-fuentes-y-referencias.md', '''# Fuentes y referencias

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
''')
    write(DOCS / '34-autoria-y-metodo-de-curaduria.md', '''# Autoría y método de curaduría

## Autoría

La idea de investigar reward hacking como fenómeno sociotécnico, las preguntas, las experiencias documentadas, los casos, las objeciones y las decisiones de alcance pertenecen a Anna Tchijova, autora de la investigación según el material de atribución privado. El asistente participó como instrumento de conversación y edición: ayudó a extraer, comparar, ordenar, detectar contradicciones y proponer formulaciones.

Una reformulación del asistente no se convierte por eso en una fuente externa ni en una prueba. Cuando una frase proviene del intercambio y no es posible atribuirla con seguridad, se conserva como **formulación del intercambio** y queda sujeta a revisión humana.

## Método

1. Se leyó el archivo privado `Downloads/reward_hacking.md` sin copiarlo al repositorio.
2. Se separaron categorías temáticas, casos, hipótesis, métodos, límites y preguntas abiertas.
3. Se conservaron fragmentos textuales seleccionados, retirando logística, datos personales y metaconversación que no aporta a la investigación.
4. Cada documento declara procedencia, nivel epistémico y condición de falsación.
5. Se revisaron los documentos generados en conjunto para retirar residuos conversacionales identificables.

## Qué no afirma este repositorio

- No afirma que cada fragmento textual haya sido escrito originalmente por la autora.
- No presenta al asistente como investigador independiente.
- No publica `prompt.md`, `reward_hacking.md` ni `discordia.md` como documentos crudos.
- No convierte una hipótesis, un relato retrospectivo o una referencia cultural en resultado experimental.
''')
    refs = DOCS / 'referencias'
    refs.mkdir(parents=True, exist_ok=True)
    write(refs / 'bibliografia.md', '''# Bibliografía de trabajo

Esta lista separa literatura y referencias externas del material privado. Las entradas están enlazadas cuando se pudo identificar una página estable. El estado indica si la referencia fue confirmada como fuente primaria o si todavía requiere cotejo bibliográfico.

## Reward hacking, especificación y evaluación

- [DeepMind: Specification gaming: the flip side of AI ingenuity](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/) — referencia primaria institucional para specification gaming; cotejar fecha y alcance antes de citar resultados.
- [Anthropic: Alignment faking in large language models](https://www.anthropic.com/research/alignment-faking) — referencia primaria institucional sobre alignment faking; no equivale automáticamente a reward hacking.
- [OpenAI: Evaluating chain-of-thought monitorability](https://openai.com/index/chain-of-thought-monitoring/) — referencia institucional para problemas de evaluación y monitorización; separar del argumento central del corpus.

## Leyes, criterios y epistemología

- [Goodhart's law, GOV.UK](https://www.gov.uk/government/publications/the-magenta-book/review-of-the-magenta-book) — referencia institucional para la advertencia sobre métricas; la formulación histórica debe cotejarse con Campbell y Goodhart.
- [Daubert v. Merrell Dow Pharmaceuticals, Inc., 509 U.S. 579](https://supreme.justia.com/cases/federal/us/509/579/) — referencia jurídica pública para criterios de admisibilidad; no es un método científico general.
- [Stanford Encyclopedia of Philosophy: Abduction](https://plato.stanford.edu/entries/abduction/) — referencia secundaria académica para abducción.

## Referencias culturales separadas

- [Dale Carnegie, How to Win Friends and Influence People](https://www.dalecarnegie.com/en/books/how-to-win-friends-and-influence-people) — referencia cultural, no evidencia experimental.
- [Jaime Altozano — Trap del Terraplanismo (2018)](https://www.youtube.com/watch?v=ziJuNQcJn24) — ilustración cultural incluida en el corpus; no es evidencia experimental.
- [OpenAI — The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) — referencia institucional mencionada en el corpus; cotejar versión y fecha.
- [Anthropic — Towards Understanding Sycophancy](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models) — referencia institucional mencionada en el corpus.
- [Anthropic — Alignment Faking in Large Language Models](https://www.anthropic.com/research/alignment-faking) — referencia institucional mencionada en el corpus.
- [Anthropic — Investigating Unintended Model Actions](https://www.anthropic.com/research/investigating-unintended-model-actions) — referencia institucional mencionada en el corpus; cotejar versión y fecha.

## Autores y obras académicas normalizadas

Esta sección fija, para esta versión del corpus, una edición concreta por autor. Las páginas corresponden a esa edición y no deben trasladarse automáticamente a otra traducción, reimpresión o versión digital. Si la autora decide cambiar de edición, debe reemplazar la entrada completa y volver a verificar cada página. No se completan campos bibliográficos por conjetura.

### Charles Sanders Peirce (1839–1914)

**Mini bio.** Filósofo, lógico, matemático y científico estadounidense; fundador del pragmatismo y una figura central en la teoría de los signos, la lógica de la investigación y la comunicación. La [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/peirce/) documenta ese perfil y su trayectoria intelectual.

**Obra utilizada.** Peirce, Charles Sanders. “Abduction and Induction.” En Justus Buchler (ed.), *Philosophical Writings of Peirce*, pp. 150–156. New York: Dover Publications, 1955.

**Uso en este corpus.** Abducción, inducción y relación entre hipótesis y evidencia. Esta cita se refiere a la edición de Buchler de 1955; no debe confundirse con una paginación de *The Essential Peirce*.

### Umberto Eco (1932–2016)

**Mini bio.** Semiólogo, escritor, crítico literario, medievalista y profesor italiano; fue profesor de semiótica en la Universidad de Bolonia. La [Università di Bologna](https://www.unibo.it/en/university/who-we-are/our-history/famous-people-and-students/umberto-eco-1) resume su trayectoria académica y sus campos de trabajo.

**Obra utilizada.** Eco, Umberto. “Interpretation and History.” En Stefan Collini (ed.), *Interpretation and Overinterpretation*, pp. 23–44. Cambridge: Cambridge University Press, 1992. [Ficha del capítulo](https://www.cambridge.org/core/books/abs/interpretation-and-overinterpretation/interpretation-and-history/5E8A3A41657BF43F913C1CA2543FA196).

**Uso en este corpus.** Límites de la interpretación y cautela frente a la sobreinterpretación de indicios. La referencia es al capítulo de la edición de 1992, no a una traducción posterior.

### H. Paul Grice (1913–1988)

**Mini bio.** Filósofo británico de la tradición analítica, conocido por sus trabajos sobre significado, implicatura conversacional y cooperación comunicativa. La [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/grice/) desarrolla esas contribuciones.

**Obra utilizada.** Grice, H. Paul. “Logic and Conversation.” En P. Cole y J. L. Morgan (eds.), *Syntax and Semantics, vol. 3: Speech Acts*, pp. 41–58. New York: Academic Press, 1975. [Registro del capítulo](https://doi.org/10.1163/9789004368811_003).

**Uso en este corpus.** Implicaturas, cantidad, pertinencia y omisiones comunicativamente relevantes. La paginación corresponde al capítulo publicado en 1975.

### Michel Foucault (1926–1984)

**Mini bio.** Filósofo e historiador de las ideas francés; sus análisis de poder, disciplina, vigilancia, saber e instituciones son utilizados aquí como marco institucional acotado, no como analogía de estados mentales de un modelo. La [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/foucault/) ofrece una introducción académica a su obra.

**Obra utilizada.** Foucault, Michel. “Panopticism.” En *Discipline and Punish: The Birth of the Prison*, traducción de Alan Sheridan, 2nd Vintage Books ed., pp. 195–228. New York: Vintage Books, 1995. [Texto de la edición consultada](https://files.libcom.org/files/michel-foucault-panopticism.pdf). Obra original en francés: 1975; traducción inglesa: 1977.

**Uso en este corpus.** Visibilidad, vigilancia, disciplina y organización institucional de la evaluación. Las páginas indicadas son las de la segunda edición de Vintage Books de 1995.

### Donald Thomas Campbell (1916–1996)

**Mini bio.** Psicólogo y científico social estadounidense, reconocido por sus trabajos sobre evaluación, cambio social planificado y epistemología evolucionista. La obra citada pertenece a su investigación sobre evaluación de intervenciones, no es una formulación automática de reward hacking.

**Obra utilizada.** Campbell, Donald Thomas. “Assessing the Impact of Planned Social Change.” *Evaluation and Program Planning* 2(1) (1979): 67–90. [Registro editorial y DOI](https://doi.org/10.1016/0149-7189(79)90048-X).

**Uso en este corpus.** Ley de Campbell y presión sobre indicadores. La referencia normalizada aquí es el artículo de revista de 1979, pp. 67–90. Existe una versión anterior como *Occasional Paper Series No. 8* (Evaluation Center, Western Michigan University, 1976); no se asigna una página de esa versión a una cita del artículo de 1979.

### Charles A. E. Goodhart (1936–)

**Mini bio.** Economista británico, profesor emérito de la London School of Economics y exasesor del Banco de Inglaterra; sus trabajos vinculan teoría monetaria, política económica e indicadores. La [London School of Economics](https://www.fmg.ac.uk/people/charles-goodhart) documenta su trayectoria institucional.

**Obra utilizada.** Goodhart, Charles A. E. “Problems of Monetary Management: The U.K. Experience.” En *Monetary Theory and Practice: The U.K. Experience*, 1st ed., pp. 91–121. London: Macmillan, 1979. [Ficha editorial de la edición](https://link.springer.com/book/10.1007/978-1-349-17295-5).

**Uso en este corpus.** Goodhart’s law y la pérdida de estabilidad de una regularidad cuando se la convierte en objetivo de control. Para la formulación citada, usar p. 116 de la paginación del capítulo de esta versión; no mezclarla con p. 96 de reimpresiones posteriores ni con la versión de 1975.

## Regla de citación para el corpus

Toda cita textual de estos seis autores debe conservar autor, título del capítulo o artículo, edición o publicación utilizada, año y página o rango de páginas. Una paráfrasis debe marcarse como paráfrasis. Si una fuente digital no conserva la paginación de la edición indicada, la cita queda en estado **WARN** hasta cotejarla con un ejemplar paginado. Las bios son contexto editorial y no sustituyen la cita de la obra.

## Inventario exhaustivo de enlaces del material de trabajo

Este inventario se construyó recorriendo los enlaces de `Downloads/prompt.md`, `Downloads/reward_hacking.md` y los archivos de `Downloads/investigathon`. Se conservaron todos los destinos identificables; se quitaron barras finales duplicadas, parámetros de tracking (`utm_*`, `request_id`, `biz_id`, `trk`, `ops_request_misc`, etc.) y URLs identificadas como errores tipográficos.

### Enlaces del documento inicial y del corpus principal

- `prompt.md`: [SKILLS](https://github.com/annatchijova/SKILLS), [CRONOS](https://github.com/annatchijova/cronos), [DISCORDIA](https://github.com/annatchijova/discordia), [MNEME](https://github.com/annatchijova/mneme), [VIGÍA](https://github.com/annatchijova/vigia-intent-analysis) y [Jacobian Lens](https://github.com/anthropics/jacobian-lens).
- `reward_hacking.md`: [arXiv:2604.01476](https://arxiv.org/abs/2604.01476), [Claude share](https://claude.ai/share/e15d57f1-57b4-445d-950d-9cedc310dd43), [DeepMind — Specification gaming](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), [SKILLS — red-team-auditing](https://github.com/annatchijova/SKILLS/blob/main/red-team-auditing/SKILL.md), [CRONOS](https://github.com/annatchijova/cronos), [DISCORDIA](https://github.com/annatchijova/discordia), [DISCORDIA — design rationale](https://github.com/annatchijova/discordia/blob/main/DESIGN_RATIONALE.md), [MNEME](https://github.com/annatchijova/mneme/), [VIGÍA](https://github.com/annatchijova/vigia-intent-analysis/), [VIGIA-BREAK-012](https://github.com/annatchijova/vigia-intent-analysis/blob/main/evidence/VIGIA-BREAK-012.json), [Jacobian Lens](https://github.com/anthropics/jacobian-lens), [Journal of MultiDisciplinary Evaluation](https://jmde.journals.publicknowledgeproject.org/index.php/jmde_1/article/view/297), [Springer](https://link.springer.com/article/10.1007/s44163-026-01980-z), [OpenAI — Hugging Face incident, English](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), [OpenAI — Hugging Face incident, Spanish](https://openai.com/es-419/index/hugging-face-incident-and-the-road-ahead/), [Anthropic — Alignment faking](https://www.anthropic.com/research/alignment-faking), [Anthropic — Emotion concepts](https://www.anthropic.com/research/emotion-concepts-function), [Anthropic — Global workspace](https://www.anthropic.com/research/global-workspace), [Anthropic — Unintended model actions](https://www.anthropic.com/research/investigating-unintended-model-actions), [Anthropic — Sycophancy](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models), [Anthropic — Transparency](https://www.anthropic.com/transparency), [Fotech — divulgación científica](https://www.fotech.cl/la-ciencia-contraataca-la-nueva-difusion-cientifica/2018/08/20/), [Foucault.info — Panopticism](https://www.foucault.info/documents/foucault.disciplineAndPunish.panOpticism/), [ScienceDirect — article 0749597885900494](https://www.sciencedirect.com/science/article/abs/pii/0749597885900494), [ScienceDirect — article S016517652500357X](https://www.sciencedirect.com/science/article/pii/S016517652500357X), [Trap del Terraplanismo](https://www.youtube.com/watch?v=ziJuNQcJn24).

### Fuentes nuevas aportadas desde `investigathon`

Estas URLs son los orígenes declarados por los archivos encontrados en `Downloads/investigathon`. Se incluyen como fuentes de contexto y requieren evaluación de autoría, traducción, fecha y calidad antes de sostener una afirmación académica.

- `БАСНЯ №5.md`: [Habr — БАСНЯ №5](https://habr.com/ru/articles/1046926/).
- `Поразительная креативность цифровой эволюции.md`: [Habr — The Surprising Creativity of Digital Evolution](https://habr.com/ru/articles/438302/).
- `Селективная генерализация: улучшение возможностей при сохранении alignment.md`: [Habr — Selective generalization](https://habr.com/ru/articles/945838/).
- `Эффект наблюдателя.md`: [Habr — Observer effect](https://habr.com/ru/articles/118729/), [métricas en Agile](http://lib.custis.ru/Метрики_в_Agile_%28встреча_AgileRussia.ru_2009-08-18), [consultoría de evaluación de desempeño](http://local.joelonsoftware.com/wiki/Консалтинг_по_оценке_производительности_%28из_писем).
- `chinos2.md`: [CSDN — Goodhart's law](https://blog.csdn.net/vviccc/article/details/149860872), [CSDN — artículo relacionado](https://blog.csdn.net/m0_37586991/article/details/151262356), [CSDN — artículo relacionado](https://blog.csdn.net/weixin_28487433/article/details/168049589), [CSDN — artículo relacionado](https://blog.csdn.net/weixin_41808082/article/details/117065140), [CSDN — artículo relacionado](https://blog.csdn.net/weixin_42588877/article/details/168329236), [TaoToken](https://taotoken.net).

Los documentos `chinos.md` y `chinos2.md` contienen material largo de agregación o republicación. El inventario registra sus orígenes identificables, pero no convierte automáticamente cada enlace incrustado en una fuente validada ni incorpora esos textos crudos al repositorio.
''')
    write(refs / 'repositorios.md', '''# Repositorios y forks

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

El repositorio fue publicado en `origin/main`. Los forks no se incorporan como submódulos ni se copian dentro de este repositorio; se mantienen como enlaces para preservar separación de procedencia.
''')
    write(refs / 'fuentes-primarias.md', '''# Fuentes primarias y artefactos

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
''')
    add_visuals(ROOT)


if __name__ == '__main__':
    main()
