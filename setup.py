from setuptools import find_packages, setup

package_name = 'beginner_package'

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
    maintainer='sanjuna',
    maintainer_email='robotechietipstutorials@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_publisher =  beginner_package.hello_publisher:main',
            'hello_subscriber =  beginner_package.hello_subscriber:main',            
        ],
    },
)
