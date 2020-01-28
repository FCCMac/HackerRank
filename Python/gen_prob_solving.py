import math

def reduceCapacity(model):
    gens_to_shutoff = math.ceil(len(model) / 2)
    
    # create dict for values and counts of models
    model_counts = []
    model.sort()
    j = 0
    for i in range(len(model)):
        if i == 0:
            model_counts.append([model[i], 1])
        elif model[i] == model_counts[j][0]:
            model_counts[j][1] += 1
        else:
            model_counts.append([model[i], 1])
            j += 1

    def sortSecond(val):
        return val[1]
    
    model_counts.sort(key = sortSecond, reverse = True)

    print(model_counts)

    i = 0
    total_gens_off = 0
    for gen_count in model_counts:
        
        total_gens_off += gen_count[1]

        if total_gens_off >= gens_to_shutoff:
            break

        i += 1

    print(i)

reduceCapacity([7,10,1,2,7,7,1])