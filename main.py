import time

from pyspark.sql import SparkSession
from exo1 import get_top10_repos
from exo2 import get_top_contributor
from exo3 import get_biggest_contributors_since_4_years_ago
from exo4 import get_top_10_words


def main():
    dataset_file = "full.csv"
    word_stop_file = "wordStop.txt"

    spark = SparkSession \
        .builder \
        .appName("GitHubCommitAnalytics") \
        .master("local[*]") \
        .getOrCreate()

    spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

    data = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(dataset_file, format="csv")

    get_top10_repos(data)
    get_top_contributor(data, "apache/spark")
    get_biggest_contributors_since_4_years_ago(data, "apache/spark")
    get_top_10_words(data, word_stop_file)

    time.sleep(1000)

if __name__ == "__main__":
    main()
