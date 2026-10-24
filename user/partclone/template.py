pkgname = "partclone"
pkgver = "0.3.50"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-fuse",
    "--enable-extfs",
    # "--enable-reiserfs",  # Not in distro
    # "--enable-reiser4",  # Not in distro
    "--enable-xfs",
    "--enable-ntfs",
    "--enable-fat",
    "--enable-exfat",
    "--enable-hfsp",
    # "--enable-apfs",  # Not in distro
    # "--enable-ufs",  # Not in distro
    # "--enable-vmfs",  # Not in distro
    # "--enable-jfs",  # Library not in progs package
    "--enable-btrfs",
    "--enable-f2fs",
    "--enable-nilfs2",
    "--enable-ncursesw",
]
make_build_args = ["MAN_STYLESHEET=/usr/share/xsl/docbook/manpages/docbook.xsl"]
hostmakedepends = [
    "autoconf",
    "automake",
    "bash",  # used by tests
    "btrfs-progs-libs",
    "docbook-xsl",
    "e2fsprogs-devel",
    "fuse-devel",
    "gettext-devel",
    "hfsutils",
    "libtool",
    "libxslt-progs",
    "linux-headers",
    "ncurses-devel",
    "ncurses-libtinfo-devel",
    "nilfs-utils-devel",
    "ntfs-3g-devel",
    "openssl3-devel",
    "pkgconf",
    "userspace-rcu-devel",
    "util-linux-uuid-devel",
    "xfsprogs-devel",
    "xxhash-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
makedepends = []
pkgdesc = "Utilities to back up and restore used-blocks of a partition"
license = "GPL-2.0-or-later"
url = "https://partclone.org"
source = [
    f"https://github.com/Thomas-Tsai/partclone/archive/refs/tags/{pkgver}.tar.gz",
]
sha256 = [
    "ba66e6c7b46da3339bc7369ca90d647383660f8e74874a82dd8034a39193876e",
]
