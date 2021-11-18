# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for generic and customizable requests."""

from .records.request_types import RequestType
from .resolvers import UserResolver
from .resolvers.requests import RequestResolver
from .services.permissions import PermissionPolicy

REQUESTS_PERMISSION_POLICY = PermissionPolicy
"""Override the default requests/comments permission policy."""

REQUESTS_REGISTERED_TYPES = [RequestType()]
"""Configuration for registered Request Types."""

REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    RequestResolver(),
]
"""Registered resolvers for resolving/creating references in request metadata."""
