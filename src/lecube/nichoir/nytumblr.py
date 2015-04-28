#!/usr/bin/env python
# -*- coding: utf8 -*-

import pytumblr
import logging

import nygithub
import nyconfig

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  nyconfig.consumer_key(),
  nyconfig.consumer_secret(),
  nyconfig.oauth_token(),
  nyconfig.oauth_secret()
)

def message(accroche,titre,msg):
    client.create_text(nyconfig.tumblr_account(), state="published", slug=accroche, title=titre, body=msg)

def snapshot(msg,chemin):
    client.create_photo(nyconfig.tumblr_account(), state="published", tags=["test", "photo"], tweet=msg, data=chemin)

def upload_csv_link(jour,taille):
    logging.debug("Upload CSV")
    client.create_link(nyconfig.tumblr_account(), title="Données du nichoir pour le %s" % jour, url="https://raw.githubusercontent.com/JulienPobot/NichoirConnecte/master/csv/%s.csv" % jour, description="Le fichier de %s octets est disponible contenant toutes les valeurs recueillies depuis 24h." % taille)

