# The small Kids repeated question
"""
The small kids keeps asking the questions repeatedly until we say "just because"

"""

from random import choice

questions = ["why the sky is blue?: ","why there a face on the moon?:","Where are all the dinosaurs?:"]

question = choice (questions)

answer = input(question).strip().lower()

while answer != "just because":

    answer = input("why?: ").strip().lower()

print("oh....Ok.")
