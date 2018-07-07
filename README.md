[![License](https://img.shields.io/github/license/citellusorg/citmetrics.svg)](LICENSE)
[![Build Status](https://travis-ci.org/citellusorg/citmetrics.svg?branch=master)](https://travis-ci.org/citellusorg/citmetrics)
[![Coverage Status](https://coveralls.io/repos/github/citellusorg/citmetrics/badge.svg?branch=master)](https://coveralls.io/github/citellusorg/citmetrics?branch=master)
[![Release status](https://img.shields.io/github/release/citellusorg/citmetrics.svg)](https://github.com/citellusorg/citmetrics/releases)


<img src="doc/citmetrics.png" width="20%" border=0 align="right">


### Introduction

Citmetrics  is a set of simple scripts to receive incoming `--call-home <serveruri>`  over http and store as json files on disk.

Those files will be later analyzed for metrics information like most 'hit' issue on executions to detect plugins that always return the same status and hence are not useful or erroneous or even to detect old plugins that are no longer relevant in current systems.

### Execution

In an environment with tox run:

~~~sh
tox -e start
~~~

It will start webserver with default port of `80` so ensure having proper  privileges for doing so.
