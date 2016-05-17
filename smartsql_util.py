#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: jack <jacktan.whu@foxmail.com>
#

from smartsql import Condition, Field


def common_datetime_wheres(f_datetime, start_time=None, end_time=None):

    if not isinstance(f_datetime, Field):
        raise TypeError("f_datetime must be a Field instance")

    wheres = Condition('TRUE')

    if start_time is not None:
        wheres &= (f_datetime >= start_time)

    if end_time is not None:
        wheres &= (f_datetime < end_time)

    return wheres
