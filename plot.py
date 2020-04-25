import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class plotar(object):

    def __init__(self, terminais):
        self.terminais = terminais

    def plot_1(self, graph1, title1):
        graph_1, end_nodes_1, Graph_1 = {}, [], nx.Graph()
        graph_1 = self.passarprastring(graph1)

        for node in graph_1:
            Graph_1.add_nodes_from(node)
            
            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_1.append(str(int(node)))

            for edge, weight in graph_1[node].items():
                Graph_1.add_edge(node,edge, weight=weight)

        graph_layout1 = nx.spring_layout(Graph_1)
        labels_1 = nx.get_edge_attributes(Graph_1,'weight')
        nx.draw_networkx_nodes(Graph_1, graph_layout1)
        nx.draw_networkx_labels(Graph_1, graph_layout1, edge_labels= labels_1, node_color = 'b')
        nx.draw_networkx(Graph_1, graph_layout1, nodelist= end_nodes_1, node_color= 'r')
        plt.title(title1)
        plt.show()

    def plot_2(self, graph1, graph2,  title1:str, title2:str):
        graph_1, graph_2= {},{}
        end_nodes_1, end_nodes_2 = [], []
        Graph_1, Graph_2= nx.Graph(), nx.Graph()

        graph_1 = self.passarprastring(graph1)
        graph_2 = self.passarprastring(graph2)
       
        for node in graph_1:
            Graph_1.add_nodes_from(node)

            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_1.append(node)

            for edge, weight in graph_1[node].items():
                Graph_1.add_edge(node, edge, weight = weight)

        for node in graph_2:
            Graph_2.add_nodes_from(node)

            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_2.append(node)

            for edge, weight in graph_2[node].items():
                Graph_2.add_edge(node, edge, weight = weight)


        
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))
        graph_layout1 = nx.spring_layout(Graph_1)
        graph_layout2 = nx.spring_layout(Graph_2)

        labels_1 = nx.get_edge_attributes(Graph_1,'weight')
        labels_2 = nx.get_edge_attributes(Graph_2,'weight')



        nx.draw_networkx_nodes(Graph_1, graph_layout1, ax=axes[0])
        nx.draw_networkx_labels(Graph_1, graph_layout1, edge_labels= labels_1, node_color = 'b', ax=axes[0])
        nx.draw_networkx_edges(Graph_1, graph_layout1,
                               ax=axes[0])
        nx.draw_networkx(Graph_1, graph_layout1, nodelist= end_nodes_1, node_color= 'r', ax = axes[0])
        axes[0].set_title(title1)

        nx.draw_networkx_nodes(Graph_2, graph_layout2, ax=axes[1])
        nx.draw_networkx_labels(Graph_2, graph_layout2, edge_labels= labels_2, ax=axes[1])
        nx.draw_networkx_edges(Graph_2, graph_layout2,
                               ax=axes[1])
        nx.draw_networkx(Graph_2, graph_layout2, nodelist= end_nodes_2, node_color= 'r', ax = axes[1])
        axes[1].set_title(title2)
        plt.show()
       


    def plot_3(self, graph1, graph2, graph3, title1:str, title2:str, title3:str):
        graph_1, graph_2, graph_3 = {},{},{}
        end_nodes_1, end_nodes_2, end_nodes_3 = [], [], []
        Graph_1, Graph_2, Graph_3 = nx.Graph(), nx.Graph(), nx.Graph()

        graph_1 = self.passarprastring(graph1)
        graph_2 = self.passarprastring(graph2)
        graph_3 = self.passarprastring(graph3)

        for node in graph_1:
            Graph_1.add_nodes_from(node)

            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_1.append(node)

            for edge, weight in graph_1[node].items():
                Graph_1.add_edge(node, edge, weight = weight)

        for node in graph_2:
            Graph_2.add_nodes_from(node)

            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_2.append(node)

            for edge, weight in graph_2[node].items():
                Graph_2.add_edge(node, edge, weight = weight)

        for node in graph_3:
            Graph_3.add_nodes_from(node)

            for terminal in range(len(self.terminais)):
                if(str(self.terminais[terminal]) == node):
                    end_nodes_3.append(node)

            for edge, weight in graph_3[node].items():
                Graph_3.add_edge(node, edge, weight = weight)   

        
        fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 10))
        graph_layout1 = nx.spring_layout(Graph_1)
        graph_layout2 = nx.spring_layout(Graph_2)
        graph_layout3 = nx.spring_layout(Graph_3)
      
        labels_1 = nx.get_edge_attributes(Graph_1,'weight')
        labels_2 = nx.get_edge_attributes(Graph_2,'weight')
        labels_3 = nx.get_edge_attributes(Graph_3,'weight')


        nx.draw_networkx_nodes(Graph_1, graph_layout1, ax=axes[0])
        nx.draw_networkx_labels(Graph_1, graph_layout1, edge_labels= labels_1, node_color = 'b', ax=axes[0])
        nx.draw_networkx_edges(Graph_1, graph_layout1,
                               ax=axes[0])
        nx.draw_networkx(Graph_1, graph_layout1, nodelist= end_nodes_1, node_color= 'r', ax = axes[0])
        axes[0].set_title(title1)

        nx.draw_networkx_nodes(Graph_2, graph_layout2, ax=axes[1])
        nx.draw_networkx_labels(Graph_2, graph_layout2, edge_labels= labels_2, ax=axes[1])
        nx.draw_networkx_edges(Graph_2, graph_layout2,
                               ax=axes[1])
        nx.draw_networkx(Graph_2, graph_layout2, nodelist= end_nodes_2, node_color= 'r', ax = axes[1])
        axes[1].set_title(title2)
       
        nx.draw_networkx_nodes(Graph_3, graph_layout3, ax=axes[2])
        nx.draw_networkx_labels(Graph_3, graph_layout3, edge_labels= labels_3, ax=axes[2])
        nx.draw_networkx_edges(Graph_3, graph_layout3,
                               ax=axes[2])
        nx.draw_networkx(Graph_3, graph_layout3, nodelist= end_nodes_3, node_color= 'r', ax = axes[2])
        axes[2].set_title(title3)
        plt.show()



    def passarprastring(self, dataset):

        graph = defaultdict(dict)
        values = list()
        keys = list(dataset.keys())

        
        for i in keys:
            keys2 = list(dataset[i].keys())

            for j in keys2:

                graph[str(i)][str(j)] = dataset[i][j]
                graph[str(j)][str(i)] = dataset[i][j]

        return dict(graph)        