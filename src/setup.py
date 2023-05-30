from setuptools import setup, find_packages

setup(
    name='PredictiveMaintenanceAutoML',
    version='0.1.0',
    url='https://github.com/Asad1287/AutoML',   
    author='Asad1287',
    author_email='asadali047@gmail.com',
    description='Description of my package',
    packages=find_packages(),                
    install_requires=[
        'pandas==1.5.3',
        'numpy==1.22.4',
        'scikit-learn==1.2.2',
        'paho-mqtt',
        'pyspark',
        'apache-airflow',
        'pymodbus',
        'dask==2022.12.1',
        'category_encoders',
        'dask-glm==0.2.0',
        'dask-ml==2023.3.24',
        'dask-xgboost==0.2.0',
        'pymongo',
        'python-dotenv',
        'category_encoders',
        'pyarrow',
        'boto3',
        'psycopg2-binary',
        'imbalanced-learn',
        'seaborn',
        'dask_xgboost',
        'hyperopt',
        'fastapi',
        'uvicorn',
        'lightgbm',
        'py4j' ],
)