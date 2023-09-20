$commit_message = Read-Host "Enter your commit message: "
git add . 
git commit -m $commit_message 
git push origin master