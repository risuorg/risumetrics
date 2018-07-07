.. image:: https://img.shields.io/github/license/citellusorg/citmetrics.svg :alt: LICENSE
.. image:: https://travis-ci.org/citellusorg/citmetrics.svg?branch=master :alt:  Build Status
.. image:: https://coveralls.io/repos/github/citellusorg/citmetrics/badge.svg?branch=master :alt:  Coverage Status
.. image:: https://img.shields.io/github/release/citellusorg/citmetrics.svg :alt:  Releases


Introduction
============

Citmetrics  is a set of simple scripts to receive incoming `--call-home <serveruri>`  over http and store as json files on disk.

Those files will be later analized for metrics information like most 'hit' issue on executions to detect plugins that always return the same status and hence are not useful or erroneous or even to detect old plugins that are no longer relevant in current systems.