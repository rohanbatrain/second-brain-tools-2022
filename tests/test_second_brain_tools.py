# Importing production branch modules Started
from dotenv import load_dotenv
from second_brain_tools.directories import initial_check
# Importing production branch modules Finished

# importing directories
from second_brain_tools.config import example as sbtc_example
from second_brain_tools.config import example_elif as sbtc_example_elif
from second_brain_tools.config import _01 as sbtc_01
from second_brain_tools.config import _02 as sbtc_02
from second_brain_tools.config import _03 as sbtc_03
from second_brain_tools.config import _04 as sbtc_04
from second_brain_tools.config import _05 as sbtc_05
from second_brain_tools.config import _06 as sbtc_06
from second_brain_tools.config import _07 as sbtc_07
from second_brain_tools.config import _08 as sbtc_08
from second_brain_tools.config import _01A as sbtc_01A
from second_brain_tools.config import _01B as sbtc_01B
from second_brain_tools.config import _01B1 as sbtc_01B1
from second_brain_tools.config import _01C as sbtc_01C
from second_brain_tools.config import _01A1 as sbtc_01A1
from second_brain_tools.config import _01A2 as sbtc_01A2
from second_brain_tools.config import _01A3 as sbtc_01A3
from second_brain_tools.config import _01A4 as sbtc_01A4
from second_brain_tools.config import _01A5 as sbtc_01A5
from second_brain_tools.config import _01A6 as sbtc_01A6
from second_brain_tools.config import _01A7 as sbtc_01A7
from second_brain_tools.config import _01A8 as sbtc_01A8
from second_brain_tools.config import _01A9 as sbtc_01A9
from second_brain_tools.config import _01A10 as sbtc_01A10
from second_brain_tools.config import _01A2A as sbtc_01A2A
from second_brain_tools.config import _01A2B as sbtc_01A2B
from second_brain_tools.config import _01A2A1 as sbtc_01A2A1
from second_brain_tools.config import _01A2B1 as sbtc_01A2B1
from second_brain_tools.config import _01A8A as sbtc_01A8A
from second_brain_tools.config import _01A8B as sbtc_01A8B
from second_brain_tools.config import _01A8C as sbtc_01A8C
from second_brain_tools.config import _01A8D as sbtc_01A8D
from second_brain_tools.config import _01B as sbtc_01B
from second_brain_tools.config import _01B2 as sbtc_01B2
from second_brain_tools.config import _01B3 as sbtc_01B3
from second_brain_tools.config import _01B3A as sbtc_01B3A
from second_brain_tools.config import _01B3B as sbtc_01B3B
from second_brain_tools.config import _01C as sbtc_01C
from second_brain_tools.config import _01C1 as sbtc_01C1
from second_brain_tools.config import _01C1A as sbtc_01C1A
from second_brain_tools.config import _01C1B as sbtc_01C1B
from second_brain_tools.config import _01C1C as sbtc_01C1C
from second_brain_tools.config import _01C1D as sbtc_01C1D
from second_brain_tools.config import _01C1E as sbtc_01C1E
from second_brain_tools.config import _01C1E1 as sbtc_01C1E1
from second_brain_tools.config import _01C1E2 as sbtc_01C1E2
from second_brain_tools.config import _01C1E3 as sbtc_01C1E3
from second_brain_tools.config import _01C1E4 as sbtc_01C1E4
from second_brain_tools.config import _01C1F as sbtc_01C1F
from second_brain_tools.config import _01C1G as sbtc_01C1G
from second_brain_tools.config import _01C1H as sbtc_01C1H
from second_brain_tools.config import _01C1I as sbtc_01C1I
from second_brain_tools.config import _01C1I1 as sbtc_01C1I1
from second_brain_tools.config import _01C1I2 as sbtc_01C1I2
from second_brain_tools.config import _01C1I3 as sbtc_01C1I3
from second_brain_tools.config import _01C1I4 as sbtc_01C1I4
from second_brain_tools.config import _01C1I5 as sbtc_01C1I5
from second_brain_tools.config import _01C1I6 as sbtc_01C1I6
from second_brain_tools.config import _01C1I7 as sbtc_01C1I7
from second_brain_tools.config import _01C1I8 as sbtc_01C1I8
from second_brain_tools.config import _01C1I9 as sbtc_01C1I9
from second_brain_tools.config import _02A as sbtc_02A
from second_brain_tools.config import _02B as sbtc_02B
from second_brain_tools.config import _02A1 as sbtc_02A1
from second_brain_tools.config import _02A2 as sbtc_02A2
from second_brain_tools.config import _02A3 as sbtc_02A3
from second_brain_tools.config import _02B1 as sbtc_02B1
from second_brain_tools.config import _03A as sbtc_03A
from second_brain_tools.config import _03B as sbtc_03B
from second_brain_tools.config import _03C as sbtc_03C
from second_brain_tools.config import _03D as sbtc_03D
from second_brain_tools.config import _03A1 as sbtc_03A1
from second_brain_tools.config import _03A2 as sbtc_03A2
from second_brain_tools.config import _03A3 as sbtc_03A3
from second_brain_tools.config import _03A4 as sbtc_03A4
from second_brain_tools.config import _03B1 as sbtc_03B1
from second_brain_tools.config import _03B2 as sbtc_03B2
from second_brain_tools.config import _03B3 as sbtc_03B3
from second_brain_tools.config import _03B4 as sbtc_03B4
from second_brain_tools.config import _03B5 as sbtc_03B5
from second_brain_tools.config import _03B6 as sbtc_03B6
from second_brain_tools.config import _03B7 as sbtc_03B7
from second_brain_tools.config import _03B8 as sbtc_03B8
from second_brain_tools.config import _03B9 as sbtc_03B9
from second_brain_tools.config import _03B10 as sbtc_03B10
from second_brain_tools.config import _03B11 as sbtc_03B11
from second_brain_tools.config import _03C1 as sbtc_03C1
from second_brain_tools.config import _03C2 as sbtc_03C2
from second_brain_tools.config import _03C3 as sbtc_03C3
from second_brain_tools.config import _03C4 as sbtc_03C4
from second_brain_tools.config import _03C1A as sbtc_03C1A
from second_brain_tools.config import _03C1B as sbtc_03C1B
from second_brain_tools.config import _03C1C as sbtc_03C1C
from second_brain_tools.config import _03C1A1 as sbtc_03C1A1
from second_brain_tools.config import _03C1A2 as sbtc_03C1A2
from second_brain_tools.config import _03C1A3 as sbtc_03C1A3
from second_brain_tools.config import _03C1A4 as sbtc_03C1A4
from second_brain_tools.config import _03C1A5 as sbtc_03C1A5
from second_brain_tools.config import _03C1A6 as sbtc_03C1A6
from second_brain_tools.config import _03C1A7 as sbtc_03C1A7
from second_brain_tools.config import _03C1A8 as sbtc_03C1A8
from second_brain_tools.config import _03C1A9 as sbtc_03C1A9
from second_brain_tools.config import _03C1A10 as sbtc_03C1A10
from second_brain_tools.config import _03C1A11 as sbtc_03C1A11
from second_brain_tools.config import _03C1A12 as sbtc_03C1A12
from second_brain_tools.config import _03C1A13 as sbtc_03C1A13
from second_brain_tools.config import _03C1A14 as sbtc_03C1A14
from second_brain_tools.config import _03C1A15 as sbtc_03C1A15
from second_brain_tools.config import _03C1A16 as sbtc_03C1A16
from second_brain_tools.config import _03C1A17 as sbtc_03C1A17
from second_brain_tools.config import _03C1A18 as sbtc_03C1A18
from second_brain_tools.config import _03C1B1 as sbtc_03C1B1
from second_brain_tools.config import _03C1C1 as sbtc_03C1C1
from second_brain_tools.config import _03C2A as sbtc_03C2A
from second_brain_tools.config import _03C2B as sbtc_03C2B
from second_brain_tools.config import _03C3A as sbtc_03C3A
from second_brain_tools.config import _03C3B as sbtc_03C3B
from second_brain_tools.config import _03C3A1 as sbtc_03C3A1
from second_brain_tools.config import _03C3A2 as sbtc_03C3A2
from second_brain_tools.config import _03C3A3 as sbtc_03C3A3
from second_brain_tools.config import _03C3A4 as sbtc_03C3A4
from second_brain_tools.config import _03C3B1 as sbtc_03C3B1
from second_brain_tools.config import _03C4A as sbtc_03C4A
from second_brain_tools.config import _03D1 as sbtc_03D1
from second_brain_tools.config import _03D2 as sbtc_03D2
from second_brain_tools.config import _03D3 as sbtc_03D3
from second_brain_tools.config import _03D4 as sbtc_03D4
from second_brain_tools.config import _03D5 as sbtc_03D5
from second_brain_tools.config import _04A as sbtc_04A
from second_brain_tools.config import _04B as sbtc_04B
from second_brain_tools.config import _04C as sbtc_04C
from second_brain_tools.config import _04A1 as sbtc_04A1
from second_brain_tools.config import _04A2 as sbtc_04A2
from second_brain_tools.config import _04A3 as sbtc_04A3
from second_brain_tools.config import _04A4 as sbtc_04A4
from second_brain_tools.config import _04A5 as sbtc_04A5
from second_brain_tools.config import _04A6 as sbtc_04A6
from second_brain_tools.config import _04A7 as sbtc_04A7
from second_brain_tools.config import _04A99 as sbtc_04A99
from second_brain_tools.config import _04C1 as sbtc_04C1
from second_brain_tools.config import _05A as sbtc_05A
from second_brain_tools.config import _05B as sbtc_05B
from second_brain_tools.config import _05C as sbtc_05C
from second_brain_tools.config import _05D as sbtc_05D
from second_brain_tools.config import _05E as sbtc_05E
from second_brain_tools.config import _06A as sbtc_06A
from second_brain_tools.config import _06B as sbtc_06B
from second_brain_tools.config import _06A1 as sbtc_06A1
from second_brain_tools.config import _06B1 as sbtc_06B1
from second_brain_tools.config import _06C1 as sbtc_06C1
from second_brain_tools.config import _06C2 as sbtc_06C2
from second_brain_tools.config import _06D1 as sbtc_06D1
from second_brain_tools.config import _06D2 as sbtc_06D2
from second_brain_tools.config import _06D3 as sbtc_06D3
from second_brain_tools.config import _07A as sbtc_07A
from second_brain_tools.config import _07A1 as sbtc_07A1
from second_brain_tools.config import _07A2 as sbtc_07A2
from second_brain_tools.config import _07B as sbtc_07B
from second_brain_tools.config import _07B1 as sbtc_07B1
# importing directories

