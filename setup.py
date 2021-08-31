from distutils.core import setup
setup(
  name = 'marker',
  packages = ['marker'],
  version = '0.1',
  license='MIT',
  description = 'Marker is a language that transpiles directly to HTML.',
  url = 'https://github.com/MystPi/marker',
  download_url = 'https://github.com/MystPi/marker/archive/refs/tags/v0.1.tar.gz',
  keywords = ['HTML', 'Language', 'Transpiler'],
  install_requires=[
          'lark'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
