def lookup(metric, cluster):
    metric_destinations = map(lambda m: "%s:%s" % (m[0], m[2]),
                              cluster.getDestinations(metric))
    return metric_destinations
