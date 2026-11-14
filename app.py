import streamlit as st 

#Defining the title of the web application
st.title("Chromatography Calculator")
#Creating Tabs for various calculations
tab1, tab2, tab3, tab4 = st.tabs(["Column Volume", "Flow Rate Converter"," Residence Time Calculator","Flow Rate from Residence Time"])
#Creating Columns to arrange the input fields side by side
#Creating the first tab for Column Volume Calculation
with tab1:
    cols = st.columns(2)
    with cols[0]:
        st.number_input("Bed Height (cm) :", min_value=0.0, max_value=None, value=10.0, step=0.1, key="bed_height")
        st.number_input("Column Diameter (cm) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="column_diameter")
        #Creating a session state variable to store the calculated volume
        if "volume" not in st.session_state:
            st.session_state.volume = 7.85
        def calculate_parameters():
            bed_height = st.session_state.bed_height
            column_diameter = st.session_state.column_diameter
            #Calculation of column volume
            import math
            radius = column_diameter / 2
            volume = math.pi * (radius ** 2) * bed_height
            st.session_state.volume = volume
        st.button("Calculate", on_click=calculate_parameters,shortcut="ctrl+enter",key="calculate_volume")


        
    with cols[1]:
        st.metric(label="Column Volume", value=f"{st.session_state.volume:.2f} ml")
#Creating Second Tab for Flow Rate Conversion
with tab2:
    #Create Two tabs to be able to convert from Volumetric Flowrate to linear velocity and vice versa 
    tabs = st.tabs(["Volumetric Flowrate to Linear Velocity", "Linear Velocity to Volumetric Flowrate"])
    with tabs[0]:
        cols = st.columns(2)
        with cols[0]:
            st.number_input("Linear Velocity (cm/h) :", min_value=0.0, max_value=None, value=100.0, step=1.0, key="linear_velocity   ")
            st.number_input("Column Diameter (cm) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="column_diameter_flow")
            #Creating a session state variable to store the converted flow rate      
            if "converted_flow_rate" not in st.session_state:
                    st.session_state.converted_flow_rate = 0.0
            if "linear_velocity" not in st.session_state:
                    st.session_state.linear_velocity = 100.0
            if "column_diameter_flow" not in st.session_state:
                    st.session_state.column_diameter_flow = 1.0
            def calculate_flow_rate():
                    linear_velocity = st.session_state.linear_velocity
                    column_diameter = st.session_state.column_diameter_flow
                    #Calculation of flow rate
                    import math
                    radius = column_diameter / 2
                    area = math.pi * (radius ** 2)
                    flow_rate = linear_velocity * area / 60  # Convert cm^3/h to ml/min
                    st.session_state.converted_flow_rate = flow_rate

        st.button("Convert", on_click=calculate_flow_rate,shortcut="ctrl+enter",key="convert_flow_rate")
        with cols[1]:
            st.metric(label="Converted Flow Rate", value=f"{st.session_state.converted_flow_rate:.2f} ml/min")
    with tabs[1]:
        cols = st.columns(2)
        with cols[0]:
            st.number_input("Flow Rate (ml/min) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="flow_rate_linear")
            st.number_input("Column Diameter (cm) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="column_diameter_linear")
            #Creating a session state variable to store the converted linear velocity
            if "converted_linear_velocity" not in st.session_state:
                    st.session_state.converted_linear_velocity = 0.0
            if "flow_rate_linear" not in st.session_state:
                    st.session_state.flow_rate_linear = 1.0
            if "column_diameter_linear" not in st.session_state:
                    st.session_state.column_diameter_linear = 1.0
            def calculate_linear_velocity():
                    flow_rate = st.session_state.flow_rate_linear
                    column_diameter = st.session_state.column_diameter_linear
                    #Calculation of linear velocity
                    import math
                    radius = column_diameter / 2
                    area = math.pi * (radius ** 2)
                    linear_velocity = (flow_rate * 60) / area  # Convert ml/min to cm^3/h
                    st.session_state.converted_linear_velocity = linear_velocity

        st.button("Convert", on_click=calculate_linear_velocity,shortcut="ctrl+enter",key="convert_linear_velocity")
        with cols[1]:
            st.metric(label="Converted Linear Velocity", value=f"{st.session_state.converted_linear_velocity:.2f} cm/h")
         
#Creating Third Tab for Residence Time Calculation
with tab3:
    cols = st.columns(2)
    with cols[0]:
        st.number_input("Column Volume (ml) :", min_value=0.0, max_value=None, value=20.00, step=0.1, key="column_volume")
        st.number_input("Flow Rate (ml/min) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="flow_rate")
        #Creating a session state variable to store the calculated residence time
        if "residence_time" not in st.session_state:
            st.session_state.residence_time = 1.0
        def calculate_residence_time():
            column_volume = st.session_state.column_volume
            flow_rate = st.session_state.flow_rate
            #Calculation of residence time
            if flow_rate > 0:
                residence_time = column_volume / flow_rate
                st.session_state.residence_time = residence_time
            else:
                st.session_state.residence_time = float('inf')  # Handle division by zero

        st.button("Calculate", on_click=calculate_residence_time,shortcut="ctrl+enter",key="calculate_residence_time")
    with cols[1]:
        st.metric(label="Residence Time", value=f"{st.session_state.residence_time:.2f} min")
#Creating Fourth Tab for Flow Rate from Residence Time Calculation
with tab4:
    cols = st.columns(2)
    with cols[0]:
        st.number_input("Residence Time (min) :", min_value=0.0, max_value=None, value=1.0, step=0.1, key="residence_time_input")
        st.number_input("Column Volume (ml) :", min_value=0.0, max_value=None, value=7.85, step=0.1, key="column_volume_input")
        #Creating a session state variable to store the calculated flow rate
        if "calculated_flow_rate" not in st.session_state:
            st.session_state.calculated_flow_rate = 1.0
        def calculate_flow_rate_from_residence_time():
            residence_time = st.session_state.residence_time_input
            column_volume = st.session_state.column_volume_input
            #Calculation of flow rate from residence time
            if residence_time > 0:
                flow_rate = column_volume / residence_time
                st.session_state.calculated_flow_rate = flow_rate
            else:
                st.session_state.calculated_flow_rate = float('inf')  # Handle division by zero

        st.button("Calculate", on_click=calculate_flow_rate_from_residence_time,shortcut="ctrl+enter",key="calculate_flow_rate_from_residence_time")
    with cols[1]:
        st.metric(label="Flow Rate", value=f"{st.session_state.calculated_flow_rate:.2f} ml/min")
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 0.85rem;'>"
    "Developed by <b>Yusif Qabil</b> | Downstream Processing Calculation Suite"
    "</p>", 
    unsafe_allow_html=True
)