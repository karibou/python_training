"""
"""
import numpy as np

# filename = "introduction_volume_experiment_raw_data.dat"


def read_data(filename):
    """
    """
    timesteps = []
    measures = []
    ## the following should be enclosed in a try... finally
    f = open(filename)
    for line in f:
        if line.startswith("Time step"):
            v = line.split()[-1]
            timesteps.append(float(v))
        else:
            data = [float(element) for element in line.split()]
            data.insert(0, float(v)) ## add time as first column
            measures.append(data)
    f.close()

    data = (np.array(measures))
    dimt = len(timesteps)
    dimx = len(np.unique(data[:,1]))
    dimy = len(np.unique(data[:,2]))
    dimz = len(np.unique(data[:,3]))
    dimPT = 2
    dataPT = data[:,4:]
    measures = np.reshape(dataPT, (dimt, dimx, dimy, dimz, dimPT))
    return timesteps, measures


def read_data1(filename):
    """
    """
    datafile = open(filename)
    timesteps = []
    measures = []
    for line in datafile:
        if not line.strip():
            continue
        if line.startswith('Time step:'):
            dummy, timestep = line.split(':')
            timesteps.append(float(timestep))
        else:
            x, y, z, p, t = line.split()
            measures.append(float(p))
            measures.append(float(t))
            
    nb_x, nb_y, nb_z = int(x), int(y), int(z)
    measures = np.reshape(measures, (len(timesteps), nb_x+1, nb_y+1, nb_z+1, 2))
    datafile.close()
    return timesteps, measures


def read_data2(filename):
    """this version supposes we know the size of the data in advance"""
    datafile = open(filename)
    timesteps = []
    measures = np.empty((10, 10, 10, 10, 2), np.float)
    for line in datafile:
        if not line.strip():
            continue
        if line.startswith('Time step:'):
            dummy, timestep = line.split(':')
            time = len(timesteps) 
            timesteps.append(float(timestep))
        else:
            x, y, z, p, t = line.split()
            x, y, z = int(x), int(y), int(z)
            measures[time, x, y, z, 0] = float(p)
            measures[time, x, y, z, 1] = float(t)
    datafile.close()
    return timesteps, measures


def compute_space_avg(measures):
    """measures is an array of shape (time, x, y,z, mes)
    return an array of shape (time, mes)"""
    # this groups the X,Y,Z axis on a single axis
    # tmp has 3 axis: time, space, measures
    tmp = measures.reshape(measures.shape[0], -1, measures.shape[-1])
    # average tmp on axis 1, i.e. space
    return tmp.mean(1)


def compute_time_avg(measures):
    """
    """
    return measures.mean(0)
    

def run(filename):
    timesteps, measures = read_data(filename)

    # compute space averages and write to a result file
    space_avg =  compute_space_avg(measures)

    resultfile = open(filename.replace('_raw_data.dat', '_space_avg_numpy.dat'), 'w')
    for time, (press, temp) in zip(timesteps, space_avg):
        resultfile.write("Time step: %f pressure: %e temperature %e\n" % (time, press, temp))
    resultfile.close()

    # compute time averages and write to a result file
    time_avg = compute_time_avg(measures)
    
    max_x, max_y, max_z, nb_mes = time_avg.shape
    resultfile = open(filename.replace('_raw_data.dat', '_time_avg_numpy.dat'), 'w')
    for x in range(max_x):
        for y in range(max_y):
            for z in range(max_z):
                resultfile.write("%d %d %d %e %e\n" % (x, y, z,
                                                       time_avg[x, y, z, 0],
                                                       time_avg[x, y, z, 1]))
    resultfile.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "Expecting a file name for data file"
        sys.exit(1)
    
    run(sys.argv[1])
    sys.exit(0)
