import streamlit as st
from collections import deque
from usstates import usa_map
from bfs import bfs_path

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
           
        else:
            st.error("No Path Found Between These States")


