## Résumé du bug 

Quand un user souhaite acheter plus de 12 places aucun check n'est fais, voici la seule condition dans le code :
```py
if pointsclub < placesRequired
```

before fixing:
![alt text](image.png)