#!/usr/bin/env python
# -*- coding: utf8 -*-

from github3 import login
import logging

import nyconfig

gh = login(nyconfig.github_email(),nyconfig.github_password())

logging.debug(gh)

repo = gh.repository('JulienPobot','NichoirConnecte')

def upload_csv(csvfile,jour):
   with open(csvfile,"rb") as f:
      repo.create_file("csv/%s.csv" % jour,"Upload du fichier CSV du jour",f.read())
      f.close()
   logging.debug("Création du fichier sur GitHub")   
