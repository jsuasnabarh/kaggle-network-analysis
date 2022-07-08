'''
Validate.py
Autor: Joshua Suasnabar
Fecha: Jun 2022
'''

import pandas as pd
import numpy as np
import networkx as nx
from pyvis import network as net

class Network():
    '''
    Clase para invocar funciones personalizadas para manipular redes
    '''

    def get_top_nodes(cdict, num=5, reverseBool=True):
        top_nodes ={}
        for i in range(num):
            top_nodes =dict(sorted(cdict.items(), key=lambda x: x[1], reverse=reverseBool)[:num])
            return top_nodes


    def get_subgraph_from_with_neighbors(G=None,centro=None):
        #Agregamos primero el nodo central y sus vecinos
        predecessors = list(G.predecessors(centro))
        successors = list(G.successors(centro))
        mantener = predecessors + successors  + [centro]
        G1 = G.subgraph(mantener)
        return G1

    def get_subgraph_from_node_attr(G=None,tipo='>',attr= 'degree',corte=10):
        corte = float(corte)
        print(corte)
        dict_atr = nx.get_node_attributes(G, attr)
        dict_atr.items()
        if tipo == ">":
            to_keep = [ed for (ed, attr) in dict_atr.items() if attr>corte]
        elif tipo == "<":
            to_keep = [ed for (ed, attr) in dict_atr.items() if attr<corte]
        elif tipo == "=":
            to_keep = [ed for (ed, attr) in dict_atr.items() if attr==corte]   
        SG = G.subgraph(to_keep)
        return SG

    def get_subgraph_from_edge_attr(G=None,tipo='>',attr= 'degree',corte=10):
        #Aplicamos la regla del filtro (sin tocar al nodo principal y sus vecinos)
        if tipo == ">":
            G2 = nx.DiGraph(((_source, _target, _attr) for _source, _target, _attr in G.edges(data=True) if _attr[attr] > corte ))
        elif tipo == "<":
            G2 = nx.DiGraph(((_source, _target, _attr) for _source, _target, _attr in G.edges(data=True) if _attr[attr] < corte))
        elif tipo == "=":
            G2 = nx.DiGraph(((_source, _target, _attr) for _source, _target, _attr in G.edges(data=True) if _attr[attr] == corte))
        #Copiamos los atributos del grafo anterior al subgrafo
        list_attr = []
        for n in G2.nodes():
            attr_G = G.node[n]
            list_attr.append((n,attr_G))
        dict_G2_atr = dict(list_attr)
        nx.set_node_attributes(G2, dict_G2_atr)

        return G2

    def draw_graph3(networkx_graph,notebook=True,show_buttons=True,only_physics_buttons=False,
                    height=None,width=None,bgcolor=None,directed=False,font_color=None,pyvis_options=None,peso='peso',output_filename='graph.html'):
        # make a pyvis network
        network_class_parameters = {"notebook": notebook, "height": height, "width": width, "bgcolor": bgcolor, "font_color": font_color,"directed":directed}
        pyvis_graph = net.Network(**{parameter_name: parameter_value for parameter_name, parameter_value in network_class_parameters.items() if parameter_value})
        pyvis_graph.force_atlas_2based()

        # for each node and its attributes in the networkx graph
        for node,node_attrs in networkx_graph.nodes(data=True):
            pyvis_graph.add_node(node,**node_attrs)

        # for each edge and its attributes in the networkx graph
        for source,target,edge_attrs in networkx_graph.edges(data=True):
            # if value/width not specified directly, and weight is specified, set 'value' to 'weight'
            if peso in edge_attrs:
                # place at key 'value' the weight of the edge
                edge_attrs['value']=edge_attrs[peso]
            # add the edge
            pyvis_graph.add_edge(source,target,color='gray',**edge_attrs)

        # pyvis-specific options
        if pyvis_options:
            pyvis_graph.set_options(pyvis_options)
        pyvis_graph.show_buttons(filter_=['physics'])
        # return and also save
        return pyvis_graph.show(output_filename)