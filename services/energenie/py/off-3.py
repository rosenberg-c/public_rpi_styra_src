"""
This file is called from request service for manual control
"""
from lib.energenie_handlers import run_off_script


def main():
    run_off_script(3)


if __name__ == '__main__':
    main()
