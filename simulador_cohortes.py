
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos del modelo por cohortes
@st.cache_data
def cargar_datos():
    return pd.read_csv("proyeccion_pensiones_cohortes_2025_2050.csv")

df = cargar_datos()

st.title("Simulador de Pensiones por Cohortes Demográficas (2025–2050)")

# Sidebar: controles de ajustes
st.sidebar.header("Ajustes de política")
ajuste_cotizacion = st.sidebar.slider("Ajuste % cotización inicial", 80, 120, 100) / 100
ajuste_pension = st.sidebar.slider("Ajuste % pensión inicial", 80, 120, 100) / 100
crecimiento_cotizacion = st.sidebar.slider("Crecimiento anual cotización (%)", 0.0, 5.0, 2.0) / 100
crecimiento_pension = st.sidebar.slider("Crecimiento anual pensión (%)", 0.0, 5.0, 2.5) / 100

# Recalcular con ajustes
cotizacion_base = 320 * ajuste_cotizacion
pension_base = 1260 * ajuste_pension
df["Cotizacion_Media"] = [cotizacion_base * (1 + crecimiento_cotizacion) ** i for i in range(len(df))]
df["Pension_Media"] = [pension_base * (1 + crecimiento_pension) ** i for i in range(len(df))]

df["Ingresos"] = df["Cotizantes_estimados"] * df["Cotizacion_Media"] * 12
df["Gastos"] = df["Pensionistas_estimados"] * df["Pension_Media"] * 12
df["Balance"] = df["Ingresos"] - df["Gastos"]

# Mostrar métricas del último año
ultimo = df[df["Año"] == 2050].iloc[0]
st.subheader("Resumen del año 2050")
st.metric("Ingresos", f"{ultimo['Ingresos']/1e9:,.2f} M €")
st.metric("Gastos", f"{ultimo['Gastos']/1e9:,.2f} M €")
st.metric("Balance", f"{ultimo['Balance']/1e9:,.2f} M €", delta=f"{(ultimo['Balance']/ultimo['Ingresos'])*100:.2f}%")

# Gráfico de balance
st.subheader("Balance anual del sistema")
fig, ax = plt.subplots()
ax.plot(df["Año"], df["Balance"] / 1e9, label="Balance", marker='o')
ax.axhline(0, color='red', linestyle='--')
ax.set_ylabel("Miles de millones €")
ax.set_xlabel("Año")
ax.grid(True)
st.pyplot(fig)

# Mostrar tabla si se desea
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df[["Año", "Cotizantes_estimados", "Pensionistas_estimados", "Cotizacion_Media", "Pension_Media", "Ingresos", "Gastos", "Balance"]])
