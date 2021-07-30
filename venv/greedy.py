def FindBestStation(states_needed, stations):

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


if __name__ == '__main__':

    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    stations = {}
    stations['one'] = set (['id', 'nv', 'ut'])
    stations['two'] = set (['wa', 'id', 'mt'])
    stations['three'] = set (['or', 'nv', 'ca'])
    stations['four'] = set (['nv', 'ut'])
    stations['five'] = set (['ca', 'az'])

    print(FindBestStation ( states_needed , stations ))


