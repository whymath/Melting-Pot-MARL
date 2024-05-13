# Copyright 2020 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Install script for setuptools."""

import os
import shutil
import tarfile
import urllib.request

import setuptools
from setuptools.command import build_py

VERSION = '2.1.1.dev10'
ASSETS_VERSION = '2.1.0'

ASSETS_URL = f'http://storage.googleapis.com/dm-meltingpot/meltingpot-assets-{ASSETS_VERSION}.tar.gz'


class BuildPy(build_py.build_py):
  """Command that downloads Melting Pot assets as part of build_py."""

  def run(self):
    self.download_and_extract_assets()
    if not self.editable_mode:
      super().run()
      self.build_assets()

  def download_and_extract_assets(self):
    """Downloads and extracts assets to meltingpot/assets."""
    tar_file_path = os.path.join(
        self.get_package_dir('assets'), os.path.basename(ASSETS_URL))
    if os.path.exists(tar_file_path):
      print(f'found cached assets {tar_file_path}', flush=True)
    else:
      os.makedirs(os.path.dirname(tar_file_path), exist_ok=True)
      print('downloading assets...', flush=True)
      urllib.request.urlretrieve(ASSETS_URL, filename=tar_file_path)
      print(f'downloaded {tar_file_path}', flush=True)

    root = os.path.join(self.get_package_dir(''), 'meltingpot')
    os.makedirs(root, exist_ok=True)
    if os.path.exists(f'{root}/assets'):
      shutil.rmtree(f'{root}/assets')
      print('deleted existing assets', flush=True)
    with tarfile.open(tar_file_path, mode='r|*') as tarball:
      tarball.extractall(root)
    print(f'extracted assets from {tar_file_path} to {root}/assets', flush=True)

  def build_assets(self):
    """Copies assets from package to build lib."""
    package_root = os.path.join(self.get_package_dir(''), 'meltingpot')
    os.makedirs(package_root, exist_ok=True)
    build_root = os.path.join(self.build_lib, 'meltingpot')
    if os.path.exists(f'{build_root}/assets'):
      shutil.rmtree(f'{build_root}/assets')
      print('deleted existing assets', flush=True)
    shutil.copytree(f'{package_root}/assets', f'{build_root}/assets')
    print(f'copied assets from {package_root}/assets to {build_root}/assets',
          flush=True)


