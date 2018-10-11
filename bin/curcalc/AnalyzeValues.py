from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from DataParsing import getInputCsv,saveCsv

if __name__ == '__main__':
    spark = SparkSession.builder.appName("CalcBorderValues").master("local").getOrCreate()
    fxRates = getInputCsv(spark,"/home/tzablock/IdeaProjects/Currencies/resources/FXCM-H1.csv")
    fxRates = fxRates.withColumn("open_to_close_deff",F.abs(fxRates.openbid-fxRates.closebid))
    maxBorders = fxRates.groupBy("symbol")\
                        .agg(F.max("openbid").alias("max_open_bid"),
                             F.max("closebid").alias("max_close_bid"),
                             F.max("openask").alias("max_open_ask"),
                             F.max("closeask").alias("max_close_ask"),
                             F.min("openbid").alias("min_open_bid"),
                             F.min("closebid").alias("min_close_bid"),
                             F.min("openask").alias("min_open_ask"),
                             F.min("closeask").alias("min_close_ask"),
                             F.max("open_to_close_deff").alias("open_to_close_deff"))
    maxBorders.show()
    saveCsv(maxBorders,"/home/tzablock/IdeaProjects/Currencies/resources/maxVals")