from GA import GA


def read_file(filepath):
    net = {}
    f = open(filepath, "r")
    nr = int(f.readline())
    net['noNodes'] = nr
    mat = []
    for i in range(0, nr):
        mat.append([])
    i = 0
    line = f.readline()
    while line and i<nr:
        args = line.split(",")
        for arg in args:
            mat[i].append(int(arg))
        i = i + 1
        line = f.readline()
    f.close()
    net['mat'] = mat
    return net

def fitnessFct(net, path):
    val = 0
    mat = net['mat']
    for i in range(0, len(path) - 1):
        node = path[i]
        nextNode = path[i+1]
        val = val + mat[node-1][nextNode-1]
    val = val + mat[path[len(path)-1]-1][path[0]-1]
    return val

def main():
    net = read_file("Exemplul3.txt")

    gaParam = {'popSize':10, 'noGen' : 1000, 'pc' : 0.8, 'pm' : 0.1}
    problParam = {'net': net, 'function': fitnessFct, 'noNodes':net['noNodes']}

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    #for i in range(1, gaParam['noGen']):
    ga.oneGenerationElitism()
    final = ga.bestChromosome()
    print(final)

main()
