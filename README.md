
## How to Contribute to this Repo's DATA:
We  populate a google sheet. Some folks web-scrape and  some manually enter the data. Reach out [via email](https://bit.ly/3aSlS9K) to get involved!

## How to Contribute to this Repo's CODE:  
***Use feature-branch workflow***  

![master-->feature-branch-->master](https://github.com/john-telfeyan/multi_media/blob/master/feature_branch_diagram.png?raw=true)  

Clone the Repo:
```bash
git clone git@github.com:john-telfeyan/covid19_data.git
```
Then please use feature-branch workflow like so; First:
```bash
git checkout -b <feature-name>-<your-name>
```

Add only the required files and use a descriptive commit message like...
```bash
git add scrapers/get_va_data.py
git commit -m "added a working web scraper for Virginia hospital data."
```
 ...then to push the new feature and I'll review it before merging it:
```bash
git push --set-upstream origin <feature-name>-<your-name>
```

Thanks for reading and contributing!

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY5NzA5Nzc1MCwtODU2NDU1NTg4LDY3OD
c1MTgxOF19
-->