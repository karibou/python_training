from __future__ import division

def read_data(filename):
    datafile = open(filename)
    timesteps = []
    pressures = []
    temperatures = []
    for line in datafile:
        if not line.strip():
            continue
        if line.startswith('Time step:'):
            dummy, timestep = line.split(':')
            timesteps.append(float(timestep))
            pressure = {}
            temperature = {}
            pressures.append(pressure)
            temperatures.append(temperature)
        else:
            x, y, z, p, t = line.split()
            coords = (int(x), int(y), int(z))
            pressure[coords] = float(p)
            temperature[coords] = float(t)
            

    datafile.close()
    return timesteps, pressures, temperatures

def compute_space_avg(data):
    """data is a dictionary of (coords): value"""
    values = data.values()
    return sum(values)/len(values)


def compute_time_avg(datalist):
    """data is a list of dictionaries (coords):value
    function returns a dictionary of (coords): avg_value"""
    result = {}
    for coords in datalist[0].keys():
        values = []
        for data in datalist:
            values.append(data[coords])
        avg = sum(values)/len(values)
        result[coords] = avg
    return result
    

def run(filename):
    timesteps, pressures, temperatures = read_data(filename)

    # compute space averages and write to a result file
    avg_p = [compute_space_avg(p) for p in pressures]
    avg_t = [compute_space_avg(t) for t in temperatures]

    resultfile = open(filename.replace('_raw_data.dat', '_space_avg.dat'), 'w')
    for time, press, temp in zip(timesteps, avg_p, avg_t):
        resultfile.write("Time step: %f pressure: %e temperature %e\n" % (time, press, temp))
    resultfile.close()

    # compute time averages and write to a result file
    time_avg_p = compute_time_avg(pressures)
    time_avg_t = compute_time_avg(temperatures)
    coords = time_avg_p.keys()
    coords.sort()
    resultfile = open(filename.replace('_raw_data.dat', '_time_avg.dat'), 'w')
    for x,y,z in coords:
        resultfile.write("%d %d %d %e %e\n" % (x,y,z,
                                               time_avg_p[(x,y,z)],
                                               time_avg_t[(x,y,z)]))
    resultfile.close()

if __name__ == '__main__':
    import sys
    run(sys.argv[1])



    
