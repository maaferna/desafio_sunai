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
    size = len(data)
    colormap = ["#fffac8", "#ffd8b1", "#fabed4", "#a9a9a9", "#911eb4",
                "#4363d8", "#42d4f4", "#469990", "#f58231", "#800000"]
    legend_list = []
    for l in range(0, size):
        legend_list.append(data.iloc[l, 0] + "/" + str(data.iloc[l, 1]))

    print(legend_list)

    fig, axs = plt.subplots(2, 1, figsize=(15, 10), sharey=False, sharex=True)

    title_list = ['Active Energy (min/max/average)', 'Active Energy Total']

    axs[0].title.set_text(title_list[0])
    axs[0].plot(data['id_i'].map(str), data['Minimum'], color='red', label='Min')
    axs[0].plot(data['id_i'].map(str), data['Mean'], color='blue', label='Average')
    axs[0].plot(data['id_i'].map(str), data['Maximum'], color='green', label='Max')
    axs[1].title.set_text(title_list[1])
    axs[1].plot(data['id_i'].map(str), data['Sum'], color='green')

    axs[0].legend( )
    plt.show()
