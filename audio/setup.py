from setuptools import find_packages, setup

package_name = 'audio'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cae',
    maintainer_email='cae@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["realtime_audio_orin = audio.realtime_audio_orin:main",
                            "realtime_audio_pc = audio.realtime_audio_pc:main",
        ],
    },
)
