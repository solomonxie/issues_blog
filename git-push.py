#!/usr/bin/env python
# -*- coding: utf-8 -*-

import git

import pdb; pdb.set_trace()

repo = git.Repo.init('.')

repo.git.status()


repo.git.add('.')
repo.git.commit(m='updated')


remote = repo.remote()
remote.push()


repo.git.status()

