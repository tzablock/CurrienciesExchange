from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from utils.DataParsing import getInputCsv,saveCsv

if __name__ == '__main__':
    spark = SparkSession.builder.appName("CalcBorderValues").master("local").getOrCreate()
    fxRates = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/FXCM-H1.csv")

    fxRates = fxRates.withColumn("open_to_close_bid_diff",F.abs(fxRates.openbid-fxRates.closebid))
    fxRates = fxRates.withColumn("open_to_close_ask_diff",F.abs(fxRates.openask-fxRates.closeask))

    maxBordersDF = fxRates.groupBy("symbol")\
                        .agg(F.max("openbid").alias("max_open_bid"),
                             F.max("closebid").alias("max_close_bid"),
                             F.max("openask").alias("max_open_ask"),
                             F.max("closeask").alias("max_close_ask"),
                             F.min("openbid").alias("min_open_bid"),
                             F.min("closebid").alias("min_close_bid"),
                             F.min("openask").alias("min_open_ask"),
                             F.min("closeask").alias("min_close_ask"),
                             F.max("open_to_close_bid_diff").alias("max_open_to_close_bid_diff"),
                             F.max("open_to_close_ask_diff").alias("max_open_to_close_ask_diff"))

    symToNameDF = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/fullCurrenciesName.csv").withColumnRenamed("SYMBOL","symbol")
    maxBordersDF = maxBordersDF.join(symToNameDF,"symbol","left_outer").drop("symbol").withColumnRenamed("CURRENCY_PAIR","currency_pair")
    maxBordersDF = maxBordersDF.select("currency_pair","max_open_bid","min_close_bid","max_open_to_close_bid_diff","max_open_ask","min_close_ask","max_open_to_close_ask_diff","max_close_bid","max_close_ask","min_open_bid","min_open_ask")

    maxBordersDF.show()
    #saveCsv(maxBordersDF, "/home/tzablock/IdeaProjects/Currencies/resources/maxVals")