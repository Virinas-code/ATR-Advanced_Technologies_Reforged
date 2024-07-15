#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the project description on Modrinth based on the README file."""
import os

print(os.environ["MODRINTH_SLUG"])
print(bool(os.environ["MODRINTH_PAT"]))
