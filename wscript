#! /usr/bin/env python
# vim : set fileencoding=utf-8 expandtab noai ts=4 sw=4 filetype=python :
APPNAME = 'SoCRocket'
VERSION = '$Revision$'
top = '.'
out = 'build'

import sys
from waflib.Tools import waf_unit_test  
from tools.waf.logger import Logger

LOAD = [
    'compiler_c',
    'compiler_cxx',
    'python',
    'waf_unit_test',
]

TOOLS = [
    'common',
    'repo',
    'swig',
    'flags',
    'virtualenv',
    'pthreads',
    'boosting',
    'endian',
    'grlib',
    'modelsim',
    'systools',
    'libelf',
    'systemc',
    'cmake',
    'winsocks',
#    'trap',
#    'sdl',
#    'mpeg3',
    'lua',
#    'blas',
#    'lapack',
    'greenlib',
    'ambakit',
    'socrocket',
    'wizard',
    'docs',
#    'shell',
    'cpplint',
    'oclint',
    'clang_compilation_database',
    'sparcelf',
]

def options(self): 
    self.load(LOAD)
    self.load(TOOLS, tooldir='tools/waf')

def configure(self):
    self.load(LOAD)
    self.check_waf_version(mini='1.6.0')
    self.check_python_version((2,4,0))
    self.check_python_headers()
    self.load(TOOLS, tooldir='tools/waf')
    self.env.CPPLINT_FILTERS = ','.join((
    #    '-whitespace/newline',      # c++11 lambda
    #    '-readability/braces',      # c++11 constructor
    #    '-whitespace/braces',       # c++11 constructor
    #    '-build/storage_class',     # c++11 for-range
    #    '-whitespace/blank_line',   # user pref
    #    '-whitespace/labels'        # user pref
    ))
    
def build(self):
    logger = Logger("%s/build.log" % self.bldnode.abspath())
    sys.stdout = logger
    sys.stderr = logger
    
    self.recurse_all()
    self.recurse_all_tests()

    # Install headers
    self.install_files('${PREFIX}/include', self.path.ant_glob(['**/*.h', '**/*.tpp'], excl=['build','**/signalkit/**', '**/tests/**', '**/extern/**', '**/contrib/**', '**/platform/**', '**/software/**', '**/.svn/**', '**/.git/**']))
    self.install_files('${PREFIX}/', ['waf', 'wscript', 'platforms/wscript'], relative_trick=True)
    self.install_files('${PREFIX}/', self.path.ant_glob('tools/**', excl=['**/*.pyc', '**/.svn/**', '**/.git/**']), relative_trick=True)
    self.install_files('${PREFIX}/', self.path.ant_glob('templates/**', excl=['**/*~', '**/.svn/**', '**/.git/**']), relative_trick=True)
    self.install_files('${PREFIX}/include', self.path.ant_glob('contrib/grambasockets/*.h', excl=['**/*~', '**/.svn/**', '**/.git/**']))
    self.add_post_fun(waf_unit_test.summary)
