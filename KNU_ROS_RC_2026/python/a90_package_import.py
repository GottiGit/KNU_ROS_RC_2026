# import test_package.module_a
# import test_package.module_b
# from test_package.module_a import Module_a, module_a_fuc, module_var_a
from KNU_ROS_RC_2026.python.test_package import *


def main():
    # print(test_package.module_a.Module_a())
    # print(test_package.module_a.module_var_a)
    # test_package.module_a.module_a_fuc()
    # print(test_package.module_b.Module_b())
    # print(test_package.module_b.module_var_b)
    # test_package.module_b.module_b_fuc()
    # print(test_package.Module_a())
    # print(test_package.module_var_a)
    # test_package.module_a_fuc()
    # test_package.module_b_fuc()
    print(module_var_a)
    module_a_fuc()
    module_b_fuc()


if __name__ == "__main__":
    main()
