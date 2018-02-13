#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git

import pdb; pdb.set_trace()

repo = git.Repo.init('.')

repo.git.status()


remote = repo.remote()



repo.git.status()

