import matplotlib.pyplot as plt

def chart_graph(data):
    plt.bar(data['id'], data['test'], color='#0343df')

    plt.title('Producción diaria')
    plt.ylabel('Producción')
    plt.xlabel('Fecha')
    plt.show()