setuptools.setup(
    name='dm-meltingpot',
    version=VERSION,
    license='Apache 2.0',
    license_files=['LICENSE'],
    url='https://github.com/deepmind/meltingpot',
    download_url='https://github.com/deepmind/meltingpot/releases',
    author='DeepMind',
    author_email='noreply@google.com',
    description=(
        'A suite of test scenarios for multi-agent reinforcement learning.'),
    keywords='multi-agent reinforcement-learning python machine-learning',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    cmdclass={'build_py': BuildPy},
    package_dir={
        'meltingpot': 'meltingpot',
        'baselines': 'baselines',
    },
    package_data={
        'meltingpot.lua': ['**'],
    },
    python_requires='>=3.9', #changed from 3.10
    install_requires=[
        #'absl-py',
        # 'chex<0.1.81',  # Incompatible with tensorflow 2.13 (due to numpy req).
        #'chex==0.1.86',
        #'dm-env',
        #'dmlab2d',
        #'dm-tree',
        #'immutabledict',
        #'ml-collections',
        #'networkx',
        #'numpy==1.24.3',
        #'opencv-python',
        #'pandas',
        #'pygame',
        #'reactivex',
        #'tensorflow==2.11.1',
        #'tensorflow',
        #'tensorflow-probability',
        #'torch==2.0.1',
        #'ray==2.10.0',
        #'gymnasium',
        #'matplotlib',
        #'pydantic==1.10.12',
        #'wandb',
        'absl-py==2.1.0',
        'aiohttp==3.9.3',
        'aiohttp-cors==0.7.0',
        'aiosignal==1.3.1',
        'annotated-types==0.6.0',
        'anyio==4.3.0',
        'appdirs==1.4.4',
        'astunparse==1.6.3',
       'async-timeout==4.0.3',
       'attrs==23.2.0',
       'cachetools==5.3.3',
       'certifi==2024.2.2',
       'charset-normalizer==3.3.2',
       'chex==0.1.86',
       'click==8.1.7',
       'cloudpickle==3.0.0',
    'colorful==0.5.6',
    'contextlib2==21.6.0',
    'distlib==0.3.8',
    'dm-env==1.6',
    'dm-meltingpot==2.1.1.dev10',
    'dm-tree==0.1.8',
    'dmlab2d==1.0.0',
    'docker-pycreds==0.4.0',
    'e==1.4.5',
    'exceptiongroup==1.2.0',
    'Farama-Notifications==0.0.4',
    # 'fastapi==0.110.0',
    'filelock==3.13.1',
    'flatbuffers==24.3.7',
    'frozenlist==1.4.1',
    'fsspec==2024.3.1',
    'gast==0.5.4',
    'gitdb==4.0.11',
    'GitPython==3.1.42',
    'google-api-core==2.18.0',
    'google-auth==2.29.0',
    'google-pasta==0.2.0',
    'googleapis-common-protos==1.63.0',
    'grpcio==1.62.1',
    'gymnasium==0.29.1',
    'h11==0.14.0',
    'h5py==3.10.0',
    'httptools==0.6.1',
    'idna==3.6',
    'immutabledict==4.2.0',
    'importlib_metadata==7.1.0',
    'jax==0.4.25',
    'jaxlib==0.4.25',
    'Jinja2==3.1.3',
    'jsonschema==4.21.1',
    'jsonschema-specifications==2023.12.1',
    'keras==3.1.1',
    'libclang==18.1.1',
    'lz4==4.3.3',
    'Markdown==3.6',
    'markdown-it-py==3.0.0',
    'MarkupSafe==2.1.5',
    'mdurl==0.1.2',
    'ml-dtypes==0.3.2',
    'ml_collections==0.1.1',
    'mpmath==1.3.0',
    'msgpack==1.0.8',
    'multidict==6.0.5',
    'namex==0.0.7',
    'networkx==3.2.1',
    'numpy==1.26.4',
    'opencensus==0.11.4',
    'opencensus-context==0.1.3',
    'opencv-python==4.9.0.80',
    'opt-einsum==3.3.0',
    'optree==0.10.0',
    'packaging==24.0',
    'pandas==2.2.1',
    'pillow==10.2.0',
    'platformdirs==4.2.0',
    'prometheus_client==0.20.0',
    'proto-plus==1.23.0',
    'protobuf==4.25.3',
    'psutil==5.9.8',
    'py-spy==0.3.14',
    'pyarrow==15.0.2',
    'pyasn1==0.5.1',
    'pyasn1-modules==0.3.0',
    'pydantic==2.6.4',
    'pydantic_core==2.16.3',
    'pygame==2.5.2',
    'Pygments==2.17.2',
    'python-dateutil==2.9.0.post0',
    'python-dotenv==1.0.1',
    'pytz==2024.1',
    'PyYAML==6.0.1',
    'ray==2.10.0',
    'reactivex==4.0.4',
    'referencing==0.34.0',
    'requests==2.31.0',
    'rich==13.7.1',
    'rpds-py==0.18.0',
    'rsa==4.9',
    'scipy==1.12.0',
    'sentry-sdk==1.43.0',
    'setproctitle==1.3.3',
    'six==1.16.0',
    'smart-open==7.0.3',
    'smmap==5.0.1',
    'sniffio==1.3.1',
    'starlette==0.36.3',
    'sympy==1.12',
    'tensorboard==2.16.2',
    'tensorboard-data-server==0.7.2',
    'tensorboardX==2.6.2.2',
    'tensorflow==2.16.1',
    'tensorflow-io-gcs-filesystem==0.36.0',
    'tensorflow-macos==2.16.1',
    'termcolor==2.4.0',
    'toolz==0.12.1',
    'torch==2.2.1',
    'typer==0.10.0',
    'typing_extensions==4.10.0',
    'tzdata==2024.1',
    'urllib3==2.2.1',
    'uvicorn==0.29.0',
    'uvloop==0.19.0',
    'virtualenv==20.25.1',
    'wandb==0.16.5',
    'watchfiles==0.21.0',
    'websockets==12.0',
    'Werkzeug==3.0.1',
    'wrapt==1.16.0',
    'yarl==1.9.4',
    'zipp==3.18.1',

    ],
    extras_require={
        # Used in development.
        'dev': [
            'build',
            'isort',
            'pipreqs',
            'pyink',
            'pylint',
            'pytest-xdist',
            'pytype',
        ],
    },
)
