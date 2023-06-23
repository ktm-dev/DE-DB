# Databricks notebook source
# MAGIC %run ../../Includes/_common

# COMMAND ----------

# MAGIC %scala
# MAGIC lesson_config = LessonConfig(name = None,
# MAGIC                              create_schema = True,
# MAGIC                              create_catalog = False,
# MAGIC                              requires_uc = False,
# MAGIC                              installing_datasets = True,
# MAGIC                              enable_streaming_support = False)
# MAGIC
# MAGIC DA = DBAcademyHelper(course_config=course_config,
# MAGIC                      lesson_config=lesson_config)
# MAGIC DA.reset_lesson()
# MAGIC DA.init()
# MAGIC DA.conclude_setup()

# COMMAND ----------

# TODO
my_name = None

# COMMAND ----------

example_df = spark.range(16)
