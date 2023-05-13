from pyspark.sql.functions import col


def get_top10_repos(data):
    filtered_data = data.filter(col("repo").isNotNull())

    top10Repo = filtered_data \
        .groupBy("repo") \
        .count() \
        .sort("count", ascending=False) \
        .limit(10)

    top10Repo.show()

    return top10Repo
