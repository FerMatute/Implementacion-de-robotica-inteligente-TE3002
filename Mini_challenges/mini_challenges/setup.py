from setuptools import find_packages, setup

package_name = 'mini_challenges'

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
    maintainer='ricardon',
    maintainer_email='ricardonavarro2003@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'challenge4 = mini_challenges.challenge4:main',
            'color_id = mini_challenges.color_id:main',
        ],
    },
)
