# financeproject-retail-analysis
PySpark project

Adding a financial based pyspark project.

Adding content from local.

When changes are made (unstaged) -> stage (Ready to be committed) -> commit

# Set a origin
git remote add origin <remote_url>

# Adding upstream tag
git push -u origin main

going forward use "git push" alone.

# Branch creation

git branch ( To check which branch )

git branch -M main ( To rename the branch name )

git branch feature1 ( To create a branch )

git checkout feature1 ( To switch to feature1 branch )

git checkout -b feature2 ( To create and switch to feature2 branch )

git checkout -b feature2 feature1 ( To create feature2 branch and get the code base from feature1)

# Delete Branch

git branch -d <branch_name>

# Feature

# Remove the unstaged change

git restore <file_name>

# Remove the staged change

git restore --staged <file_name>

# Remove the committed change

git log (To show all the commits and shows the most recent change at the top)

git reset <hash_value>

## to go just one step down, the one step before

git reset head~1


# Stash

- To place the content in the parking area
git stash

- To retrive the content from the parking area
git stash pop

- To clear the stash area
git stash clear

Remove this line.
