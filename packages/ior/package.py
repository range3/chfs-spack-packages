# Copyright 2022 range3 ( https://github.com/range3/ )
# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.pkg.builtin.ior import Ior as BuiltinIor

class Ior(BuiltinIor):

    git = 'https://github.com/hpc/ior'
    version('develop', branch='main', submodules=True)
    version('main', branch='main', submodules=True)

    variant('chfs', default=False, description='support CHFS in IOR')

    # chfs
    depends_on('chfs', when='+chfs')
    depends_on('openssl', when='+chfs')
    depends_on('pkg-config', when='+chfs')
    conflicts('+chfs', when='@:3') # force ior@main or @develop

    def configure_args(self):
        spec = self.spec
        config_args = super(Ior, self).configure_args()

        if '+chfs' in spec:
            config_args.append('--with-chfs')

        return config_args
