from setuptools import setup
from glob import glob
import os

package_name = 'project_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'urdf'),
        glob('urdf/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'goal_navigator = project_package.goal_navigator:main',
            'go_to_goal = project_package.go_to_goal:main',
            'project_node = project_package.project_node:main',
        ],
    },
)
