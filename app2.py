import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Autoescuela CHESTER - Test DGT", page_icon="🚗", layout="centered")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #f8fafc; }
    .stButton>button { width: 100%; background-color: #2563eb; color: white; border-radius: 8px; font-weight: bold; }
    .stButton>button:hover { background-color: #1d4ed8; }
    h1, h2, h3 { color: #38bdf8; text-align: center; }
    .card { background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 15px; }
    .etapa-header { background-color: #1e1b4b; padding: 10px; border-radius: 8px; text-align: center; border: 1px solid #4338ca; margin-bottom: 15px; }
    .apto { color: #4ade80; font-size: 24px; font-weight: bold; text-align: center; }
    .no-apto { color: #f87171; font-size: 24px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE PREGUNTAS (Localizadas con tus archivos de GitHub) ---
preguntas = [
    {
        "p": "1. ¿Es aconsejable conducir un turismo calzado con unas chanclas?",
        "ops": [
            "a) No, porque podrían caerse y dificultar el manejo de los pedales.",
            "b) Sí, porque al no sujetar el pie, es más fácil ejercer la presión correcta sobre los pedales.",
            "c) Sí, porque permiten un manejo más rápido y seguro de los pedales."
        ],
        "c": "a",
        "img": "1.png"
    },
    {
        "p": "2. ¿Puede realizar un cambio de sentido en un lugar donde esté prohibido adelantar?",
        "ops": [
            "a) Sí, excepto entre la puesta y la salida de sol, porque disminuye la visibilidad.",
            "b) No, salvo que el cambio de sentido esté expresamente autorizado.",
            "c) Sí, cuando la circulación en sentido contrario lo permita."
        ],
        "c": "b",
        "img": "2.png"
    },
    {
        "p": "3. En un vehículo de autoescuela realizando clases prácticas, ¿quién es considerado el conductor?",
        "ops": [
            "a) Tanto al alumno como al profesor.",
            "b) El alumno, ya que maneja el volante.",
            "c) El profesor, por ser responsable de los mandos adicionales."
        ],
        "c": "c",
        "img": "3.png"
    },
    {
        "p": "4. ¿Dónde está permitido que viaje un niño que no alcance los 135 centímetros de estatura?",
        "ops": [
            "a) En cualquiera de los asientos traseros utilizando el cinturón para adultos.",
            "b) En un asiento delantero o trasero, utilizando siempre el cinturón de seguridad para adultos.",
            "c) En el asiento trasero, utilizando siempre un dispositivo de retención homologado en función de su talla y peso."
        ],
        "c": "c",
        "img": "https://images.unsplash.com/photo-1510511233900-1982d92bd835?auto=format&fit=crop&q=80&w=600"
    },
    {
        "p": "5. Con esta señalización (S-7 Velocidad máxima aconsejada), ¿a qué velocidad debe circular?",
        "ops": [
            "a) Obligatoriamente a 30 km/h.",
            "b) Al menos a 30 km/h.",
            "c) A 30 km/h, como recomendación, durante el tramo que subsista el peligro."
        ],
        "c": "c",
        "img": "5.png"
    },
    {
        "p": "6. Una línea blanca continua sobre la calzada, sensiblemente más ancha que en el caso general...",
        "ops": [
            "a) indica la existencia de un carril especial.",
            "b) sirve para delimitar, únicamente, los carriles bus.",
            "c) indica el borde de la calzada."
        ],
        "c": "a",
        "img": "6.png"
    },
    {
        "p": "7. ¿Cuál es la sanción por no tener el seguro obligatorio del vehículo?",
        "ops": [
            "a) Una multa, pero sin inmovilización del vehículo.",
            "b) Una multa, y además se podrá inmovilizar el vehículo.",
            "c) La inmovilización del vehículo, pero no supone sanción económica."
        ],
        "c": "b",
        "img": "7.png"
    },
    {
        "p": "8. ¿Al aumentar la velocidad incrementa la probabilidad de muerte en caso de atropello a un peatón?",
        "ops": [
            "a) No, la velocidad del vehículo no tiene impacto significativo en la probabilidad de muerte de un peatón.",
            "b) Sí, al aumentar la velocidad de un vehículo se incrementa la probabilidad de fatalidad.",
            "c) La probabilidad es la misma, dependerá exclusivamente del estado de salud del peatón."
        ],
        "c": "b",
        "img": "8.png"
    },
    {
        "p": "9. ¿Cuántos espejos retrovisores tienen que llevar instalados las motocicletas?",
        "ops": [
            "a) Obligatoriamente uno en el lado derecho, pero pueden llevar dos.",
            "b) Siempre deben llevar dos espejos, uno en cada lado.",
            "c) Un espejo exterior izquierdo si no superan los 100 km/h y dos, uno en cada lado, si la velocidad es mayor."
        ],
        "c": "c",
        "img": "9.png"
    },
    {
        "p": "10. ¿Está permitida la circulación de animales por una carretera convencional?",
        "ops": [
            "a) Sí, únicamente cuando no exista vía pecuaria.",
            "b) No.",
            "c) Sí, excepto cuando circulen en rebaño."
        ],
        "c": "a",
        "img": "https://upload.wikimedia.org/wikipedia/commons/d/da/Spain_traffic_signal_p23.svg"
    },
    {
        "p": "11. ¿Qué aportan a la seguridad vial los sistemas avanzados de ayuda a la conducción también conocidos como ADAS?",
        "ops": [
            "a) Disminuyen el tiempo de reacción del conductor.",
            "b) Permiten al conductor reducir su nivel de alerta.",
            "c) Mejoran notablemente la seguridad activa del vehículo."
        ],
        "c": "c",
        "img": "11.png"
    },
    {
        "p": "12. ¿Cuál es la tasa de alcohol máxima permitida a un conductor novel?",
        "ops": [
            "a) 0,25 miligramos de alcohol por litro de aire espirado.",
            "b) 0,3 miligramos de alcohol por litro de aire espirado.",
            "c) 0,15 miligramos de alcohol por litro de aire espirado."
        ],
        "c": "c",
        "img": "12.png"
    },
    {
        "p": "13. Cuando un vehículo accidentado comienza a arder, ¿qué se debe hacer primero?",
        "ops": [
            "a) Apagar el fuego.",
            "b) Sacar rápidamente a los heridos.",
            "c) Ir a buscar ayuda."
        ],
        "c": "b",
        "img": "13.png"
    },
    {
        "p": "14. En esta situación (semáforo a la izquierda en rojo), ¿qué debe hacer si va a girar a la izquierda?",
        "ops": [
            "a) Continuar, obedeciendo al semáforo de la derecha.",
            "b) Detenerse, obedeciendo al semáforo situado a la izquierda.",
            "c) Sólo detenerse si hay peatones cruzando."
        ],
        "c": "b",
        "img": "14.png"
    },
    {
        "p": "15. ¿Está permitido colocar la señal luminosa de preseñalización de peligro, V-16, alejada del vehículo averiado?",
        "ops": [
            "a) Sí, alejado se podrá apreciar mejor.",
            "b) Sí, debe estar al menos a 100 metros.",
            "c) No, se debe colocar en la parte más alta posible del vehículo inmovilizado."
        ],
        "c": "c",
        "img": "15.png"
    },
    {
        "p": "16. Para entrar en una autopista, ¿a qué velocidad debe circular?",
        "ops": [
            "a) A la máxima velocidad permitida en la autopista.",
            "b) Siempre muy despacio para entrar con seguridad.",
            "c) A la velocidad adecuada que permita incorporarse con seguridad."
        ],
        "c": "c",
        "img": "16.png"
    },
    {
        "p": "17. ¿Qué es una detención?",
        "ops": [
            "a) La inmovilización del vehículo por necesidades de la circulación.",
            "b) Una parada por cualquier causa.",
            "c) Un estacionamiento sin bajarse del vehículo."
        ],
        "c": "a",
        "img": "https://images.unsplash.com/photo-1494832421162-538999141953?auto=format&fit=crop&q=80&w=600"
    },
    {
        "p": "18. Esta señal (perfil sinuoso con concavidad hacia arriba) indica peligro por la proximidad de...",
        "ops": [
            "a) una vía en mal estado.",
            "b) un badén en la vía.",
            "c) un resalto en la vía."
        ],
        "c": "b",
        "img": "18.png"
    },
    {
        "p": "19. En condiciones normales, la velocidad adecuada está siempre...",
        "ops": [
            "a) por debajo de la velocidad mínima.",
            "b) por encima de la velocidad máxima y por debajo de la mínima.",
            "c) por encima de la velocidad mínima y por debajo de la máxima."
        ],
        "c": "c",
        "img": "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&q=80&w=600"
    },
    {
        "p": "20. ¿Tiene alguna obligación cuando su vehículo va a ser adelantado?",
        "ops": [
            "a) Sí, señalizar con el intermitente derecho para indicar que puede realizar la maniobra.",
            "b) No, la responsabilidad es del vehículo que adelanta.",
            "c) Sí, ceñirse al borde derecho de la calzada para facilitar la maniobra."
        ],
        "c": "c",
        "img": "20.png"
    },
    {
        "p": "21. ¿Qué distancia de separación respecto al de delante debe mantener un vehículo de más de 3.500 kg en autovía?",
        "ops": [
            "a) 50 metros como mínimo.",
            "b) 50 metros si no pretende adelantar.",
            "c) La que le permita detenerse sin colisionar con él."
        ],
        "c": "c",
        "img": "https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80&w=600"
    },
    {
        "p": "22. El funcionamiento del airbag, ¿puede llegar a ser peligroso en un accidente?",
        "ops": [
            "a) Sí, siempre.",
            "b) Sí, si no se lleva puesto el cinturón de seguridad.",
            "c) No."
        ],
        "c": "b",
        "img": "22.png"
    },
    {
        "p": "23. ¿Cuál debe ser su comportamiento al ceder el paso?",
        "ops": [
            "a) Detenerse en las intersecciones si se acerca otro vehículo.",
            "b) Parar y comprobar si otro usuario de la vía tiene prioridad.",
            "c) No obligar al vehículo prioritario a modificar bruscamente su trayectoria o velocidad."
        ],
        "c": "c",
        "img": "https://upload.wikimedia.org/wikipedia/commons/8/87/Spain_traffic_signal_r1.svg"
    },
    {
        "p": "24. En esta vía de poblado de un solo carril por sentido, ¿a qué velocidad máxima se circula sin señales?",
        "ops": [
            "a) A 30 km/h.",
            "b) A 20 km/h.",
            "c) A 50 km/h."
        ],
        "c": "a",
        "img": "24.png"
    },
    {
        "p": "25. La fatiga, ¿provoca lentitud y falta de precisión en los movimientos?",
        "ops": [
            "a) No, la fatiga sólo produce calambres.",
            "b) No.",
            "c) Sí, por lo cual la conducción se hace más peligrosa."
        ],
        "c": "c",
        "img": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&q=80&w=600"
    },
    {
        "p": "26. Si los paneles de mensaje variable permiten circular por carril VAO a turismos con etiqueta B, ¿qué ocupación mínima requiere?",
        "ops": [
            "a) Dos ocupantes, incluido el conductor.",
            "b) Un ocupante.",
            "c) Dos ocupantes, sin incluir al conductor."
        ],
        "c": "b",
        "img": "26.png"
    },
    {
        "p": "27. Los accidentes de tráfico generan...",
        "ops": [
            "a) un enorme impacto económico, solamente.",
            "b) daños materiales y costes sanitarios, administrativos y humanos.",
            "c) daños materiales y costes humanos, únicamente."
        ],
        "c": "b",
        "img": "27.png"
    },
    {
        "p": "28. El efecto submarino, que provoca graves lesiones al conductor, está relacionado con...",
        "ops": [
            "a) Una incorrecta presión de los neumáticos.",
            "b) Un mal uso del cinturón de seguridad.",
            "c) Un consumo excesivo de alcohol, medicamentos o drogas."
        ],
        "c": "b",
        "img": "28.png"
    },
    {
        "p": "29. Si queda detenido en un atasco, ¿qué distancia es aconsejable mantener con el coche de delante?",
        "ops": [
            "a) Un metro como máximo.",
            "b) Un espacio mínimo para ocupar menos espacio.",
            "c) Dos o tres metros para evitar alcances traseros."
        ],
        "c": "c",
        "img": "29.png"
    },
    {
        "p": "30. Fuera de poblado, ¿qué separación lateral debe dejar una motocicleta al adelantar un camión?",
        "ops": [
            "a) Una distancia proporcional a la velocidad a la que circule.",
            "b) Un espacio no inferior a 1,50 metros.",
            "c) Una separación que considere segura en función de las circunstancias."
        ],
        "c": "b",
        "img": "30.png"
    }
]

# --- VARIABLES DE ESTADO ---
if "inicio" not in st.session_state:
    st.session_state.inicio = True
    st.session_state.index = 0
    st.session_state.errores = 0
    st.session_state.respuestas_usuario = []

# --- PANTALLA DE BIENVENIDA ---
if st.session_state.inicio:
    st.title("🚗 Autoescuela CHESTER - Test DGT")
    st.write("## ¡Pon a prueba tus conocimientos para la licencia española!")
    
    # Se muestra únicamente la foto y.png al inicio
    st.image("y.png", caption="🛴 ¿Conducir en chanclas? Spoiler de la Pregunta 1...")
        
    st.markdown("""
    ---
    ### 🗺️ Tu Ruta: Monumentos de Almazán a Soria
    Supera las preguntas para completar el viaje de forma segura por la provincia:
    * **Preguntas 1-10 (Etapa 1):** El Cruce de Almazán 🌉 (Puente medieval sobre el Duero).
    * **Preguntas 11-20 (Etapa 2):** Subida por la Puerta de la Villa 🏰 (Murallas históricas de Almazán).
    * **Preguntas 21-30 (Etapa 3):** El Reto Definitivo: Aparcamiento en El Collado de Soria 🚗 (La capital).
    
    **Reglas del Examen Oficial:**
    * Consta de **30 preguntas**.
    * Para conseguir tu **APTO**, debes cometer **como máximo 3 errores**.
    """)
    
    if st.button("🏁 INICIAR LA RUTA"):
        st.session_state.inicio = False
        st.rerun()

# --- PANTALLA DE PREGUNTAS ---
elif st.session_state.index < len(preguntas):
    q_idx = st.session_state.index
    q = preguntas[q_idx]
    
    # Lógica visual de etapas de Soria / Almazán
    if q_idx < 10:
        etapa_nombre = "📍 ETAPA 1: El Cruce de Almazán 🌉"
    elif q_idx < 20:
        etapa_nombre = "📍 ETAPA 2: Subida por la Puerta de la Villa 🏰"
    else:
        etapa_nombre = "📍 ETAPA 3: Aparcamiento en El Collado de Soria 🚗"
        
    st.markdown(f"<div class='etapa-header'><h3>{etapa_nombre}</h3></div>", unsafe_allow_html=True)
    st.progress(q_idx / len(preguntas))
    st.write(f"**Pregunta {q_idx + 1} de 30** | Errores en ruta: `{st.session_state.errores}`")
    
    st.markdown(f"<div class='card'><h4>{q['p']}</h4></div>", unsafe_allow_html=True)
    
    # Carga de imagen
    st.image(q["img"], use_container_width=True)
    
    # Opciones de respuesta
    seleccion = st.radio("Elige la respuesta correcta:", q["ops"], key=f"ans_{q_idx}")
    
    if st.button("SIGUIENTE DESAFÍO ➡️"):
        letra_sel = seleccion[0].lower()
        
        if letra_sel != q["c"]:
            st.session_state.errores += 1
            
        st.session_state.respuestas_usuario.append(letra_sel)
        st.session_state.index += 1
        st.rerun()

# --- PANTALLA DE RESULTADOS ---
else:
    st.title("📊 Resumen del Viaje por Soria")
    errores = st.session_state.errores
    st.write(f"### Has completado la ruta con **{errores} errores** de un total de 30 preguntas.")
    
    if errores <= 3:
        st.balloons()
        st.markdown("<p class='apto'>🏆 ¡APTO! Has llegado a El Collado de Soria de forma segura y sin multas. ¡Estás listo para el examen real!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='no-apto'>❌ NO APTO. La grúa municipal ha retirado tu coche en la Puerta de la Villa. Necesitas repasar (máximo 3 fallos).</p>", unsafe_allow_html=True)
        
    st.write("---")
    st.write("### 🔍 Historial de fallos en el trayecto:")
    
    any_error = False
    for i, q in enumerate(preguntas):
        tu_resp = st.session_state.respuestas_usuario[i]
        if tu_resp != q["c"]:
            any_error = True
            
            # Buscar el texto completo de la opción correcta
            opcion_correcta_texto = ""
            for opcion in q["ops"]:
                if opcion.strip().lower().startswith(q["c"]):
                    opcion_correcta_texto = opcion
                    break
            
            st.warning(f"**Pregunta {i+1} (Etapa {1 if i<10 else 2 if i<20 else 3}):** {q['p']}")
            
            # Encontrar también el texto completo de la opción que eligió el usuario
            opcion_usuario_texto = ""
            for opcion in q["ops"]:
                if opcion.strip().lower().startswith(tu_resp):
                    opcion_usuario_texto = opcion
                    break
                    
            st.write(f"❌ **Tu respuesta:** {opcion_usuario_texto}")
            st.write(f"✔️ **Respuesta correcta:** {opcion_correcta_texto}")
            st.write(" ")
            
    if not any_error:
        st.success("✨ ¡Increíble! ¡Un viaje perfecto sin un solo fallo de Almazán a Soria!")
            
    if st.button("HACER OTRA RUTA 🔄"):
        st.session_state.inicio = True
        st.session_state.index = 0
        st.session_state.errores = 0
        st.session_state.respuestas_usuario = []
        st.rerun()
