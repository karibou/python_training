import csv
import sys

def load_table(fpath):
    """Read file specified by fpath, return a dict with column names as keys
    and a list of values as values"""
    f = open(fpath)
    # read headers line; split to get a list of column names
    headers = f.readline().split()
    # read the remainder of the file and file the result dictionnary
    result = {}
    for line in f.readlines():
        vals = line.split()
        for h, v in zip(headers, vals):
            if h not in result:
                result[h] = []
            result[h].append(float(v)) # convert string to float
    f.close()
    return result

def load_csv(fpath):
    """Use the csv module to read the file and return the dict"""
    result = {}
    csvfile = open(fpath, 'r')
    dialect = csv.Sniffer().sniff(csvfile.readline())
    csvfile.seek(0)
    reader = csv.DictReader(csvfile, dialect=dialect)
    for data in reader:
        for colname in data:
            if colname in result:
                result[colname].append(float(data[colname]))
            else:
                result[colname] = [float(data[colname])]
    return result

def format_csv_python(data, output_stream):
    output_stream.write('mesures = %r\n' % data)

def format_csv_stats(data, output_stream):
    output_stream.write('\t'.join(['Sensor', 'min', 'max', 'avg']) + '\n')
    for sensor, values in data.iteritems():
        minv = min(values)
        maxv = max(values)
        avgv = float(sum(values)) / len(values)
        output_stream.write('\t'.join([sensor, str(minv), str(maxv), str(avgv)]) + '\n')

def format_csv(data, format='python', output_stream=None):
    if output_stream is None:
        output_stream = sys.stdout
    if format == 'python':
        format_csv_python(data, output_stream)
    elif format == 'stats':
        format_csv_stats(data, output_stream)
    else:
        raise ValueError('unknown format %s' % format)

if __name__ == '__main__':
    filenames = sys.argv[1:]
    if not filenames:
        print "no filename specified"
    for filename in filenames:
        data = load_table(filename)
        print data
        for format in ('python', 'stats'):
            print 'Format:', format
            format_csv(data, format)
