from apyori import apriori


def convertResult(input):
    output = []

    output.append("Items:")
    for e in input:
        output.append([list(e.items), e.support])

    output.append("Rules:")
    for e in input:
        for comb in e.ordered_statistics:
            if len(comb.items_base) > 0:
                output.append([list(comb.items_base),"=>", list(comb.items_add), comb.confidence])

    return output


datContent = [i.strip().split() for i in open("./retail.dat").readlines()]

f = open('result.txt', 'w')
results = list(apriori(datContent, min_support=0.3, min_confidence=0.1))
for item in convertResult(results):
    f.write(str(item) + '\n')
