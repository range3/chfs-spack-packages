from spack import *


class Chfs(AutotoolsPackage):
    """CHFS parallel and distributed file system for node-local persistent memory"""

    homepage = 'https://github.com/otatebe/chfs'
    git = 'https://github.com/otatebe/chfs.git'
    url = 'https://github.com/otatebe/chfs/archive/v1.0.0.tar.gz'

    maintainers = ['range3']

    version('master', branch='master')
    version('develop', branch='master')
    version('1.0.0', sha256='9e8fce88a6bd9c1002b4a6924c935ebb2e2024e3afe6618b17e23538335bd15d')
    # version('1.0.0-exp', git='', branch='experimental')

    variant('verbs', default=False, description="enable verbs")

    depends_on('libfabric fabrics=rxm,sockets,tcp,udp', when='~verbs')
    depends_on('libfabric fabrics=rxm,sockets,tcp,udp,verbs', when='+verbs')
    depends_on('mercury')
    depends_on('mochi-margo')
    depends_on('pmemkv')
    depends_on('memkind')
    depends_on('libpmemobj-cpp')

    depends_on('autoconf', type=("build"))
    depends_on('m4', type=('build'))
    depends_on('automake', type=("build"))
    depends_on('libtool', type=("build"))
    depends_on('pkg-config', type=("build"))

    def configure_args(self):
        args = ['--with-pmemkv']

        if '+verbs' in self.spec:
            args.extend(['--enable-zero-copy-read-rdma'])

        return args
