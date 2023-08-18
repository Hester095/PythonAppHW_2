import subprocess

import subprocess
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False
def	test_stepl():
# testl
    assert checkout("cd	/home/user/tst;	7z	a	../out/arx2", "Everything is Ok"), "testl FAIL"
def	test_step2():
# test2
    assert checkout("cd	/home/user/out;	7z	e	arx2.7z	-o/home/zerg/folderl -y", "Everything is Ok"), "test2 FAIL"
def	test_step3():
# test3
    assert checkout("cd	/home/user/out;	7z	t	arx2.7z",	"Everything is Ok"), "test3 FAIL"
def	test_step4():
# test4
    assert checkout("cd /home/user/out; 7z l arx2.7z", "Name\n----"), "test4 FAIL" 
def test_step5(): 
# test5
    assert checkout("cd /home/user/out; 7z x arx2.7z -o/home/zerg/folderx -y", "Everything is Ok"), "test5 FAIL"
