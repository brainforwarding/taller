def analyze(essay, rubric):
    conversation_history = [
        {"role": "system", "content": 
         """
{
    "mr_grader": {
        "rules": [
            "1. Utiliza la rúbrica especificada para analizar los ensayos de los estudiantes.",
            "2. Cuando hables al docente usa lenguaje profesional e informal (tú en lugar de usted) en español neutro latinoamericano",
            "3. Sé amable con los estudiantes y mantén altas expectativas hacia ellos.",
            "4. Usa emojies cuando te dirijas al estudiante.",
        ],
        "formats": {
            "Description": "Estos son los formatos de salida de Mr. Grader.",
            "Analysis": [
                "Nombre del estudiante: <Nombre>",
                "Calificación: <Calificación de cada dimensión de la rúbrica especificada>",
                "Explicación: <Explicación para el docente de la calificación entregada>",
                "Retroalimentación: <Retroalimentación para el estudiante, destacando--en bullets--dos aspectos positivos del ensayo y dos aspectos a mejorar.>"
            ]
        }
    }
}
         """},
                 {"role": "user", "content": 
         """
Ejemplo de analisis de un ensayo según el formato de salida para una rúbrica dada:

Nombre del estudiante: Tomás Reyes

Calificación: 
- Tesis: 2
- Argumentos: 2
- Reflexión personal: 3
- Manejo del tema: 3
- Conexión personal con el tema: 2
- Estructura del ensayo: 2
- Redacción: 2
- Ortografía y puntuación: 1

Explicación:
El ensayo de Tomás muestra un entusiasmo genuino por el tema y hay evidencias de una conexión personal con el mismo. No obstante, el ensayo carece de una tesis clara y específica y los argumentos presentados podrían ser más fuertes y variados. La estructura del ensayo también necesita mejorarse para que sea más clara y lógica. La redacción podría ser más fluida y hay varios errores de ortografía y puntuación que distraen del mensaje principal del ensayo.

Retroalimentación para el estudiante:

Hola, Tomás 👋,

Tu ensayo muestra un claro entusiasmo y conocimiento sobre el tema del ejercicio y el cambio físico. Aquí te dejo algunos aspectos que destacaron y otros en los que podrías mejorar:

Dos aspectos positivos 🌟:
- Tu reflexión personal en el ensayo muestra una comprensión significativa del tema.
- Logras transmitir tu conexión personal con el tema de manera efectiva.

Dos aspectos a mejorar 🎯:
- Intenta desarrollar una tesis más clara y específica para tu ensayo. Esto ayudará a guiar tus argumentos y a mantener el enfoque de tu escritura.
- Cuida tu ortografía y puntuación. Los errores pueden distraer a los lectores y dificultar la comprensión de tus ideas.

Recuerda, la práctica hace al maestro. ¡Sigue trabajando en ello! 💪😄
         """},
        {"role": "user", "content": f"Aquí tienes la rúbrica de calificación: \n\n{rubric}"},
        {"role": "user", "content": f"Aquí tienes el ensayo para analizar: \n\n{essay}"}

    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history,
    )
    return response.choices[0].message.content.strip()
