import numpy as np
import matplotlib.pyplot as plt
from src.config import files
from src.data_manager import DataManager
from typing import List, Dict
import os


def plot_data():
    dm = DataManager(files)
    collection_data: List[Dict[str, np.ndarray]] = dm.load_data(columns=["strain", "stress"])

    for data in collection_data:
        strain = data["strain"]
        stress = data["stress"]

        x1, x2 = 0.3, 0.5
        y1 = np.interp(x1, strain, stress)
        y2 = np.interp(x2, strain, stress)

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        max_stress = np.max(stress)
        max_strain = (max_stress - b) / m
        max_strain = min(max_strain, strain.iloc[-1])

        # recta ajustada
        adjusted_strain = strain[strain <= max_strain]
        adjusted_initial_line_y = m * adjusted_strain + b

        # recta desplazada
        displacement = 0.03 * (strain.iloc[-1] - strain.iloc[0])
        displaced_strain = adjusted_strain + displacement

        # Buscar el punto de cedencia (donde se cortan)
        cedence_strain = None
        cedence_stress = None
        for i, strain_value in enumerate(displaced_strain):
            stress_value = np.interp(strain_value, strain, stress)
            y = adjusted_initial_line_y[i]
            if y > stress_value:
                cedence_strain = strain_value
                cedence_stress = stress_value
                break
    

        plt.plot(strain, stress, label="Curva de esfuerzo-deformación")
        # plt.plot(adjusted_strain, adjusted_initial_line_y,
        #          label="Recta inicial", linestyle="--")
        plt.plot(displaced_strain, adjusted_initial_line_y,
                 label="Recta desplazada 3%", linestyle="-.")
        
        if cedence_strain is not None and cedence_stress is not None:
            plt.scatter(cedence_strain, cedence_stress, color='red', label="Punto de cedencia")

        plt.xlabel("Deformación")
        plt.ylabel("Esfuerzo")
        plt.legend()
        plt.title("Diagrama Esfuerzo-Deformación y Puntos de Cedencia")
        
        if not os.path.exists("output"):
            os.makedirs("output")

        plt.savefig(f"output/plot.png")


if __name__ == "__main__":
    plot_data()
