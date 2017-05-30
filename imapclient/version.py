# Copyright (c) 2016, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses

from __future__ import unicode_literals

version_info = (2, 0, 1, 'alpha')


def _imapclient_version_string(vinfo):
    major, minor, micro, releaselevel = vinfo
    v = '%d.%d.%d' % (major, minor, micro)
    if releaselevel != 'final':
        v += '-' + releaselevel
    return v

version = _imapclient_version_string(version_info)
author = 'Menno Smits'
author_email = 'menno@freshfoo.com'

min_pyopenssl_version = '0.15.1'
