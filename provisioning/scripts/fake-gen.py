import sys, os, traceback, optparse
import time
import re

from faker import Factory
#from pexpect import run, spawn

def generate_entry(fake):
    p = fake.profile()
    p.pop('website')
    p.pop('current_location')
    p.pop('residence')
    p.pop('address')
    p['code'] = fake.pyint()
    p['latitude'] = fake.latitude()
    p['longtitude'] = fake.longitude()
    p['certified'] = fake.boolean()
    p['web-site'] = fake.url()
    p['credit-card'] = fake.credit_card_provider()
    p['phone-number'] = fake.phone_number()
    return p




def main ():
    global options, args
    size = 10
    if len(args) is 1:
        size = int(args[0])
    fake = Factory.create()
    SEP = u' ; '
    with open("data.csv", "w") as f:
        f.write(SEP.join(generate_entry(fake).keys()) + "\n")
        for i in xrange(0, size):
            entry = generate_entry(fake).values()
            s = SEP.join([repr(x) if type(x) == type(str()) else unicode(x) for x in entry])
            f.write(s + "\n")




if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=globals()['__doc__'], version='$Id$')
        parser.add_option ('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        main()
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)