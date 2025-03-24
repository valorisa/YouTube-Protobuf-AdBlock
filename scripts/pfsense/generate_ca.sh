#!/bin/bash

# Génération du certificat CA pour MITMProxy
openssl req -x509 -newkey rsa:4096 -keyout ca.key -out ca.crt -days 365 -nodes -subj "/CN=YouTube-Protobuf-AdBlock CA"

echo "Certificat CA généré avec succès."
