#!/usr/bin/env python3
import logging
def main():
    # create formatter
    #formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d(%(funcName)s): %(message)s')
    #formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s:%(lineno)d(%(funcName)s): %(message)s')
    formatter = logging.Formatter('{asctime} [{levelname}] {module}:{lineno}({funcName}): {message}', '%m-%d %H:%M:%S', style='{')

    # create console handler
    Handler=logging.StreamHandler()

    # add formatter to Handler
    Handler.setFormatter(formatter)

    # add Handler to logger
    a=logging.getLogger("a")
    a.addHandler(Handler)
    a.warn("logmessage")

    ab=logging.getLogger("a.b")

if "__main__" == __name__:
    try:
        main()
    except Exception as main_err:
        print(main_err)

