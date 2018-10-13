from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from DataParsing import getInputCsv,saveCsv

if __name__ == '__main__':
    spark = SparkSession.builder.appName("CalcBorderValues").master("local").getOrCreate()
    fxRates = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/FXCM-H1.csv")
    fxRates = fxRates.withColumn("open_to_close_diff",F.abs(fxRates.openbid-fxRates.closebid))
    maxBordersDF = fxRates.groupBy("symbol")\
                        .agg(F.max("openbid").alias("max_open_bid"),
                             F.max("closebid").alias("max_close_bid"),
                             F.max("openask").alias("max_open_ask"),
                             F.max("closeask").alias("max_close_ask"),
                             F.min("openbid").alias("min_open_bid"),
                             F.min("closebid").alias("min_close_bid"),
                             F.min("openask").alias("min_open_ask"),
                             F.min("closeask").alias("min_close_ask"),
                             F.max("open_to_close_diff").alias("open_to_close_diff"))

    symToNameDF = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/fullCurrenciesName.csv").withColumnRenamed("SYMBOL","symbol")
    maxBordersDF = maxBordersDF.join(symToNameDF,"symbol","left_outer").drop("symbol")

    maxBordersDF.show()
    saveCsv(maxBordersDF, "/home/tzablock/IdeaProjects/Currencies/resources/maxVals")