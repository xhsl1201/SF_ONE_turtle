from setuptools import find_packages, setup
import os

package_name = 'sf_one_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'models'), ['sf_one_turtle/models/best.pt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khj',
    maintainer_email='xhsl1201.gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
          'camera_view = sf_one_turtle.camera_view_test:main',
          'turtle_yolo = sf_one_turtle.turtlebot_yolo_test:main'
        ],
    },
)
