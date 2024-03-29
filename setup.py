import setuptools

version = "2.0.1"

setuptools.setup(
    name='configcat-flag-reference-validator',
    version=version,
    scripts=['configcat-validator.py'],
    packages=['configcat', 'configcat.reference_validator'],
    url='https://github.com/configcat/feature-flag-reference-validator',
    license='MIT',
    author='ConfigCat',
    author_email='team@configcat.com',
    description='ConfigCat feature flag reference validator.',
    long_description="This tool can be used for discovering ConfigCat feature flag usages in your source code and validating them against your own ConfigCat configuration dashboard. It searches for ConfigCat SDK usage and greps the feature flag keys from the source code, then it compares them with the keys got from your ConfigCat dashboard. Manage features and change your software configuration using ConfigCat feature flags, without the need to re-deploy code. A 10 minute trainable dashboard allows even non-technical team members to manage application features. Supports A/B testing, soft launching or targeting a specific group of users first with new ideas. Deploy any time, release when confident. Open-source SDKs enable easy integration with any web, mobile or backend application. https://configcat.com",
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
)
