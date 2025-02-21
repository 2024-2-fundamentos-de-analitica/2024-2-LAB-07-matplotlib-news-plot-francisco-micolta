"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    
    # Ruta de entrada y salida
    input_file = "files/input/news.csv"
    output_dir = "files/plots"
    output_file = os.path.join(output_dir, "news.png")

    # Asegurar que la carpeta de salida exista
    os.makedirs(output_dir, exist_ok=True)

    # Cargar el archivo CSV, usando la primera columna como "Year"
    df = pd.read_csv(input_file, index_col=0)
    df.index.name = "Year"
    df = df.reset_index()

    # Configurar el tamaño de la figura
    plt.figure(figsize=(10, 6))

    # Usar un estilo alternativo si "seaborn-darkgrid" no está disponible
    try:
        plt.style.use("seaborn-darkgrid")
    except OSError:
        plt.style.use("ggplot")  # Alternativa segura

    # Graficar cada medio de comunicación
    plt.plot(df["Year"], df["Television"], label="Television", color="black", linestyle="-", marker="o", alpha=0.7)
    plt.plot(df["Year"], df["Newspaper"], label="Newspaper", color="gray", linestyle="-", marker="o", alpha=0.7)
    plt.plot(df["Year"], df["Radio"], label="Radio", color="lightgray", linestyle="-", marker="o", alpha=0.7)
    plt.plot(df["Year"], df["Internet"], label="Internet", color="blue", linestyle="-", marker="o", linewidth=3)

    # Etiquetas de porcentaje en los extremos
    plt.text(df["Year"].iloc[0], df["Television"].iloc[0], f"{df['Television'].iloc[0]}%", color="black", fontsize=12)
    plt.text(df["Year"].iloc[-1], df["Television"].iloc[-1], f"{df['Television'].iloc[-1]}%", color="black", fontsize=12)

    plt.text(df["Year"].iloc[0], df["Newspaper"].iloc[0], f"{df['Newspaper'].iloc[0]}%", color="gray", fontsize=12)
    plt.text(df["Year"].iloc[-1], df["Newspaper"].iloc[-1], f"{df['Newspaper'].iloc[-1]}%", color="gray", fontsize=12)

    plt.text(df["Year"].iloc[0], df["Radio"].iloc[0], f"{df['Radio'].iloc[0]}%", color="lightgray", fontsize=12)
    plt.text(df["Year"].iloc[-1], df["Radio"].iloc[-1], f"{df['Radio'].iloc[-1]}%", color="lightgray", fontsize=12)

    plt.text(df["Year"].iloc[0], df["Internet"].iloc[0], f"{df['Internet'].iloc[0]}%", color="blue", fontsize=12)
    plt.text(df["Year"].iloc[-1], df["Internet"].iloc[-1], f"{df['Internet'].iloc[-1]}%", color="blue", fontsize=12)

    # Título y subtítulo
    plt.title("How people get their news", fontsize=16)
    plt.suptitle("An increasing proportion cite the internet as their primary news source", fontsize=10)

    # Etiquetas de los ejes
    plt.xlabel("")
    plt.ylabel("Percentage")

    # Guardar la gráfica
    plt.savefig(output_file, dpi=300)
    plt.close()

    print(f"✅ Gráfico guardado en {output_file}")

if __name__ == "__main__":
    pregunta_01()