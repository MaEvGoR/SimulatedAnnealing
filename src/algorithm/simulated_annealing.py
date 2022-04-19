# import plotly.express as px
import plotly.graph_objects as go
from random import shuffle, choices
import numpy as np

from src.algorithm.node import Node


class Algo:

    def __init__(
        self,
        annealing_rate=0.999,
        start_temp=100000,
        cooldown=1e-6
    ):
        self.data = None
        self.nodes = None
        self.path = None
        self.step_number = None
        self.annealing_rate = annealing_rate
        self.start_temperature = start_temp
        self.cooldown = 1e-6

    def _precondition(self):
        if self.data is None:
            raise ValueError('Hui tebe')

    def setup(self, raw_data):
        self.data = raw_data
        self.generate_nodes()
        self.temperature = self.start_temperature
        self.create_random_path()
        self.cost = self.calculate_cost(self.path)
        self.set_step(0)

    def set_step(self, value):
        self.step_number = value

    def update_temperature(self):
        self.temperature *= self.annealing_rate

    def create_random_path(self):
        self.path = [*self.nodes.keys()]
        shuffle(self.path)

    def generate_nodes(self):
        self.nodes = {}
        for index, row in self.data.df.iterrows():
            self.nodes[index] = Node((row['geo_lon'], row['geo_lat']))

    @property
    def _num_of_nodes(self):
        return len(self.path)

    def step(self):
        self._precondition()

        neighbour_path = self._neighbour
        neighbour_cost = self.calculate_cost(neighbour_path)

        coin_flip = np.random.uniform()
        threshold = np.exp(-neighbour_cost/self.temperature)

        if neighbour_cost < self.cost:
            # print(f'NEW PATH! {neighbour_path}')
            self.path = neighbour_path
            self.cost = neighbour_cost
        elif coin_flip < threshold:
            # print(f'Lucky bastard! {neighbour_path} ({coin_flip:.3f} < {threshold:.3f})')
            self.path = neighbour_path
            self.cost = neighbour_cost

        self.update_temperature()
        self.set_step(self.step_number + 1)

    @property
    def heat(self):
        return self.temperature >= self.cooldown

    def solve(self):
        while self.heat:
            self.step()

            # with open(f'src/data/raw/statistics.csv', 'a') as f:
            #     f.write(f'{self.step_number},{self.cost},{self.start_temperature},{self.annealing_rate}\n')

    def calculate_cost(self, path):
        distances = []
        for i in range(self._num_of_nodes - 1):
            left_node_idx = path[i]
            right_node_idx = path[i + 1]

            left_node = self.nodes[left_node_idx]
            right_node = self.nodes[right_node_idx]

            distances.append(left_node >> right_node)

        first_node = self.nodes[path[0]]
        last_node = self.nodes[path[-1]]

        distances.append(first_node >> last_node)
        return sum(distances)

    @property
    def _neighbour(self):
        left_idx, right_idx = choices(
            [*range(self._num_of_nodes)],
            k=2
        )

        pth = self.path.copy()
        pth[left_idx], pth[right_idx] = pth[right_idx], pth[left_idx]

        return pth

    def summary(self):
        title = [
            f'Temp: {self.temperature:.2f}',
            f'Cost: {self.cost:.2f}',
            f'Step: {self.step_number}'
        ]
        return ", ".join(title)

    def figure(self):

        fig = go.Figure()
        fig = go.Figure(
            go.Scattergeo(
                lon=self.data.df['geo_lon'],
                lat=self.data.df['geo_lat'],
                hoverinfo='text',
                text=self.data.df['city'],
                mode='markers',
                marker=dict(
                    size=2,
                    color='rgb(255, 0, 0)',
                    line=dict(
                        width=3,
                        color='rgba(68, 68, 68, 0)'
                    )
                )
            )
        )

        path_nodes = self.data.df.loc[self.path + [self.path[0]]]

        for i in range(len(path_nodes) - 1):
            left = path_nodes.iloc[i]
            right = path_nodes.iloc[i + 1]

            fig.add_trace(
                go.Scattergeo(
                    lon=[left['geo_lon'], right['geo_lon']],
                    lat=[left['geo_lat'], right['geo_lat']],
                    mode='lines',
                    line=dict(
                        width=1,
                        color='red'
                    )
                )
            )

        fig.update_geos(
            center=dict(lon=63.161757, lat=92.733444),
            lataxis_range=[-10, 100], lonaxis_range=[-10, 10],
        )

        fig.update_layout(height=700, showlegend=False)

        return fig


algo = Algo()