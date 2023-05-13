from pyspark.sql.functions import split, explode, lower, col


def get_top_10_words(data, stopwords_file):
    with open(stopwords_file, "r") as f:
        stopwords = [line.strip() for line in f]

    split_messages = data.select(explode(split(lower(col("message")), " ")).alias("word"))

    filtered_words = split_messages.filter(~col("word").isin(stopwords) & (col("word") != ""))

    top10_words = filtered_words.groupBy("word") \
        .count() \
        .sort("count", ascending=False) \
        .limit(10)

    top10_words.show()

    return top10_words
