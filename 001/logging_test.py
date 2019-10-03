#!/usr/bin/env python3
import logging
def main():
    # create formatter
    #formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d(%(funcName)s): %(message)s')
    #formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s:%(lineno)d(%(funcName)s): %(message)s')
    formatter = logging.Formatter('{name} {asctime} [{levelname}] {module}:{lineno}({funcName}): {message}', '%m-%d %H:%M:%S', style='{')
    formatter_a =  logging.Formatter('[a logger]   - {name} [{levelname}] {module}:{lineno}({funcName}): {message}', style='{')
    formatter_ab = logging.Formatter('[a.b logger] - {name} [{levelname}] {module}:{lineno}({funcName}): {message}', style='{')
    formatter_ac = logging.Formatter('[a.c logger] - {name} [{levelname}] {module}:{lineno}({funcName}): {message}', style='{')

    # create console handler
    Handler=logging.StreamHandler()
    Handler_ab=logging.StreamHandler()
    Handler_ac=logging.StreamHandler()

    # add formatter to Handler
    Handler.setFormatter(formatter_a)
    Handler_ab.setFormatter(formatter_ab)
    Handler_ac.setFormatter(formatter_ac)

    # add Handler to logger
    a=logging.getLogger("a")
    a.addHandler(Handler)

    ab=logging.getLogger("a.b")
    ab.addHandler(Handler_ab)
    #ab.propagate=False; # don't pass to parent logger


    ac=logging.getLogger("a.c")
    ac.addHandler(Handler_ac)

    # Filters can be used by Handlers and Loggers
    flt = logging.Filter("a.b")
    #a.addFilter(flt)
    ab.addFilter(flt)
    ac.addFilter(flt)
    #a.warn("a_logmessage")
    ab.warn("ab_logmessage")
    ac.warn("ac_logmessage")

if "__main__" == __name__:
    try:
        main()
    except Exception as main_err:
        print(main_err)

