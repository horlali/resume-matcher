from operator import index

import pandas as pd

import Similar

# Reading the CSV files prepared by the fileReader.py
Resumes = pd.read_csv("Resume_Data.csv")
Jobs = pd.read_csv("Job_Data.csv")


def calculate_scores(resumes, job_description):
    scores = []
    tempScore = ""
    for x in range(resumes.shape[0]):
        for y in range(job_description.shape[0]):
            score = Similar.match(resumes["TF_Based"][x], job_description["TF_Based"][y])
            tempScore = tempScore + ", " + str(score)
        scores.append(tempScore)
    return scores


Resumes["Scores"] = calculate_scores(Resumes, Jobs)

Ranked_resumes = Resumes.sort_values(by=["Scores"], ascending=False).reset_index(
    drop=True
)

Ranked_resumes["Rank"] = pd.DataFrame(
    [i for i in range(1, len(Ranked_resumes["Scores"]) + 1)]
)


# print(Resumes['Scores'])


#####
# user --> job name ---> score
