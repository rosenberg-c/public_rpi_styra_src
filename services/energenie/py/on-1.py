"""
This file is called from request service for manual control
"""
from lib.energenie_handlers import run_on_script


def main():
    run_on_script(1)


if __name__ == '__main__':
    main()
