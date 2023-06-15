from mymodule import my_func  # module is a .py file (in same dir)
from MyMainPackage import some_main_script # packages are .py files in subfolders containing a blank __init__.py
from MyMainPackage.SubPackage import mysubscript # packages are .py files in subfolders containing a blank __init__.py

my_func()
some_main_script.report_main()
mysubscript.sub_report()