# Default Functions Calling
load_dotenv(".sbt_config")
# Default Functions Calling

"""
Below are the test which checks that all directories in the config
are resolving to their respective directory codes or not.

prefix used = test_dir_{1..X}
"""


# Started
def test_dir_example():
    dir_code = "example"
    expected_dir_path = sbtc_example
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_example_elif():
    dir_code = "example_elif"
    expected_dir_path = sbtc_example_elif
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_1():
    dir_code = "01"
    expected_dir_path = sbtc_01
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_10():
    dir_code = "01B"
    expected_dir_path = sbtc_01B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_100():
    dir_code = "03D2"
    expected_dir_path = sbtc_03D2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_101():
    dir_code = "03D3"
    expected_dir_path = sbtc_03D3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_102():
    dir_code = "03D4"
    expected_dir_path = sbtc_03D4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_103():
    dir_code = "03D5"
    expected_dir_path = sbtc_03D5
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_104():
    dir_code = "04A"
    expected_dir_path = sbtc_04A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_105():
    dir_code = "04B"
    expected_dir_path = sbtc_04B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_106():
    dir_code = "04C"
    expected_dir_path = sbtc_04C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_107():
    dir_code = "04C"
    expected_dir_path = sbtc_04C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_108():
    dir_code = "04A1"
    expected_dir_path = sbtc_04A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_109():
    dir_code = "04A2"
    expected_dir_path = sbtc_04A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_11():
    dir_code = "01B1"
    expected_dir_path = sbtc_01B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_110():
    dir_code = "04A3"
    expected_dir_path = sbtc_04A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_111():
    dir_code = "04A4"
    expected_dir_path = sbtc_04A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_112():
    dir_code = "04A5"
    expected_dir_path = sbtc_04A5
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_113():
    dir_code = "04A6"
    expected_dir_path = sbtc_04A6
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_114():
    dir_code = "04A7"
    expected_dir_path = sbtc_04A7
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_115():
    dir_code = "04A99"
    expected_dir_path = sbtc_04A99
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_116():
    dir_code = "04C1"
    expected_dir_path = sbtc_04C1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_117():
    dir_code = "05A"
    expected_dir_path = sbtc_05A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_118():
    dir_code = "05B"
    expected_dir_path = sbtc_05B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_119():
    dir_code = "05C"
    expected_dir_path = sbtc_05C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_12():
    dir_code = "01C"
    expected_dir_path = sbtc_01C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_120():
    dir_code = "05D"
    expected_dir_path = sbtc_05D
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_121():
    dir_code = "05E"
    expected_dir_path = sbtc_05E
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_122():
    dir_code = "06A"
    expected_dir_path = sbtc_06A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_123():
    dir_code = "06B"
    expected_dir_path = sbtc_06B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


