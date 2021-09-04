
#!/bin/bash
DATE=$(date +"%Y-%b-%d")
git init
git rm -r --cached .
git add .
git commit -m "'$DATE'"
git branch -M main
git remote add origin https://github.com/julianwagle/octopod-spork.git
git push -u origin main -f
