#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the project description on Modrinth based on the README file."""
import os
from pathlib import Path

import requests
from requests.models import Response
from requests.structures import CaseInsensitiveDict

API_KEY: str = os.environ["modrinth_pat"]
"""TOP SECRET - Modrinth Personnal Access Token"""
PROJECT_SLUG: str = os.environ["modrinth_slug"]
"""Modrinth project ID (slug)"""

ENDPOINT: str = f"https://api.modrinth.com/v2/project/{PROJECT_SLUG}"
"""API endpoint"""

README_PATH: Path = Path("./README.md")
"""Path to the README file"""

DEFAULT_HEADERS: CaseInsensitiveDict[str] = requests.utils.default_headers()
"""Default requests headers"""
HEADERS: CaseInsensitiveDict[str] = CaseInsensitiveDict(
    {
        "Authorization": API_KEY,
        "User-Agent": "Virinas-code/ATR-Advanced_Technologies_Reforged/1.0"
        + " (contact via GitHub Discussions / Issues) "
        + DEFAULT_HEADERS.get("User-Agent", ""),
    }
)
"""Headers used"""

SESSION: requests.Session = requests.Session()
"""Session for requests"""

SESSION.headers.update(HEADERS)

with open(README_PATH, encoding="utf-8") as file:
    data: Response = requests.patch(
        ENDPOINT,
        json={
            "body": file.read(),
        },
        headers={
            "Authorization": API_KEY,
            "User-Agent": "Virinas-code/ATR-Advanced_Technologies_Reforged/1.0"
            + " (contact via GitHub Discussions / Issues) "
            + DEFAULT_HEADERS.get("User-Agent", ""),
        },
        timeout=15,
    )
