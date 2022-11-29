Git komennot:
Setup:
git config --global github.user user.nimes
git config --global github.password salasana123
Yhdistäminen githubiin:
cd sinne mihin haluut kansion
git clone https://github.com/jouko-aalto/sovellus_ohjelmointi.git
Muutoksien tekeminen:
git add . && git commit -m "joku kommentti"
git push origin dev
Muutoksien lataaminen githubista:
git pull origin dev(/tai main)
Muuta:
git switch dev tai main  (vaihtaa dev tai main branchiin)
