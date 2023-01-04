from setuptools import setup

setup(
    name='bulk_crawler',
    packages=['bulk_crawler'],
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'asyncio'
    ],
)
