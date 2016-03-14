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

def get_centroid(p):
    green_point_min = random.choice(green_points)
    distance_min = distance(p, green_point_min)
    for green_point in green_points:
        if distance(green_point, p) < distance_min:
            green_point_min, distance_min = green_point, distance(green_point, p)
    return green_point_min




# now that you have assigned a centroid to each gold point,
# calculate new centroids by taking the average of the gold points in each centroid

class Cluster:
    def __init__(self, points=None, centroid=None):
        self.points = points
        self.centroid = centroid
    def recompute_centroid(self):
        xs = [point[0] for point in self.points]
        ys = [point[1] for point in self.points]
        avg_x = float(sum(xs))/len(xs)
        avg_y = float(sum(ys))/len(ys)
        return (avg_x, avg_y)



initial_clusters = [Cluster(centroid=green_point) for green_point in green_points]


for gold_point in gold_points:
    centroid = get_centroid(gold_point)
    gold_points_centroids[gold_point] = centroid

print 'done'

pprint.pprint(gold_points_centroids)


