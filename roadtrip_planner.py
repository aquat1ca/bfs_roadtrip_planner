import streamlit as st
from collections import deque
from usstates import usa_map
from bfs import bfs_path
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph_with_path(graph_dict, path):
    G = nx.Graph(graph_dict)

    # layout for nodes
    pos = nx.spring_layout(G, seed=7)

    plt.figure(figsize=(10, 7))
    # draw all edges
    nx.draw_networkx_edges(G, pos, edge_color="lightgray", width=1)

    # draw all nodes
    nx.draw_networkx_nodes(G, pos, node_size=400, node_color="#E8F0FE", edgecolors="#1A73E8", linewidths=1)
    nx.draw_networkx_labels(G, pos, font_size=8)

    # highlight the path if it exists
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)
        # start and end pop
        nx.draw_networkx_nodes(G, pos, nodelist=[path[0]], node_color="#34A853", node_size=500)
        nx.draw_networkx_nodes(G, pos, nodelist=[path[-1]], node_color="#EA4335", node_size=500)

    st.pyplot(plt.gcf())
    plt.close()

st.title("Road Trip Planner")
st.write("Finds the shortest route for your road trip!")
states = sorted(list(usa_map.keys()))
start_state = st.selectbox("Start State", states)
states = sorted(list(usa_map.keys()))
end_state = st.selectbox("End State", states)
if st.button("Find Shortest Route"):
    st.write("Select your starting state and destination state")

    if start_state == end_state:
        st.warning("Your Start and End State Are The Same")
    else:
        path = bfs_path(usa_map, start_state, end_state)
        if path:
            st.success("Shortest Path Found!")
            st.write("Route:")
            st.write(" ➜ ".join(path))
            draw_graph_with_path(usa_map, path)
        else:
            st.error("No Path Found Between These States")


