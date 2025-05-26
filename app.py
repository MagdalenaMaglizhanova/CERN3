import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Детекторна стая", layout="wide")

st.title("🔬 Детекторна стая")

st.sidebar.header("🔧 Настройки на частицата")

# Избор на параметри
particle_type = st.sidebar.selectbox("Тип частица", ["Електрон", "Протон", "Мюон"])
energy = st.sidebar.slider("Енергия (GeV)", 1, 100, 20)
angle_deg = st.sidebar.slider("Ъгъл на отклонение (градуси)", -45, 45, 0)

# Пресмятане на траектория
angle_rad = np.radians(angle_deg)
z = np.linspace(0, 10, 100)
x = np.tan(angle_rad) * z
y = np.zeros_like(z)

# Цветове по тип
colors = {"Електрон": "blue", "Протон": "red", "Мюон": "green"}

fig = go.Figure()

# Добавяме слоеве (калориметри и др.)
layers = [2, 5, 8]
for layer in layers:
    fig.add_trace(go.Scatter3d(x=[-5, 5], y=[-5, 5], z=[layer, layer],
                               mode='lines',
                               line=dict(color='gray', width=2),
                               showlegend=False))

# Частица
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines',
                           name=f"{particle_type} ({energy} GeV)",
                           line=dict(width=4, color=colors[particle_type])))

# Център на сблъсък
fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers',
                           marker=dict(size=5, color='black'),
                           name="Сблъсък"))

fig.update_layout(
    scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
    height=700,
    title="🧲 Визуализация на детектор",
)

st.plotly_chart(fig, use_container_width=True)

# Резултат/анализ
st.subheader("📊 Анализ")

if particle_type == "Електрон":
    st.write("Електронът се отклонява силно от магнитното поле и се абсорбира от електромагнитния калориметър.")
elif particle_type == "Протон":
    st.write("Протонът преминава по-директно и оставя следа в хадаронния калориметър.")
else:
    st.write("Мюонът преминава през всички слоеве и се открива в мюонен детектор.")

st.info("🧠 Опитай да промениш енергията и ъгъла и наблюдавай как се променя движението!")
