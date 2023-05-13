from pyspark.sql.functions import col


def get_top_contributor(data, repo_name):
    top_contributor = data.where(col("repo") == repo_name) \
        .groupBy("author") \
        .count() \
        .sort("count", ascending=False) \
        .limit(1)

    top_contributor.show()

    return top_contributor