"""test 124..126 are commented out because these
directories are end of support for this version."""

# def test_dir_124():
#   dir_code = "06C"
#   expected_dir_path = sbtc_06C
#   dir_path = initial_check(dir_code)
#   assert dir_path == expected_dir_path
#
#
# def test_dir_125():
#   dir_code = "06D"
#   expected_dir_path = sbtc_06D
#   dir_path = initial_check(dir_code)
#   assert dir_path == expected_dir_path
#
#
# def test_dir_126():
#   dir_code = "06E"
#   expected_dir_path = sbtc_06E
#   dir_path = initial_check(dir_code)
#   assert dir_path == expected_dir_path


def test_dir_127():
    dir_code = "06A1"
    expected_dir_path = sbtc_06A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_128():
    dir_code = "06B1"
    expected_dir_path = sbtc_06B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_129():
    dir_code = "06C1"
    expected_dir_path = sbtc_06C1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_13():
    dir_code = "01A1"
    expected_dir_path = sbtc_01A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_130():
    dir_code = "06C2"
    expected_dir_path = sbtc_06C2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_131():
    dir_code = "06D1"
    expected_dir_path = sbtc_06D1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_132():
    dir_code = "06D2"
    expected_dir_path = sbtc_06D2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_133():
    dir_code = "06D3"
    expected_dir_path = sbtc_06D3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_134():
    dir_code = "07A"
    expected_dir_path = sbtc_07A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_135():
    dir_code = "07A1"
    expected_dir_path = sbtc_07A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_136():
    dir_code = "07A2"
    expected_dir_path = sbtc_07A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_137():
    dir_code = "07B"
    expected_dir_path = sbtc_07B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_138():
    dir_code = "07B1"
    expected_dir_path = sbtc_07B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_14():
    dir_code = "01A2"
    expected_dir_path = sbtc_01A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_15():
    dir_code = "01A3"
    expected_dir_path = sbtc_01A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_16():
    dir_code = "01A4"
    expected_dir_path = sbtc_01A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_17():
    dir_code = "01A5"
    expected_dir_path = sbtc_01A5
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_18():
    dir_code = "01A6"
    expected_dir_path = sbtc_01A6
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_19():
    dir_code = "01A2A"
    expected_dir_path = sbtc_01A2A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_2():
    dir_code = "02"
    expected_dir_path = sbtc_02
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_20():
    dir_code = "01A2B"
    expected_dir_path = sbtc_01A2B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_21():
    dir_code = "01A2A1"
    expected_dir_path = sbtc_01A2A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_22():
    dir_code = "01A2B1"
    expected_dir_path = sbtc_01A2B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_23():
    dir_code = "01A3"
    expected_dir_path = sbtc_01A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_24():
    dir_code = "01A4"
    expected_dir_path = sbtc_01A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_25():
    dir_code = "01B"
    expected_dir_path = sbtc_01B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_26():
    dir_code = "01C"
    expected_dir_path = sbtc_01C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_27():
    dir_code = "01C1"
    expected_dir_path = sbtc_01C1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_28():
    dir_code = "01C1A"
    expected_dir_path = sbtc_01C1A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_29():
    dir_code = "01C1B"
    expected_dir_path = sbtc_01C1B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_3():
    dir_code = "03"
    expected_dir_path = sbtc_03
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_30():
    dir_code = "01C1C"
    expected_dir_path = sbtc_01C1C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_31():
    dir_code = "01C1D"
    expected_dir_path = sbtc_01C1D
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_32():
    dir_code = "01C1E"
    expected_dir_path = sbtc_01C1E
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_33():
    dir_code = "01C1F"
    expected_dir_path = sbtc_01C1F
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_34():
    dir_code = "01C1G"
    expected_dir_path = sbtc_01C1G
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_35():
    dir_code = "01C1H"
    expected_dir_path = sbtc_01C1H
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_36():
    dir_code = "01C1I"
    expected_dir_path = sbtc_01C1I
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_37():
    dir_code = "02A"
    expected_dir_path = sbtc_02A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_38():
    dir_code = "02B"
    expected_dir_path = sbtc_02B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_39():
    dir_code = "02A1"
    expected_dir_path = sbtc_02A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_4():
    dir_code = "04"
    expected_dir_path = sbtc_04
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_40():
    dir_code = "02A2"
    expected_dir_path = sbtc_02A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_41():
    dir_code = "02A3"
    expected_dir_path = sbtc_02A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_42():
    dir_code = "02B1"
    expected_dir_path = sbtc_02B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_43():
    dir_code = "03A"
    expected_dir_path = sbtc_03A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_44():
    dir_code = "03B"
    expected_dir_path = sbtc_03B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_45():
    dir_code = "03C"
    expected_dir_path = sbtc_03C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_46():
    dir_code = "03D"
    expected_dir_path = sbtc_03D
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_47():
    dir_code = "03A1"
    expected_dir_path = sbtc_03A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_48():
    dir_code = "03A2"
    expected_dir_path = sbtc_03A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_49():
    dir_code = "03A3"
    expected_dir_path = sbtc_03A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_5():
    dir_code = "05"
    expected_dir_path = sbtc_05
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_50():
    dir_code = "03A4"
    expected_dir_path = sbtc_03A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_51():
    dir_code = "03B1"
    expected_dir_path = sbtc_03B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_52():
    dir_code = "03B2"
    expected_dir_path = sbtc_03B2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_53():
    dir_code = "03B3"
    expected_dir_path = sbtc_03B3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_54():
    dir_code = "03B4"
    expected_dir_path = sbtc_03B4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_55():
    dir_code = "03B5"
    expected_dir_path = sbtc_03B5
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_56():
    dir_code = "03B6"
    expected_dir_path = sbtc_03B6
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_57():
    dir_code = "03B7"
    expected_dir_path = sbtc_03B7
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_58():
    dir_code = "03B8"
    expected_dir_path = sbtc_03B8
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_59():
    dir_code = "03B9"
    expected_dir_path = sbtc_03B9
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_6():
    dir_code = "06"
    expected_dir_path = sbtc_06
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_60():
    dir_code = "03B10"
    expected_dir_path = sbtc_03B10
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_61():
    dir_code = "03B11"
    expected_dir_path = sbtc_03B11
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_62():
    dir_code = "03C1"
    expected_dir_path = sbtc_03C1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_63():
    dir_code = "03C2"
    expected_dir_path = sbtc_03C2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_64():
    dir_code = "03C3"
    expected_dir_path = sbtc_03C3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_65():
    dir_code = "03C4"
    expected_dir_path = sbtc_03C4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_66():
    dir_code = "03C1A"
    expected_dir_path = sbtc_03C1A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_67():
    dir_code = "03C1B"
    expected_dir_path = sbtc_03C1B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_68():
    dir_code = "03C1C"
    expected_dir_path = sbtc_03C1C
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_69():
    dir_code = "03C1A1"
    expected_dir_path = sbtc_03C1A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_7():
    dir_code = "07"
    expected_dir_path = sbtc_07
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_70():
    dir_code = "03C1A2"
    expected_dir_path = sbtc_03C1A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_71():
    dir_code = "03C1A3"
    expected_dir_path = sbtc_03C1A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_72():
    dir_code = "03C1A4"
    expected_dir_path = sbtc_03C1A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_73():
    dir_code = "03C1A5"
    expected_dir_path = sbtc_03C1A5
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_74():
    dir_code = "03C1A6"
    expected_dir_path = sbtc_03C1A6
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_75():
    dir_code = "03C1A7"
    expected_dir_path = sbtc_03C1A7
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_76():
    dir_code = "03C1A8"
    expected_dir_path = sbtc_03C1A8
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_77():
    dir_code = "03C1A9"
    expected_dir_path = sbtc_03C1A9
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_78():
    dir_code = "03C1A10"
    expected_dir_path = sbtc_03C1A10
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_79():
    dir_code = "03C1A11"
    expected_dir_path = sbtc_03C1A11
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_8():
    dir_code = "08"
    expected_dir_path = sbtc_08
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_80():
    dir_code = "03C1A12"
    expected_dir_path = sbtc_03C1A12
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_81():
    dir_code = "03C1A13"
    expected_dir_path = sbtc_03C1A13
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_82():
    dir_code = "03C1A14"
    expected_dir_path = sbtc_03C1A14
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_83():
    dir_code = "03C1A15"
    expected_dir_path = sbtc_03C1A15
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_84():
    dir_code = "03C1A16"
    expected_dir_path = sbtc_03C1A16
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_85():
    dir_code = "03C1A17"
    expected_dir_path = sbtc_03C1A17
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_86():
    dir_code = "03C1A18"
    expected_dir_path = sbtc_03C1A18
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_87():
    dir_code = "03C1B1"
    expected_dir_path = sbtc_03C1B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_88():
    dir_code = "03C1C1"
    expected_dir_path = sbtc_03C1C1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_89():
    dir_code = "03C2A"
    expected_dir_path = sbtc_03C2A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_9():
    dir_code = "01A"
    expected_dir_path = sbtc_01A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_90():
    dir_code = "03C2B"
    expected_dir_path = sbtc_03C2B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_91():
    dir_code = "03C3A"
    expected_dir_path = sbtc_03C3A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_92():
    dir_code = "03C3B"
    expected_dir_path = sbtc_03C3B
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_93():
    dir_code = "03C3A1"
    expected_dir_path = sbtc_03C3A1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_94():
    dir_code = "03C3A2"
    expected_dir_path = sbtc_03C3A2
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_95():
    dir_code = "03C3A3"
    expected_dir_path = sbtc_03C3A3
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_96():
    dir_code = "03C3A4"
    expected_dir_path = sbtc_03C3A4
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_97():
    dir_code = "03C3B1"
    expected_dir_path = sbtc_03C3B1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_98():
    dir_code = "03C4A"
    expected_dir_path = sbtc_03C4A
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path


def test_dir_99():
    dir_code = "03D1"
    expected_dir_path = sbtc_03D1
    dir_path = initial_check(dir_code)
    assert dir_path == expected_dir_path
# Ended
