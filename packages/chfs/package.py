from spack.package import *


class Chfs(AutotoolsPackage):
    '''CHFS parallel and distributed file system for node-local persistent memory'''

    homepage = 'https://github.com/otatebe/chfs'
    git = 'https://github.com/otatebe/chfs.git'
    url = 'https://github.com/otatebe/chfs/archive/1.0.0.tar.gz'

    maintainers = ['range3']

    version('master', branch='master')
    version('develop', branch='master')
    version('2.1.0', sha256='6cc21e9b890628eab0c8a669ec71787de6b71dd77827519e2723472d48337d63', preferred=True)
    version('2.0.0', sha256='61aa3600963bded220c28adc8be8bcb0e6dd2ef56f7fb596f4bdefcec37f73ae')
    version('1.0.0', sha256='315295bf10b3b3fb93620791e844c540f6f238b4eab6a5c56825c6b7896737a2')
    # version('1.0.0-exp', git='', branch='experimental')

    variant('verbs', default=False, description='enable verbs')
    variant('pandoc', default=False, description='generate manual pages')
    variant('pmemkv', default=True, description='use pmemkv instead of a POSIX backend')
    variant('devdax', default=False, when='+pmemkv', description='enable devdax support')
    variant('zero_copy_read_rdma', default=False, when='+pmemkv', description='enable zero copy read rdma')

    depends_on('libfabric fabrics=rxm,sockets,tcp,udp', when='~verbs')
    depends_on('libfabric fabrics=rxm,sockets,tcp,udp,verbs', when='+verbs')
    depends_on('mochi-margo')
    depends_on('pmemkv', when='+pmemkv')
    depends_on('pmdk+ndctl', when='+devdax')
    depends_on('libfuse@2')
    depends_on('pandoc', when='+pandoc')

    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('libtool', type=('build'))
    depends_on('pkgconfig', type=('build'))

    def autoreconf(self, spec, prefix):
        autoreconf = which('autoreconf')
        autoreconf('-fiv')

    def configure_args(self):
        args = []

        if '+pmemkv' in self.spec:
            args.extend(['--with-pmemkv'])

        if '+zero_copy_read_rdma' in self.spec:
            args.extend(['--enable-zero-copy-read-rdma'])
        

        return args
