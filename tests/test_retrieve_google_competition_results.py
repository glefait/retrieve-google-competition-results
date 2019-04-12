#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `retrieve_google_competition_results` package."""

import pytest

from retrieve_google_competition_results.utils import encode, decode


def test_encode_decode():
    encoded_param = "eyJtaW5fcmFuayI6MzEsIm51bV9jb25zZWN1dGl2ZV91c2VycyI6MTB9"
    assert encode(decode(encoded_param)) == encoded_param
