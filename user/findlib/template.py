pkgname = "findlib"
pkgver = "1.9.8"
pkgrel = 0
build_style = "configure"
configure_args = [ 
    "-mandir", "/usr/share/man",
    "-config", "/etc/findlib.conf"
]
makedepends = [
        "ocaml",
        "ocaml-compiler-libs"
]
depends = [ "ocaml-runtime" ]
pkgdesc = "OCaml library manager"
license = "MIT"
url = "https://projects.camlcity.org/projects/findlib.html"
source = f"https://download.camlcity.org/download/findlib-{pkgver}.tar.gz"
sha256 = "662c910f774e9fee3a19c4e057f380581ab2fc4ee52da4761304ac9c31b8869d"
# does not provide a check target
options = [ "!check" ]

def post_install(self):
    self.install_license("LICENSE")
