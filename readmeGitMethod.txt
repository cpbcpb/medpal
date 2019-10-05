Hi Team!  
THE PLAN IS WE WILL ALL: 

git clone <the-link-to-this-repo>
cd into medpal
git checkout -b develop
git pull origin develop

THAT SHOULD CREATE A LOCAL MODEL OF THE REMOTE DEVELOP BRANCH
THEN TO CREATE YOUR BRANCH:

git checkout -b <newBranchName> 

NOW YOU MAKE YOUR CHANGES AND GIT ADD AND COMMIT
THEN WHEN DOING A PULL REQUEST FIRST:

git add .
git commit -m <yourMessageWithQuotesAroundIt>
git push origin <yourName>

THEN ON GITHUB: 
click "Create New Pull Request"
The base should be "develop"
The compare should be your name

TADA! Youre done!
Then we can do pull requests back to develop
when we want a code review.
