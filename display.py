import streamlit as st

def display_header(title: str) -> None:
    """Muestra el título de la aplicación"""
    st.title(title)

def display_form() -> None:
    """Muestra el formulario de ingreso de datos"""
    with st.form(key='user_form'):
        edad = st.number_input("Edad", min_value=0, max_value=120, step=1, value=10)
        altura = st.slider("Altura (cm)", min_value=1, max_value=300)
        peso = st.slider("Peso (kg)", min_value=1, max_value=500)
        genero = st.radio("Género", options=["Masculino", "Femenino"])
        actividad = st.select_slider("Nivel de Actividad", options=[
            'Sedentario',
            'Ligeramente activo (1-3 días/semana)',
            'Moderadamente activo (3-5 días/semana)',
            'Muy activo (6-7 días/semana)',
            'Extra activo'
        ])


        objetivo_comidas = st.radio("Objetivo de Comidas", options=[
            "Pérdida de peso",
            "Mantenimiento",
            "Ganancia de Masa Muscular"
        ])
        cant_comidas = st.number_input("Cantidad de Alimentos por día", min_value=1, max_value=10, step=1)
        submit_button = st.form_submit_button(label='Calcular')
       
    return edad, altura, peso, genero, actividad, objetivo_comidas, cant_comidas, submit_button

def display_user_data(persona) -> None:
    """Muestra los datos ingresados por el usuario"""
    st.header("Datos Ingresados")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"**Edad:**")
        st.write(f"**{persona.edad}** años")
        st.subheader(f"**Altura:**")
        st.write(f"**{persona.altura}** cm")
        st.subheader(f"**Peso:**")
        st.write(f"**{persona.peso}** kg")
        st.subheader(f"**Género:**")
        st.write(f"**{persona.genero}**")
    with col2:
        st.subheader(f"**Nivel de Actividad:**")
        st.write(f"**{persona.actividad}**")
        st.subheader(f"**Objetivo de Comidas:**")
        st.write(f"**{persona.objetivo_comidas}**")
        st.subheader(f"**Cantidad de Comidas por Día:**")
        st.write(f"**{persona.cant_comidas}** ")

def display_calculated_data(persona) -> None:
    """Muestra los datos calculados"""
    st.header("Datos Calculados")
    
    #IMC
    st.subheader(f"**IMC calculado**")
    imc_texto, categoria, color = persona.mostrar_resultados()
    st.metric(label="**Índice de Masa Corporal:**", value=imc_texto)
    new_title = f'<p style="font-family:sans-serif; color:{color}; font-size: 25px;">{categoria}</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown(
        """
        Rango de IMC saludable: 18.5 kg/m² - 25 kg/m².
        """) 
    
    #TMB
    st.subheader(f"TMB calculado")
    st.metric(label="**Tasa Metabólica Basal:**", value=persona.calcular_tmb())
    
    #Calorias
    st.subheader(f"Calculo de calorias recomendadas")
    st.metric(label="**Ingesta de Calorias diarias recomendadas:**", value=persona.calculador_calorias())
    
    #Macronutrientes
    st.subheader(f"**Distribución de Macronutrientes:**")
    azucares, proteinas_diarias, calo_proteinas_diarias, grasas_diarias, calo_grasas_diarias, calo_carbohidratos_diarias, carbohidratos_diarios = persona.distribuir_macronutrientes()
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label= "Azucares", value=azucares)
        st.metric(label="Proteinas diarias", value=proteinas_diarias)
        st.metric(label="Calorias en proteinas", value=calo_proteinas_diarias)

    with col2:
        st.metric(label="Grasas diarias", value=grasas_diarias)
        st.metric(label="Calorias en grasas", value=calo_grasas_diarias)

    with col3:
        st.metric(label="Calorias en carbohidratos", value=calo_carbohidratos_diarias)
        st.metric(label="Carbohidratos diarios", value=carbohidratos_diarios)

def display_recommendations(recomendaciones) -> None:
    """Muestra las recomendaciones"""
    st.write("### Recomendaciones")

    # Desempaqueta las recomendaciones
    recommended_foods, Calorias, Grasas, Carbohidratos, Proteinas, Azucares = recomendaciones

    # Crea una lista de diccionarios para la tabla
    data = []
    for i in range(len(recommended_foods[0])):
        data.append({
            "Nombre": recommended_foods[0][i],
            "Calorias": Calorias[0][i],
            "Grasas": Grasas[0][i],
            "Carbohidratos": Carbohidratos[0][i],
            "Proteinas": Proteinas[0][i],
            "Azucares": Azucares[0][i]
        })

    # Muestra la tabla
    st.table(data)
