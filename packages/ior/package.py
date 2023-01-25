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

    variant('chfs', when='@3.3.1:', default=False, description='support CHFS in IOR')
    variant('gpu', when='@3.3.1:', default=False, description='support gpuDirect')

    # cuda
    depends_on('cuda', when='+gpu')

    # chfs
    depends_on('chfs', when='+chfs')
    depends_on('openssl', when='+chfs')
    depends_on('pkgconfig', when='+chfs')
    conflicts('+chfs', when='@:3') # force ior@main or @develop

    def configure_args(self):
        spec = self.spec
        config_args = super(Ior, self).configure_args()

        if '+chfs' in spec:
            config_args.append('--with-chfs')

        if '+gpu' in spec:
            config_args.append('--with-gpuDirect')
        else:
            config_args.append('--without-gpuDirect')

        return config_args
