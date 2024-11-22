import pandas
from matplotlib import pyplot

table = pandas.read_csv("/home/cun/PycharmProjects/DrawingDiagram/excel/data.csv", sep=',')
_, axes = pyplot.subplots(1, 4, figsize=(20, 8))
t = table.groupby(['<DATE>']).boxplot(column=["<OPEN>","<HIGH>","<LOW>","<CLOSE>"], ax=axes)
pyplot.savefig('DIAGRAM.png', dpi=300, bbox_inches='tight')
pyplot.show()