#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the project description on Modrinth based on the README file."""
import os
from pathlib import Path

import requests

API_KEY: str = os.environ["modrinth_pat"]
"""TOP SECRET - Modrinth Personnal Access Token"""
PROJECT_SLUG: str = os.environ["modrinth_slug"]
"""Modrinth project ID (slug)"""

README_PATH: Path = Path("./README.md")

DEFAULT_HEADERS: dict[str, str] = requests.utils.default_headers()
"""Default requests headers."""

data: requests.Response = requests.patch(
  ENDPOINT,
  json={
    "body": open(README_PATH).read(),
  },
  headers={
    "Authorization": API_KEY,
    "User-Agent": "Virinas-code/ATR-Advanced_Technologies_Reforged/1.0 (contact via GitHub Discussions / Issues) " + DEFAULT_HEADERS.get("User-Agent", ""),
  }
)
