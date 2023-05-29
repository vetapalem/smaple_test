

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as ch
import unittest as ut,time as tt
import learn_file as l
import HtmlTestRunner

from  page_object_model import w3_python_school as ck



#test both search bar amazon flipkart


class serachbar(ut.TestCase):
    de='*'*10
    
    we=webdriver.ChromeOptions()
    we.add_argument('--disable-notifications')

    def setUp(self):
        self.__driv=webdriver.Chrome(service=Service(executable_path=ch().install()),options=self.we)
        self.__driv.maximize_window()
        

    @ut.skip(reason='woriking fine')
    def test_amazon(self):
        self.mi=l.test_scenario__001(self.__driv)
        self.mi.amazon()
        

    @ut.skip(reason='fuctionality is good...')
    def test_flipkart(self):
        self.mi=l.test_scenario__001(self.__driv)
        self.mi.flipkart()
    
    def test_w3school(self):
        self.ma=ck.w3_code_test(self.__driv)
        self.ma.python_scripts()
    

    def tearDown(self):
        self.__driv.close()


style='''
body{
    border-style:ridge;
    color:white;
    background-color:black;
    font-weight:bold;
}
'''



if __name__ == "__main__":
    test=ut.TestLoader().loadTestsFromTestCase(serachbar)
    suite=ut.TestSuite([test])
#    normal html-test runner
    # HtmlTestRunner.HTMLTestRunner(
        
        
    
    #     verbosity=2,
    #     report_name='search_bar_fucction_amazon_flipkart6',
    #     report_title='flipkart,amazon',
    #     add_timestamp=False,
    #     open_in_browser=True,
    #     combine_reports=True,
    #     output=r'../test_reports',
    # ).run(suite)
    runner = HtmlTestRunner.HTMLTestRunner(
        
        log=False, 
        verbosity=2, 
        output='report', 
        title='w3school_test', 
        report_name='automated_hybried3',
        open_in_browser=True, 
        description="HTMLTestReport", 
        tested_by="krishna",
        add_traceback=False
        )

    runner.run(suite)