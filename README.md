![Quality Air (1)](https://user-images.githubusercontent.com/97995925/218177524-6e2dc175-4e3b-4d0c-9dd8-f4038d2adaff.png)

# Quality Air Quality Cities

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

## Project Purpose

### Installing

Clone the repository (https://help.github.com/articles/cloning-a-repository/)

```bash
git clone https://github.com/RTGS-Lab/QualityAirQualityCities
```
Inside of your project folder (after clone):

Note: the secrets file is in the .gitignore and should never be uploaded to GitHub

## Development Workflow

An issue will be assigned to you via GitHub. Your workflow begins after assignment:
1. Create a branch based on the `dev` branch with your initials and the issue number as the branch name (e.g. EB-5): `git checkout -b EB-5`
3. Work on the issue.
     1. In the "Projects" section on the sidebar of the issue page, under "StreamStats Ecoystem", change the "Status" to "In Progress".
     2. While you work, you may wish to have the app running live with live reload: `npm start`
     3. Add your changes: `git add .`
     4. Check that your files were added as expected: `git status`
     5. Frequently commit your work to your local branch. Use simple, short, and descriptive messages with a verb describing the work. Include the issue number. Example: `git commit -m "#5 added styling"`
4. Update the CHANGELOG.md to describe your work.
5. Ensure your code is synced with the latest version of the `dev` branch: 
     1. Use this command: `git pull origin dev`
     2. If there are no merge conflicts, the updates made to the `dev` branch will be incorporated into your local branch automatically.
     3. If there are merge conflicts, you will need to resolve conflicts manually. Please be careful with this step so that no code is lost. Once complete, you will need to add your changes: `git add .` and then commit again: `git commit -m "add message here"`
6. Push your committed and synced branch to the remote repository on GitHub: `git push origin JEB-5`
7. Submit a Pull Request:
     1. Request that your branch be merged into the `main` branch.
     2. Name the Pull Request in this format: "Fixes #5 - Issue Description". 
     3. Use [keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests) to automatically close issues (e.g. "Closes #5).
     4. Assign a reviewer (typically the lead developer).
8. Once your Pull Request is reviewed, address any feedback that needs to be addressed. Once you have addressed feedback, click the button to re-request review.
9. Upon approval of the Pull Request, your issue will be merged into the `dev` branch and you can start on a new issue.

## More Git help
Check [this](https://ohshitgit.com/) out if your having a git of a problem... [This is](https://education.github.com/git-cheat-sheet-education.pdf) a more basic cheatsheet.

## Infrastructure and Deployment

## Authors
* **[Bryan Runck](https://cla.umn.edu/about/directory/profile/runck014)**  - *Project Advisor* - Senior Research Scientist (R7), [GEMS Informatics Center](https://gems.umn.edu/gems-team)
* **[Jake Ford](https://cla.umn.edu/mgis/people/graduate-students)**  - *Developer* - University of Minnesota - [Geographic Information Science Program](https://cla.umn.edu/mgis/mgis-program) - Extentsion of Quality Air / Quality Cities
* **[Rob Hendrickson](https://cla.umn.edu/mgis/people/graduate-students)**   - *Developer* - University of Minnesota - [Geographic Information Science Program](https://cla.umn.edu/mgis/mgis-program) - Extentsion of Quality Air / Quality Cities
* **[Lauren Roach](https://cla.umn.edu/mgis/people/graduate-students)**   - *Developer* - University of Minnesota - [Geographic Information Science Program](https://cla.umn.edu/mgis/mgis-program) - Extentsion of Quality Air / Quality Cities
* **[Taylor Andersen-Beaver](https://cla.umn.edu/mgis/people/graduate-students)**   - *Developer* - University of Minnesota - [Geographic Information Science Program](https://cla.umn.edu/mgis/mgis-program) - Extentsion of Quality Air / Quality Cities
* **[Ethan Bott](https://cla.umn.edu/mgis/people/graduate-students)**  - *Developer* - University of Minnesota - [Geographic Information Science Program](https://cla.umn.edu/mgis/mgis-program) - Extentsion of Quality Air / Quality Cities
