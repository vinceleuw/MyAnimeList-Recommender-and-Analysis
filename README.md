#  CSE 163 Project: Anime and the People

## Instructions

* To run this project, first begin by downloading the required data sets [here](https://drive.google.com/drive/folders/1UhinqGrH2XytkpiD7LlLzMcn7MY2I_gt). These datasets are scraped off of MyAnimeList's database and are provided by [Hernan4444](https://github.com/Hernan4444/MyAnimeList-Database) on GitHub. Download the **anime.csv** and **rating_complete.csv** files and movee them to the same folder as the project, or change the paths as needed.
* The modules and libraries that are required to run these files are Pandas, Numpy, Matplotlib, defaultdict from collections, csr_matrix from scipy.sparse, and NearestNeighbors from sklearn.neighbors.
* The project should now be able to be run from main.py. Run the program and wait. Pictures of the charts will be made and saved in the directory. You should also eventually be asked to input an anime. Input the [main name](instructions.jpg) used on the anime's MyAnimeList page and hit enter. The program will output a list of recommended shows in the terminal.
* The recommender object also allows for you to change the amount of rows of the user rating dataset that will be used in the recommender, in case your pc is not able to handle the entire dataset (over 50,000,000 rows).
* The recommend function also allows for another parameter that lets you change the number of recommendations outputted.