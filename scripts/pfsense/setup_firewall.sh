#!/bin/bash

# Redirection du trafic YouTube vers MITMProxy
pfctl -t mitm_redirect -T add 192.168.1.0/24
iptables -t nat -A PREROUTING -i em1 -p tcp --dport 443 -j DNAT --to-destination 127.0.0.1:8080

echo "Configuration du pare-feu terminée."
