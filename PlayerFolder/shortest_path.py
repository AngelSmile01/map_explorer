import json
import sys
from collections import defaultdict
import os


class Point:
    def __init__(self, start_point, end_point, coordinates, orientation):
        self.start_point = start_point
        self.end_point = end_point
        self.coordinates = coordinates
        self.orientation = orientation


def create_points_from_input(input_data):
    points = []
    for point_data in input_data:
        point = Point(
            point_data["start_point"],
            point_data["end_point"],
            point_data["coordinates"],
            point_data["orientation"],
        )
        points.append(point)
    return points


# Creating a dictionary to hold the graph
graph = defaultdict(list)


def load_all_json_files(directory="."):
    """
    This function loads all the json files from the given directory
    and constructs a graph.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            coordinate = filename.rstrip(".json")
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                data = json.load(file)
                for link in data["links"]:
                    # Avoid adding unnecessary links between "to_x_y" nodes
                    if not (
                        link["start_point"].startswith("to_")
                        and link["end_point"].startswith("to_")
                    ):
                        graph[link["start_point"]].append(link["end_point"])
                        if link["orientation"] == "bidirectional":
                            graph[link["end_point"]].append(link["start_point"])

                # Verify the existence of corresponding JSON files and adjust links
                for point in data["points"].keys():
                    if point.startswith("to_"):
                        new_coordinate = point.split("to_")[1]
                        reciprocal_point = f"to_{coordinate}"
                        reciprocal_filepath = os.path.join(
                            directory, f"{new_coordinate}.json"
                        )

                        # Only add the points if the corresponding file exists
                        if os.path.exists(reciprocal_filepath):
                            graph[point].append(reciprocal_point)
                            graph[reciprocal_point].append(point)


def find_shortest_path(start, end, path=[]):
    """
    This function finds the shortest path between two points in a graph.
    """
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def optimize_teleport_points(path):
    """
    This function optimizes the path by keeping only the first "to_" if two "to_" follow each other.
    """
    new_path = []
    skip_next = False
    for i, point in enumerate(path):
        if skip_next:
            skip_next = False
            continue
        if (
            i < len(path) - 1
            and point.startswith("to_")
            and path[i + 1].startswith("to_")
        ):
            new_path.append(point)
            skip_next = True
        else:
            new_path.append(point)
    return new_path


# Load all JSON files and construct the graph
load_all_json_files(directory="coordinates")
