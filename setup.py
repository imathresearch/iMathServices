import os
from distutils.core import setup
from setuptools import find_packages
from os.path import expanduser


install_requires = [
    'scikit-learn>=0.15.12',
    'scipy>=0.9.0',
    'numpy>=1.9.1',
    'ujson>=1.33',
    'pandas>=0.15.12',
    'tweepy>=3.4.0',
    'TextBlob>=0.9.1',
    'pymongo>=3.0.3'
]


setup(
    name="iMathModelosPredictivos",
    description="API TO RUN PREDICTIVE MODELS",
    version=5.0,
    author="iMathResearch",
    author_email="info@imathresearch.com",
    url="www.imathresearch.com",
    package_dir={'iMathModelosPredictivos': 'iMathModelosPredictivos'},
    package_data={'iMathModelosPredictivos': ['data/*.txt']},
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    scripts=['iMathModelosPredictivos/scripts_Impagos/crearModelo_Impagos', 'iMathModelosPredictivos/scripts_Impagos/predecirModelo_Impagos', 'iMathModelosPredictivos/scripts_Impagos/testearModelo_Impagos', 'iMathModelosPredictivos/scripts_UpCrossSelling/crearModelo_UpCrossSelling', 'iMathModelosPredictivos/scripts_UpCrossSelling/testearModelo_UpCrossSelling', 'iMathModelosPredictivos/scripts_UpCrossSelling/recomendarModelo_UpCrossSelling', 'iMathModelosPredictivos/scripts_NuevoCliente/crearModelo_NuevoCliente', 'iMathModelosPredictivos/scripts_NuevoCliente/testearModelo_NuevoCliente', 'iMathModelosPredictivos/scripts_NuevoCliente/predecirModelo_NuevoCliente', 'iMathModelosPredictivos/scripts_Baja/crearModelo_Baja', 'iMathModelosPredictivos/scripts_Baja/testearModelo_Baja', 'iMathModelosPredictivos/scripts_Baja/predecirModelo_Baja', 'iMathModelosPredictivos/scripts_Abandono/crearModelo_Abandono', 'iMathModelosPredictivos/scripts_Abandono/testearModelo_Abandono', 'iMathModelosPredictivos/scripts_Abandono/predecirModelo_Abandono', 'iMathModelosPredictivos/scripts_AnalisisTextos/PredecirTexto_Twitter'],
)

home = expanduser("~")
model_directory = os.path.join(home, 'modelos_predictivos')
if not os.path.exists(model_directory):
    os.makedirs(model_directory)
