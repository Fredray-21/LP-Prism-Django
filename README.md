# TP Framework - Licence Pro Prism

Ce dépôt contient tous mes TP réalisés dans le cadre de ma licence professionnelle Prism en développement Framework en Django.

## Description
Dans ce dépôt, vous trouverez le TP que j'ai réalisés tout au long de ma formation.

## Comment utiliser ce dépôt
Ce dépôt peut être utilisé comme référence pour les projets futurs ou pour aider les autres étudiants en difficulté. Il est à noter que les TP présentés dans ce dépôt ont été réalisés dans le cadre de ma formation, il est donc conseillé de respecter les droits d'auteur et de ne pas les réutiliser tels quels.

Si vous avez des questions sur l'utilisation de ce dépôt, n'hésitez pas à me contacter.



# Idée pour le projet final
* Création d'une nouvelle œuvre d'art : Permettez aux artistes de créer un profil et d'ajouter de nouvelles œuvres d'art à la galerie. Ils pourront fournir des informations telles que le titre, la description, le médium, les dimensions, l'année de création et télécharger une image représentative de l'œuvre.


* Consultation des œuvres d'art : Affichez une liste d'œuvres d'art dans la galerie, permettant aux utilisateurs de parcourir et de voir les détails de chaque œuvre. Ils pourront visualiser l'image, lire la description et les informations supplémentaires.


* Mise à jour des informations sur une œuvre d'art : Autorisez les artistes à modifier les détails d'une œuvre existante. Ils peuvent mettre à jour le titre, la description, les informations techniques, l'image, etc.


* Suppression d'une œuvre d'art : Offrez aux artistes la possibilité de supprimer une œuvre d'art de la galerie si nécessaire. Assurez-vous de demander une confirmation pour éviter les suppressions accidentelles.


 
* Gestion des artistes : Permettez aux administrateurs de la galerie de gérer les profils des artistes. Ils pourront ajouter de nouveaux artistes, mettre à jour leurs informations, suspendre ou supprimer des profils si nécessaire.

* Ajout de catégories ou de tags : Mettez en place un système de catégorisation ou de balisage des œuvres d'art. Cela permettra aux utilisateurs de filtrer les œuvres par catégorie ou par tag spécifique, facilitant ainsi la recherche et la découverte d'œuvres.

* Système de commentaires : Intégrez un système de commentaires permettant aux utilisateurs de la galerie de laisser des commentaires sur les œuvres d'art. Ils pourront partager leurs opinions, poser des questions aux artistes ou engager des discussions.

## En ce qui concerne la base de données (BDD), vous pouvez envisager de stocker les informations suivantes :


Table "Artists" : pour stocker les détails des artistes tels que leur nom, leur biographie, leur photo de profil, etc.
Table "Artworks" : pour stocker les informations spécifiques à chaque œuvre d'art, telles que le titre, la description, les informations techniques, l'image, etc. Cette table peut être liée à la table "Artists" par une clé étrangère pour identifier l'artiste responsable de chaque œuvre.
Table "Categories" : pour stocker les différentes catégories d'œuvres d'art.
Table "Tags" : pour stocker les tags ou mots-clés associés à chaque œuvre d'art.
Table "Comments" : pour stocker les commentaires des utilisateurs, en les associant à l'œuvre d'art correspondante.
Assurez-vous de concevoir une structure de base de données adaptée à vos besoins et d'optimiser les requêtes pour garantir des performances optimales pour votre application de galerie d'art.