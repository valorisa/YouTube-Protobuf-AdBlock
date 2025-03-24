# Architecture du projet YouTube-Protobuf-AdBlock

## Vue d'ensemble
Ce projet utilise Docker et MITMProxy pour intercepter et modifier le trafic Protobuf de YouTube afin de bloquer les publicités.

## Composants principaux
1. Docker container avec MITMProxy
2. Script Python pour la modification des payloads Protobuf
3. Intégration pfSense pour la redirection du trafic

## Flux de données
1. Le trafic est redirigé via pfSense vers le container Docker
2. MITMProxy intercepte et déchiffre le trafic HTTPS
3. Le script Python modifie les payloads Protobuf
4. Le trafic modifié est renvoyé au client

## Considérations de sécurité
- Utilisation de certificats CA personnalisés
- Isolation du container Docker
