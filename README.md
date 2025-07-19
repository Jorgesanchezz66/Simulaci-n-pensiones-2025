# Simulador de Pensiones en España (2025–2050)


Este proyecto evalúa la sostenibilidad del sistema público de pensiones en España a 25 años vista, utilizando datos reales y modelos cuantitativos. Incluye una aplicación interactiva desarrollada en Streamlit, basada en proyecciones demográficas, económicas y estructurales del sistema.


 Objetivo

Simular de forma realista el comportamiento del sistema público de pensiones en España entre 2025 y 2050, y permitir al usuario:

- Ajustar supuestos económicos y demográficos.
- Visualizar ingresos, gastos y balance del sistema.
- Entender el impacto del envejecimiento y del mercado laboral en la sostenibilidad del modelo actual.


 Metodología

Se ha construido un modelo **determinista por cohortes demográficas**, en el que:

- Los **cotizantes** se estiman como:
  > población de 15–64 años × tasa de actividad × tasa de empleo.

- Los **pensionistas** se estiman como:
  > población de 65+ años × tasa de jubilación (100%).

- Los **ingresos** provienen de cotización mensual por cotizante.
- Los **gastos** se calculan como pensión mensual por pensionista.
- El **balance** es la diferencia anual entre ingresos y gastos.

Todos los valores se proyectan año a año en base a tasas de crecimiento ajustables por el usuario.


## 🚀 Cómo ejecutar la aplicación

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/simulador-pensiones-espana.git
cd simulador-pensiones-espana
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la app interactiva:

bash
Copiar
Editar
streamlit run streamlit_app/simulador_cohortes.py
🌐 ¿Qué puedes hacer con la app?
Ajustar tasas de cotización y pensión inicial.

Cambiar los crecimientos anuales proyectados.

Visualizar el balance anual entre ingresos y gastos.

Identificar si el sistema entra en déficit o superávit bajo distintos escenarios.

📚 Fuentes
Población proyectada: INE / PopulationPyramid.net

Supuestos económicos: Seguridad Social / AIReF / OCDE

✍️ Autor
Jorge Sánchez González
Estudiante de Máster en Big Data & Business Analytics
Graduado en Finanzas y ADE | Apasionado por la economía y la analítica
