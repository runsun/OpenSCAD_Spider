# OpenSCAD_Spider

Download remote OpenSCAD files

A python script to download remote OpenSCAD files. The idea is similar
to the `pip` package installer in python. 

## What `openscad_spider.py` does:

1. Create 2 folders in the `...OpenSCAD/libraries` folder:

   ```
   * spider_food
   * spider_food_store
   ```
   
2. Download OpenSCAD file(s) from one of SPIDER_WEBS. It is defined
   in a dict in python and contains urls of remote sites:   
 
   ```
    SPIDER_WEBS={
     'github':'https://github.com'
    ,'thingiverse':'https://www.thingiverse.com'
    }
   ```
   
   and is specified in a call to this file:
   
   `> python openscad_spider.py --web github`
   
3. Additionally, `libname` must be specified, and optionally `author`:

   `> ... --libname <some_name> --author <author>`
   
   Consider: for github, use `clone`; for thingiverse: use `unzip`
   
4. Users can also specify a url not in SPIDER_WEBS:
   
   `> python openscad_spider.py --web http://a/b/c`
         
   which directly points to a `.scad` file. 
   
   In this case, `libname` and `author` are to be ignored.

5. When `--web` is not a direct url to a `.scad` file, this prog needs
   to srape through the given webpage to dig out the direct download url. 
   This can be done with either python itself, or consider the other
   webpage scrapping tool like **BeautifulSoup** or **Scrapy**.
            
6. The downloaded file(s) will be saved to 

   `...OpenSCAD/libraries/spider_food`
           
7. A new file, `spider_template.scad`, is created in the current 
   working folder, containing:
   
   `include <sider_food/<libname>>`

8. Run `spider_template.scad` in OpenSCAD
    
9. Upon exist, ask users if this lib is to be kept. If yes, make
   a copy to `...OpenSCAD/libraries/spider_food_store`
 
## Project Progress 

20180313- Project plan outlined in README.md   