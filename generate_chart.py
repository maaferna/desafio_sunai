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
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    title_list = ['Active Energy (min/max/average)', 'Total Active Energy']

    ax1.set_title(title_list[0])
    ax1.plot(data['id_i'].map(str), data['Minimum'], color='red', label='Min',  linewidth=3)
    ax1.plot(data['id_i'].map(str), data['Mean'], color='blue', label='Average', linewidth=2)
    ax1.plot(data['id_i'].map(str), data['Maximum'], color='green', label='Max', linewidth=1)
    ax2.title.set_text(title_list[1])
    ax2.plot(data['id_i'].map(str), data['Sum'], color='green')

    ax1.legend()
    plt.tight_layout()
    plt.savefig('kpi.png', dpi='figure', format=None, metadata=None,
                bbox_inches=None,
                facecolor='auto', edgecolor='auto',
                backend=None)
    plt.show()
