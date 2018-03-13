# OpenSCAD_Spider

__description__ = "Download remote scad file(s)."
__author__= "Runsun Pan"
__version__= "0.0.0"

import argparse 

SPIDER_WEBS={
 'github':'https://github.com'
,'thingiverse':'https://www.thingiverse.com'
,'openscad': r'C:\Users\Daniu\Documents\OpenSCAD'
}


# argument setup and parse
argp = argparse.ArgumentParser( 
       prog= __file__
       ,description=  __description__+ "\n" + __author__ )
argp.add_argument('--version', action='version'
                 , version='%(prog)s '+__version__ 
                 , help='Shows version and exits.')       
argp.add_argument("repo", metavar="word", type=str, default="github", help="Name of repositories." )
argp.add_argument("repourl", metavar="word", type=str, default="", help="Url of repositories. Overriding repo." )

argp.add_argument("libname", metavar="word", type=str, help="Name of remote lib." )
argp.add_argument("libowner", metavar="word", type=str, help="Name of remote lib owner." )


#argp.add_argument("-f", metavar="folder", type=str, default=".", help="Target folder")
#argp.add_argument("-p", metavar="prefix", type=str, default="function|module"
#                 , help="prefix. Could be a str in regexp form. Default='function|module'")
#argp.add_argument("-a", metavar="activeModule", type=bool
#                  , default=0
#                  , help="Search for modules that are set to run at this moment by matching 'xxx(...);'. Useful for complex lib."
#                  ) 
#argp.add_argument("-i", metavar="includePrefix", type=int
#                  , default=1
#                  , help="Int. 1 = Include prefix defined in -p"
#                  )
#
#argp.add_argument('-x', metavar="fileExt", type=str, default="scad"
#                 , help="Specifiy file extension like doc, py ... etc. Default:scad"
#                 )     
                                               
args= argp.parse_args()

