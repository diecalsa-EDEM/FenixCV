# feniX - Computer Vision

## Guide how to use github

### 1. Clone github repository

0. Check if git is installed on computer: `git --version`.
1. Open a terminal (maxOS) / command line prompt.
2. Go to the directory where we want to allocate the repository.
3. Insert following lines: `git clone https://github.com/diecalsa-EDEM/FenixCV.git`.

If there's no error, now you have cloned the repository to your local directory.

### 2. Create a new branch to work on

If you are going to work on a new feature, you have to create a new branch in order to make changes in a safe way.

0. Open a terminal and go to the repository's directory (local): i.e. `cd Desktop/EDEM_DIEGO/02_CURSO/00_REPOSITORIOS/FenixCV/`
1. First fetch the remote branches: `git fetch origin`.
2. Create the new branch: `git checkout -b <branch_name>`
3. Push your branch to the remote directory: `git push -u origin <branch_name>`.

By doing that way we are creating a new branch where we are going to develop a new feature in a safe way and we are sharing it with other collaborators.

### 3. Working on a new feature

Once we have created the new branch, we can start working on the new feature.

0. Open a terminal and go to the repository's directory (local): i.e. `cd Desktop/EDEM_DIEGO/02_CURSO/00_REPOSITORIOS/FenixCV/`
1. Check that we are on the correct branch: `git branch`. All the available branches will appear. The current branch is marked with an `*`. If we are not on the correct branch, then: `git checkout <branch_name>`.
2. Get the last version of the current branch: `git pull`.
3. Now stark making changes on the code.
4. Once you have something to "save", commit the changes: 
    - `git status` will show the changes we have made.
    - `git add .`
    - `git commit -m "<commit comment>"`.
    - `git push`.

### 4. Merging a branch to master

If we are done with the new feature we have created and the new version is stable, it's time to merge the branch with the master branch. This will be done by the github manager.