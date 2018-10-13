def getInputCsv(spark, path):
    return spark.read.option("inferSchema","true")\
                     .option("header","true")\
                     .csv(path)

def saveCsv(ds, path):
    ds.write.csv(path)