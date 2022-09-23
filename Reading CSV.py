# copied from https://www.cs.cmu.edu/~110/notes/notes-2d-lists.html#csvFiles
import sqlite3


def readFile(path):
    # This makes a very modest attempt to deal with unicode if present
    with open(path, 'rt', encoding='ascii', errors='surrogateescape') as f:
        return f.read()

def readCsvFile(path):
    # Returns a 2d list with the data in the given csv file
    result = [ ]
    for line in readFile(path).splitlines():
        result.append(line.split(','))
    return result

def readSampleCsvFile():
    data = readCsvFile('sample.csv') # download sample.csv first!
    print('Reading sample.csv')
    rows = len(data)
    cols = len(data[0])
    print('In sample.csv, rows =', rows, ' and cols=', cols)
    print('2d list of data:', data)

readSampleCsvFile()