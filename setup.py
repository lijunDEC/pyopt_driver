#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': 'Kenneth T. Moore',
 'author_email': 'kenneth.t.moore-1@nasa.gov',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO driver wrapper for the open-source optimization package pyOpt',
 'download_url': '',
 'entry_points': '[openmdao.component]\npyopt_driver.test.test_pyopt_driver.OptimizationConstrained=pyopt_driver.test.test_pyopt_driver:OptimizationConstrained\npyopt_driver.test.test_pyopt_driver.MultiFunction=pyopt_driver.test.test_pyopt_driver:MultiFunction\npyopt_driver.test.test_pyopt_driver.ArrayOpt=pyopt_driver.test.test_pyopt_driver:ArrayOpt\npyopt_driver.test.test_pyopt_driver.BenchMarkOptimization=pyopt_driver.test.test_pyopt_driver:BenchMarkOptimization\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver\npyopt_driver.test.test_pyopt_driver.ArrayParaboloid=pyopt_driver.test.test_pyopt_driver:ArrayParaboloid\npyopt_driver.test.test_pyopt_driver.OptimizationConstrainedDerivatives=pyopt_driver.test.test_pyopt_driver:OptimizationConstrainedDerivatives\npyopt_driver.test.test_pyopt_driver.BenchMark=pyopt_driver.test.test_pyopt_driver:BenchMark\npyopt_driver.test.test_pyopt_driver.MultiObjectiveOptimization=pyopt_driver.test.test_pyopt_driver:MultiObjectiveOptimization\n\n[openmdao.driver]\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver\n\n[openmdao.container]\npyopt_driver.test.test_pyopt_driver.OptimizationConstrained=pyopt_driver.test.test_pyopt_driver:OptimizationConstrained\npyopt_driver.test.test_pyopt_driver.MultiFunction=pyopt_driver.test.test_pyopt_driver:MultiFunction\npyopt_driver.test.test_pyopt_driver.ArrayOpt=pyopt_driver.test.test_pyopt_driver:ArrayOpt\npyopt_driver.test.test_pyopt_driver.BenchMarkOptimization=pyopt_driver.test.test_pyopt_driver:BenchMarkOptimization\npyopt_driver.pyopt_driver.pyOptDriver=pyopt_driver.pyopt_driver:pyOptDriver\npyopt_driver.test.test_pyopt_driver.ArrayParaboloid=pyopt_driver.test.test_pyopt_driver:ArrayParaboloid\npyopt_driver.test.test_pyopt_driver.OptimizationConstrainedDerivatives=pyopt_driver.test.test_pyopt_driver:OptimizationConstrainedDerivatives\npyopt_driver.test.test_pyopt_driver.BenchMark=pyopt_driver.test.test_pyopt_driver:BenchMark\npyopt_driver.test.test_pyopt_driver.MultiObjectiveOptimization=pyopt_driver.test.test_pyopt_driver:MultiObjectiveOptimization',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': 'Kenneth T. Moore',
 'maintainer_email': 'kenneth.t.moore-1@nasa.gov',
 'name': 'pyopt_driver',
 'package_data': {'pyopt_driver': ['sphinx_build/html/index.html',
                                   'sphinx_build/html/.buildinfo',
                                   'sphinx_build/html/py-modindex.html',
                                   'sphinx_build/html/objects.inv',
                                   'sphinx_build/html/searchindex.js',
                                   'sphinx_build/html/search.html',
                                   'sphinx_build/html/pkgdocs.html',
                                   'sphinx_build/html/usage.html',
                                   'sphinx_build/html/genindex.html',
                                   'sphinx_build/html/srcdocs.html',
                                   'sphinx_build/html/_sources/usage.txt',
                                   'sphinx_build/html/_sources/pkgdocs.txt',
                                   'sphinx_build/html/_sources/index.txt',
                                   'sphinx_build/html/_sources/srcdocs.txt',
                                   'sphinx_build/html/_static/plus.png',
                                   'sphinx_build/html/_static/comment-bright.png',
                                   'sphinx_build/html/_static/comment.png',
                                   'sphinx_build/html/_static/down-pressed.png',
                                   'sphinx_build/html/_static/sidebar.js',
                                   'sphinx_build/html/_static/doctools.js',
                                   'sphinx_build/html/_static/ajax-loader.gif',
                                   'sphinx_build/html/_static/default.css',
                                   'sphinx_build/html/_static/down.png',
                                   'sphinx_build/html/_static/jquery.js',
                                   'sphinx_build/html/_static/underscore.js',
                                   'sphinx_build/html/_static/minus.png',
                                   'sphinx_build/html/_static/up-pressed.png',
                                   'sphinx_build/html/_static/up.png',
                                   'sphinx_build/html/_static/pygments.css',
                                   'sphinx_build/html/_static/searchtools.js',
                                   'sphinx_build/html/_static/file.png',
                                   'sphinx_build/html/_static/basic.css',
                                   'sphinx_build/html/_static/websupport.js',
                                   'sphinx_build/html/_static/comment-close.png',
                                   'sphinx_build/html/_modules/index.html',
                                   'sphinx_build/html/_modules/pyopt_driver/pyopt_driver.html',
                                   'sphinx_build/html/_modules/pyopt_driver/test/test_pyopt_driver.html',
                                   'test/__init__.py',
                                   'test/test_pyoptdriver.new',
                                   'test/CONMIN.out',
                                   'test/openmdao_log.txt',
                                   'test/test_pyopt_driver.py',
                                   'test/ALPSO_print.out']},
 'package_dir': {'': 'src'},
 'packages': ['pyopt_driver', 'pyopt_driver.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/pyopt-driver',
 'version': '0.14',
 'zip_safe': False}


setup(**kwargs)

