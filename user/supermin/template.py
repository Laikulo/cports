pkgname = "supermin"
pkgver = "5.2.2"
pkgrel = 0
build_style = "configure"
makedepends = [
        "bash",
        "e2fsprogs",
        "e2fsprogs-devel",
        "findlib",
        "file",
        "gawk",
        "libatomic-chimera-devel-static",
        "libunwind-devel-static",
        "musl-devel-static",
        "ocaml",
        "perl",
        "pkgconf",
]
pkgdesc = "Tool for creating supermin appliances"
license = "GPL-2.0-only"
url = "https://libguestfs.org"
source = f"https://download.libguestfs.org/supermin/5.2-stable/supermin-{pkgver}.tar.gz"
sha256 = "ce3921d3635c8168cfb7ca0c5a82b9d5cef5b2b271f84b776d63b8bbbeec358e"
