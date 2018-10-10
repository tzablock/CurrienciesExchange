from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from DataParsing import getInputCsv,saveCsv

if __name__ == '__main__':
    spark = SparkSession.builder.appName("CalcBorderValues").master("local").getOrCreate()
    fxRates = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/FXCM-H1.csv")
    maxBorders = fxRates.groupBy("symbol")\
                        .agg(F.max("openbid").alias("maxopenbid"),
                             F.max("closebid").alias("maxclosebid"),
                             F.max("openask").alias("maxopenask"),
                             F.max("closeask").alias("maxcloseask"))
    saveCsv(maxBorders,"/home/tzablock/IdeaProjects/Currencies/resources/maxVals")