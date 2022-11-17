import matplotlib.pyplot as plt


def chart_graph(data, inversor_name, fname):
    plt.plot(data['fecha_im'], data['active_energy_im'], color='#0343df')

    plt.title('Producción diaria Inversor id: {}'.format(inversor_name))
    plt.ylabel('Producción')
    plt.xlabel('Fecha')

    plt.savefig('{}_{}.png'.format(fname, inversor_name), dpi='figure', format=None, metadata=None,
                bbox_inches=None,
                facecolor='auto', edgecolor='auto',
                backend=None)
    plt.show()


def graph_result(data):
    print(data)