#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the project description on Modrinth based on the README file."""
import os

print(os.environ["modrinth_slug"])
print(bool(os.environ["modrinth_pat"]))
