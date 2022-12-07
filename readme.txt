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



Todo:
-	the web site and its source code are presented online to the instructor in agreed time (required) 
-	there must be more than 1 model, (2 points)
-	users [board gamers] can view a list of all [available board games] entities of one kind, (2 points)
-	a user [a board gamer] can edit instances to at least 2 models [(not only a board game)], (2 points)
-	information security is considered, at least partly, (2 points)
-	the web site looks good and is styled (2 points) 
Tehty:
-	a gamer is clearly informed the reason he can’t borrow the 4h game simultaneously  (1 point)
-	no gamer can borrow than 3 games simultaneously (1 point)
-	a user can do something for an entity [a board gamer can borrow a board game]. (2 points)
-	template inheritance is used, (1 point)
-	the web site is implemented for an accepted subject, (required)
-	MVT architecture is obeyed, (2 points)
-	the implemented web site functions, (2 points)
-	MVT architecture is obeyed, (2 points)
-	a user [a board gamer] can add an entity [a board game], (2 points)
-	user accounts have been set up (2 point)
-	login and logout functionality has been implemented (2 points)
-	sign-up functionality has been implemented, (2 points)
-	restricted access has been implemented, (2 points)
-	Django admin site is functioning for the application and the superuser is created, (1 point)





