import subprocess

import nose.tools

import rospkg


def test_create_urdf():
    urdf_file = rospkg.RosPack().get_path('create_description') + '/urdf/create.urdf.xacro'
    subprocess.check_call(['rosrun', 'xacro', 'xacro', '--inorder', '--xacro-ns', urdf_file])


def test_create_2_urdf():
    urdf_file = rospkg.RosPack().get_path('create_description') + '/urdf/create_2.urdf.xacro'
    subprocess.check_call(['rosrun', 'xacro', 'xacro', '--inorder', '--xacro-ns', urdf_file])
