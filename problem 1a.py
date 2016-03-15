import random
import pprint

green_points = [(25,125),
                (44,105),
                (29,97),
                (35,63),
                (55,63),
                (42,57),
                (23,40),
                (64,37),
                (33,22),
                (55,20)]

gold_points = [(28,145),
               (65,140),
               (50,130),
               (38,115),
               (55,118),
               (50,90),
               (43,83),
               (63,88),
               (50,60),
               (50,30)]

def distance(p1, p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return ((p1_x - p2_x)**2 + (p1_y - p2_y)**2 )**.5

gold_points_centroids = {}

def find_nearest_cluster(p, clusters):
    cluster_min = random.choice(clusters)
    distance_min = distance(p, cluster_min.centroid)
    for cluster in clusters:
        if distance(cluster.centroid, p) < distance_min:
            cluster_min, distance_min = cluster, distance(cluster.centroid, p)
    return cluster_min




# now that you have assigned a centroid to each gold point,
# calculate new centroids by taking the average of the gold points in each centroid

class Cluster:
    def __init__(self, points=None):
        if points == None:
            self.points = None
        elif type(points) != type([]):
            self.points = [points]
        else:
            self.points = points
        self.centroid = self.compute_centroid()
    def compute_centroid(self):
        if self.points is None:
            return None
        xs = [point[0] for point in self.points]
        ys = [point[1] for point in self.points]
        avg_x = float(sum(xs))/len(xs)
        avg_y = float(sum(ys))/len(ys)
        return (avg_x, avg_y)
    def __repr__(self):
        return 'Points :' + str(self.points) + '; Centroid: ' + str(self.centroid)


initial_clusters = [Cluster(points=green_point) for green_point in green_points]


for gold_point in gold_points:
    cluster = find_nearest_cluster(gold_point, initial_clusters)
    cluster.points += [gold_point]
    gold_points_centroids[gold_point] = cluster

print 'done'

pprint.pprint(gold_points_centroids)


