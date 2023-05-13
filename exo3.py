from datetime import datetime, timedelta
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date


def get_biggest_contributors_since_4_years_ago(data, repo_name):
    spark_commits = data.filter(col("repo") == repo_name) \
        .withColumn("date", to_date(col("date"), "EEE MMM dd HH:mm:ss yyyy Z"))

    today = datetime.now()
    date_4_years_ago = today - timedelta(days=365 * 4)

    commits_last_4_years = spark_commits.filter(col("date").between(date_4_years_ago, today))

    author_counts = commits_last_4_years \
        .groupBy("author") \
        .count() \
        .sort("count", ascending=False)

    author_counts.show()

    return author_counts
