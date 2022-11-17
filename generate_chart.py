import matplotlib.pyplot as plt

def chart_graph(data):
    plt.bar(data['fecha_im'], data['active_energy_im'], color='#0343df')

    plt.title('Producción diaria')
    plt.ylabel('Producción')
    plt.xlabel('Fecha')
    plt.show()