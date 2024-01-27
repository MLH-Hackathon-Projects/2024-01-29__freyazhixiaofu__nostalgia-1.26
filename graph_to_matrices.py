import networkx as nx
import numpy as np


# for graph visualization
import matplotlib.pyplot as plt

import cohere
# nodes examples
# nodes = [(3,"b"), (1,"d"), (1, "a")] # the nodes are derived from the text
# connections = [not ("a","b") or (1, 2), not (1, 2) or (1, "a")] # the logical connectives are derived from the text

def txt_to_matrix(v_text: str):

    co = cohere.Client('e8rlpDvah41xrbej24CPnzZt0KMfQVd5EK16kaO')

    # with open(link, 'r') as file:
    #     contents = file.read()

    # text = contents

    # classify
    # response = co.classify(
    #     model='large',
    #     inputs=text,
    #     examples=[{'text': 'Barack Obama', 'label': 'person or events'},
    #             {'text': 'World War II', 'label': 'person or events'},
    #             {'text': 'stopped a disaster', 'label' : 'outcome'},
    #             {'text': 'works for nothing', 'label' : 'outcome'},
    #             {'text': 'if A, then B', 'label' : 'IMPLIES'}]
    # )

    # ppl_or_events = [] # node variable1
    # outcomes = []   # nod variable2
    # connectives = []

    # for prediction in response.classifications:
    #     if prediction.prediction == "people or events":
    #         ppl_or_events.append(prediction.input)
    #     elif prediction.prediction == "outcome":
    #         outcomes = prediction.input
    #     elif prediction.prediction == "IMPLIES":
    #         connectives.append(prediction.input)

    text = v_text
    prompt = f"Identify all the people and events in the following text: {text}"

    ppl_or_events = co.generate(
        model='large',  # Choose the appropriate model
        prompt=prompt,
        max_tokens=50  # Adjust as necessary
        )

    prompt = f"Identify all what people did and the outcome of the events: {text}"

    outcomes = co.generate(
        model='large',  # Choose the appropriate model
        prompt=prompt,
        max_tokens=50  # Adjust as necessary
        )

    prompt = f"Identify all the logical statements in the form of 'if A, then B': {text}"

    connectives = co.generate(
        model='large',  # Choose the appropriate model
        prompt=prompt,
        max_tokens=50  # Adjust as necessary
        )

    def creat_nodes(ppl_evnts: list, outcomes: list) -> list:
        nodes = []
        for thing in ppl_evnts:
            for outcome in outcomes:
                # to have the
                nodes.append((ppl_evnts.index(thing), chr(96 + outcomes.index(outcome))))
        return nodes

    nodes = creat_nodes(ppl_or_events, outcomes)  # now we get the vertices of the graph

    def creat_graph(nodes: list[tuple], connections: list):  # out put is a matrix
        # Create a graph
        G = nx.Graph()
        for node1 in nodes:
            for node2 in nodes:
                if node1 != node2:
                    if 'if node1 or node2' in connections:  # not sure if the parenthesis should be added
                        G.add_edges_from([node1, node2])

        nx.draw(G, with_labels=True, font_weight='bold')    # Draw the graph
        plt.show()  # Show the plot
        return nx.incidence_matrix(G)  # Convert to incidence matrix

    return creat_graph(nodes, connectives)
