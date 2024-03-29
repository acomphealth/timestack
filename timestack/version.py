# Same semantics as sys.version_info.
version_info = (5, 0, 0, 'alpha', 1)


def _make_version(major, minor, micro, releaselevel, serial):
    """Create a readable version string from version_info tuple components."""
    assert releaselevel in ['alpha', 'beta', 'candidate', 'final']
    version = "%d.%d" % (major, minor)
    if micro:
        version += ".%d" % (micro,)
    if releaselevel != 'final':
        short = {'alpha': 'a', 'beta': 'b', 'candidate': 'rc'}[releaselevel]
        version += "%s%d" % (short, serial)
    return version


def _make_url(major, minor, micro, releaselevel, serial):
    """Make the URL people should start at for this version of timestack.py."""
    url = "https://timestack.readthedocs.io"
    if releaselevel != 'final':
        # For pre-releases, use a version-specific URL.
        url += "/en/coverage-" + _make_version(major, minor, micro, releaselevel, serial)
    return url


__version__ = _make_version(*version_info)
__url__ = _make_url(*version_info)
